import requests
import re
import csv
import time

url = "https://search.cctv.com/search.php"

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.27"
}

param = {
    "qtext": "台湾海峡",
    "sort": "relevance",
    "type": "web",
    "vtime": "",
    "datepid": "1",
    "channel": "新闻",
    "page": "1"
}

# 收纳子页面链接
child_urls = []
obj1 = re.compile(r'<div class="tright">.*?<span lanmu1="(?P<childul>.*?)" lanmu2.*?', re.S)

for i in range(15):
    param["page"] = str(i)
    resp1 = requests.get(url, headers=header, params=param)
    resp1.encoding = "utf-8"
    page_content1 = resp1.text
    result1 = obj1.finditer(page_content1)
    for it in result1:
        child_urls.append(it.group("childul"))
    time.sleep(1)

# resp1 = requests.get(url, headers=header, params=param)
# resp1.encoding = "utf-8"
# page_content1 = resp1.text
# result1 = obj1.finditer(page_content1)
# for it in result1:
#     child_urls.append(it.group("childul"))
# time.sleep(1)

obj2 = re.compile(r'<div class="info1">.*?\|(?P<ti>.*?)</div>',re.S)

obj3 = re.compile(r'<div class="content_area" id="content_area">.*?<p.*?</strong>(?P<content1>.*?)</p>'
                  r'|<div class="content_area" id="content_area">.*?</strong></p>.*?>(?P<content2>.*?)</p>'
                  r'|<div class="content_area" id="content_area">.*?<p.*?>(?P<content3>.*?)</p>',re.S)

#创建文件
content_list = []
for ul in child_urls:
    print(ul)
    resp2 = requests.get(ul,headers=header)
    resp2.encoding = "utf-8"
    page_content2 = resp2.text
    result2 = obj2.finditer(page_content2)
    result3 = obj3.finditer(page_content2)
    for i1 in result2:
        print("".join(i1.group("ti").strip().split()))
    for i3 in result3:
        strs = ""
        if i3.group("content1") is not None and i3.group("content1") != "":
            strs = "".join(i3.group("content1").strip().split())
        elif i3.group("content2") is not None and i3.group("content2") != "":
            strs = "".join(i3.group("content2").strip().split())
        elif i3.group("content3") is not None and i3.group("content3") != "":
            strs = "".join(i3.group("content3").strip().split())
        else:
            continue
        strs = strs.replace('&ldquo;', '\"').replace('&rdquo;', '\"').replace('&mdash;','——').replace("<br/>","")
        content_list.append(strs)
    time.sleep(0.5)

for i in content_list:
    print(i.split())

with open("army.csv",mode="w",encoding="utf-8") as f:
    csv_writer = csv.writer(f)
    for i in content_list:
        csv_writer.writerow(i.split())

print("over!")