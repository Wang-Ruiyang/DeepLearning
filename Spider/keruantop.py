import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.shanghairanking.cn/rankings/bcur/202011"

header = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.27"
}

resp = requests.get(url,headers=header)
resp.encoding = "utf-8"

#解析数据，把页面源代码交给BeautifulSoup进行处理，生成bs对象
page = BeautifulSoup(resp.text, "html.parser")    #"html.parser"原来告诉解析器传入的是HTML，可以避免警告

#从bs对象中查找属性
# table = page.find("table", class_="rk-table")    #查找class="rk-table"的table标签，因为class是python关键字，所以bs可以在class后加一个_，以作区分
table = page.find("table",attrs={"class":"rk-table"})     #与上面的效果等同
# print(table)

#删掉表头
trs = table.find_all("tr")[1:]     #将每一个tr（行）提取出来，并作切片，删去第一行（表头）

#创建csv
f = open("keruan.csv",mode="w",encoding="utf-8")
csvwriter = csv.writer(f)

for tr in trs:
    tds = tr.find_all("td")
    num = tds[0].text.strip()
    name = tr.find("a",attrs={"class":"name-cn"}).text.strip()
    city = tds[2].text.strip()
    type = tds[3].text.strip()
    score = tds[4].text.strip()
    level = tds[5].text.strip()
    csvwriter.writerow([num, name, city, type, score, level])

f.close()