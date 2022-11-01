import requests

url = 'https://fanyi.baidu.com/sug'

s = input("输入你要翻译的英文：")
#发送的数据必须放在字典中，通过data参数进行传递
ever = {
    "kw": s
}

#发送post请求
resp = requests.post(url,data=ever)
print(resp.json())     #将服务器返回的内容直接处理成json => dict字典