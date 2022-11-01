import requests
from lxml import etree

url = "https://hubei.zbj.com/search/service"

header = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.27"
}

param = {
    "kw": "saas",
    "r": "1"
}

resp = requests.get(url,headers=header,params=param)

# print(resp.text)

#解析
html = etree.HTML(resp.text)

#拿到每一个服务商的div
divs = html.xpath("/html/body/div[2]/div/div/div[3]/div/div[3]/div[4]/div[1]/div")    #最后一个div[1]改为div
print(divs)
for div in divs:
    price = div.xpath("./div/div[3]/div[1]/span/text()")    #用相对路径找到
    print(price)