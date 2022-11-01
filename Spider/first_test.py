from urllib.request import urlopen

url = "http://www.baidu.com"
resp = urlopen(url)    #打开网址，返回数据

with open("mybaidu.html",mode="w") as f:
    f.write(resp.read().decode("utf-8"))
