import requests
import re
from bs4 import BeautifulSoup
import time

url = "https://news.cctv.com/2022/08/28/ARTIxm50Po9nW6d27wAAsFw8220828.shtml"

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.27"
}

rule = r'>(.*?)<'

resp2 = requests.get(url, headers=header)
resp2.encoding = "utf-8"
child_page = BeautifulSoup(resp2.text, "html.parser")

try:
    p_list = child_page.find("div", attrs={"class": "cnt_bd"}).find_all("p")
except AttributeError as a:
    try:
        p_list = child_page.find("div", attrs={"class": "content_area"}).find("p", attrs={"style": "text-indent: 2em;"})
    except AttributeError as a:
        try:
            p_list = child_page.find("div", attrs={"class": "content_area"}).find("p")
        except:
            pass


st = "".join("".join(re.findall(rule, str(p_list))).strip().split())
print(st)
# for p in p_list:
#     print(p)