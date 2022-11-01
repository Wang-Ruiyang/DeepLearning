import requests

query = input("输入你要查找的信息：")

url = f'http://www.baidu.com/s?wd={query}'

#伪装成非机器
dic = {
    "User-Agernt": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.27"
}

resp = requests.get(url,headers=dic)   #处理一个小小的反爬机制

print(resp)
print(resp.text)