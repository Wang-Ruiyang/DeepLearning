import requests
import re
import csv

url = "https://movie.douban.com/top250"

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.27"
}

param = {
    "start": "",
    "filter": ""
}

f = open("dbtop250.csv",mode="w",encoding="utf-8")
csvwriter = csv.writer(f)

#for i in range(0,250,25):
i = 0
while i<250:
    param["start"] = str(i)
    resp = requests.get(url, headers=header, params=param)
    page_content = resp.text
    obj = re.compile(r'<li>.*?<div class="item">.*?<span class="title">(?P<name>.*?)'
                     r'</span>.*?<p class="">.*?<br>(?P<year>.*?)&nbsp.*?'
                     r'<span class="rating_num" property="v:average">(?P<score>.*?)</span>.*?'
                     r'<span>(?P<num>.*?)人评价</span>', re.S)
    result = obj.finditer(page_content)
    for it in result:
        dic = it.groupdict()  # 将数据存成字典的格式
        dic["year"] = dic["year"].strip()
        csvwriter.writerow(dic.values())  # 将字典的数据写入csv的每一行
    i += 25

f.close()
print("over!")