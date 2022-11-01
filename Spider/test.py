import requests
import re

url = "https://news.cctv.com/2022/04/27/ARTIAnlmqHd67dCvokvBsmCv220427.shtml"

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.27"
}

obj1 = re.compile(r'<div class="content_area" id="content_area">.*?<p.*?</strong>(?P<content1>.*?)</p>',re.S)

resp = requests.get(url,headers=header)
resp.encoding = "utf-8"
page_content = resp.text
result = obj1.finditer(page_content)

for i in result:
    print(i.group("content1") is not None and i.group("content1") != "")

