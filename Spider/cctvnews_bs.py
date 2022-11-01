import requests
import re
from bs4 import BeautifulSoup
import csv

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

rule = r'>(.*?)<'

child_urls = []

for i in range(20):
    param["page"] = str(i)
    resp = requests.get(url, headers=header, params=param)
    resp.encoding = "utf-8"
    main_page = BeautifulSoup(resp.text, "html.parser")
    ul_list = main_page.find("div", attrs={"class": "tuwenjg"}).find("ul").find_all("li")
    for c in ul_list:
        child_urls.append(c.find("h3").find("span").get("lanmu1"))

content_list = []

for u in child_urls:
    print(u)
    resp2 = requests.get(u, headers=header)
    resp2.encoding = "utf-8"
    child_page = BeautifulSoup(resp2.text, "html.parser")
    try:
        p_list = child_page.find("div", attrs={"class": "cnt_bd"}).find_all("p")
    except AttributeError as a:
        try:
            p_list = child_page.find("div", attrs={"class": "content_area"}).find("p",
                                                                                  attrs={"style": "text-indent: 2em;"})
        except AttributeError as a:
            try:
                p_list = child_page.find("div", attrs={"class": "content_area"}).find("p")
            except:
                pass
    st = "".join("".join(re.findall(rule, str(p_list))).strip().split())
    content_list.append(st)


with open("army_bs.csv", mode="w", encoding="utf-8") as f:
    csv_writer = csv.writer(f)
    for i in content_list:
        csv_writer.writerow(i.split())

print("over")