import requests
from bs4 import BeautifulSoup
import time

url = "https://www.toopic.cn"

header = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.27"
}

#获取页面源代码
resp = requests.get(url, headers=header)
resp.encoding = "utf-8"
# print(resp.text)

#解析数据，把页面源代码交给BeautifulSoup进行处理，生成bs对象
main_page = BeautifulSoup(resp.text, "html.parser")    #"html.parser"原来告诉解析器传入的是HTML，可以避免警告

#提取图片子页面短链接
alist = main_page.find("ul",attrs={"class":"clearfix pic-list gallery"}).find_all("a",attrs={"class":"pic"})
# print(alist)

#合成子页面完整链接
child_urls = []
for a in alist:
     child_urls.append(url+a.get("href"))      #通过get()函数获取每个a标签中的href字段
# print(child_urls)

#生成图片链接
img_url = []
for childul in child_urls:
    resp2 = requests.get(childul, headers=header)
    resp2.encoding = "utf-8"
    child_page = BeautifulSoup(resp2.text,"html.parser")
    imglist = child_page.find("div",attrs={"class":"preview-pic"}).find_all("img")
    for i in imglist:
        img_url.append(url+i.get("src"))
# print(img_url)

#下载图片
for img in img_url:
    img_resp = requests.get(img)     #获取图片请求
    img_name  = img.split("/")[-1]    #拿到url最后一个/之后的内容
    with open("img/"+img_name,mode="wb") as f:    #能自动f.close()
        f.write(img_resp.content)     #将文件以字节的形式写入
    print(img_name+"-over!")
    time.sleep(1)    #休息1s，防止被系统干掉

