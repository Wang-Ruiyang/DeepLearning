import requests

# url = "https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start=0&limit=20"
url = "https://movie.douban.com/j/chart/top_list"

param = {
    "type": "11",
    "interval_id": "100:90",
    "action": "",
    "start": "0",    #翻页时会变
    "limit": "20"
}

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.27"
}

resp = requests.get(url=url,params=param,headers=header)

# print(resp.request.url)    #https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start=0&limit=20
# print(resp.request.headers)    #{'User-Agent': 'python-requests/2.28.1', 'Accept-Encoding': 'gzip, deflate, br', 'Accept': '*/*', 'Connection': 'keep-alive'}
print(resp.text)