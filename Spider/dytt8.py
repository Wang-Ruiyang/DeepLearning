import re
import requests
import csv

base_url = "https://dy.dytt8.net/"
url = "https://dy.dytt8.net/index2.htm"

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.27"
}

# resp.text为源代码
resp = requests.get(url, headers=header)   #如果有安全验证，则加上 verify=False 字段
resp.encoding = "gb2312"     #和网站定义编码一致

#正则表达式模板，提取电影链接（多个）
obj = re.compile(r"最新华语电视剧推荐.*?<ul>(?P<mvsul>.*?)</ul>",re.S)
#从很多链接等字符串中区分出链接
obj2 = re.compile(r"<a href='(?P<movieul>.*?)'>2022年内地电视剧.*?<br/>",re.S)

result = obj.finditer(resp.text)
child_url_list = []

for i in result:
    # print(i.group("mvsul"))
    result2 = obj2.finditer(i.group("mvsul"))
    for ii in result2:
        # print(ii.group("movieul"))
        child_href = base_url + ii.group("movieul")
        child_url_list.append(child_href)    #将子页面链接保存到列表
        # print(child_href)

# print(child_url_list)

#遍历子页面链接列表，进入每一个链接，提取需要的内容
obj3 = re.compile(r"<title>2022年内地电视剧(?P<name>.*?)迅雷下载_电影天堂</title>.*?【下载地址】.*?</p>(?P<download_uls>.*?) <br>",re.S)
obj4 = re.compile(r'.*?<a href=(?P<downul>.*?)">ftp:.*?</table>',re.S)
ul_dir ={}

f = open("moviedown.csv",mode="w",encoding="utf-8")
csvwriter = csv.writer(f)

for href in child_url_list:
    resp2 = requests.get(href, headers=header)
    resp2.encoding = "gb2312"
    result3 = obj3.finditer(resp2.text)
    ul_list = []
    for us in result3:
        # print(u.group("download_ul"))
        result4 = obj4.finditer(us.group("download_uls"))
        for u in result4:
            ul_list.append(u.group("downul"))
        ul_dir[us.group("name")] = ul_list      #将列表放入字典中，key为剧名

csvwriter.writerow(ul_dir.values())  # 将字典的数据写入csv的每一行

f.close()
