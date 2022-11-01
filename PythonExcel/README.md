# 安装

## 安装openpyxl

![image-20220826142055919](pic/image-20220826142055919.png)

## 打开环境的idle.bat

D:\Anaconda\envs\py38_spider\Lib\idlelib



# 创建表格

<img src="pic/image-20220826144624946.png" alt="image-20220826144624946" style="zoom:80%;" />



# 将txt转为excel

## 爬虫网页转为txt

<img src="pic/image-20220826151408717.png" alt="image-20220826151408717" style="zoom:80%;" />

```python
import requests
import bs4
import re


def open_url(url):
    # 使用代理
    # proxies = {"http": "127.0.0.1:1080", "https": "127.0.0.1:1080"}
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36'}

    # res = requests.get(url, headers=headers, proxies=proxies)
    res = requests.get(url, headers=headers)

    return res


def find_movies(res):
    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    # 电影名
    movies = []
    targets = soup.find_all("div", class_="hd")
    for each in targets:
        movies.append(each.a.span.text)

    # 评分
    ranks = []
    targets = soup.find_all("span", class_="rating_num")
    for each in targets:
        ranks.append(' 评分：%s ' % each.text)

    # 资料
    messages = []
    targets = soup.find_all("div", class_="bd")
    for each in targets:
        try:
            messages.append(each.p.text.split('\n')[1].strip() + each.p.text.split('\n')[2].strip())
        except:
            continue

    result = []
    length = len(movies)
    for i in range(length):
        result.append(movies[i] + ranks[i] + messages[i] + '\n')

    return result


# 找出一共有多少个页面
def find_depth(res):
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    depth = soup.find('span', class_='next').previous_sibling.previous_sibling.text

    return int(depth)


def main():
    host = "https://movie.douban.com/top250"
    res = open_url(host)
    depth = find_depth(res)

    result = []
    for i in range(depth):
        url = host + '/?start=' + str(25 * i)
        res = open_url(url)
        result.extend(find_movies(res))

    with open("豆瓣TOP250电影.txt", "w", encoding="utf-8") as f:
        for each in result:
            f.write(each)


if __name__ == "__main__":
    main()
```

## txt转为excel

<img src="pic/image-20220826151342422.png" alt="image-20220826151342422" style="zoom:80%;" />

```python
import requests
import bs4
import re
import openpyxl
 
def open_url(url):
    # 使用代理
    # proxies = {"http": "127.0.0.1:1080", "https": "127.0.0.1:1080"}
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36'}
 
    # res = requests.get(url, headers=headers, proxies=proxies)
    res = requests.get(url, headers=headers)
 
    return res
 
def find_movies(res):
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
 
    # 电影名
    movies = []
    targets = soup.find_all("div", class_="hd")
    for each in targets:
        movies.append(each.a.span.text)
 
    # 评分
    ranks = []
    targets = soup.find_all("span", class_="rating_num")
    for each in targets:
        ranks.append(each.text)
 
    # 资料
    messages = []
    targets = soup.find_all("div", class_="bd")
    for each in targets:
        try:
            messages.append(each.p.text.split('\n')[1].strip() + each.p.text.split('\n')[2].strip())
        except:
            continue
 
    result = []
    length = len(movies)
    for i in range(length):
        result.append([movies[i],ranks[i],messages[i]])
 
    return result


#保存为xlsx, import openpyxl
def save_to_excel(result):
    wb = openpyxl.Workbook()
    ws = wb.active

    ws['A1'] = '电影名称'
    ws['B1'] = '评分'
    ws['C1'] = '资料'

    for each in result:
        ws.append(each)     #each是一个列表元组，而不是字符串

    wb.save("豆瓣TOP250电影.xlsx")


# 找出一共有多少个页面
def find_depth(res):
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    depth = soup.find('span', class_='next').previous_sibling.previous_sibling.text
 
    return int(depth)
 
def main():
    host = "https://movie.douban.com/top250"
    res = open_url(host)
    depth = find_depth(res)
 
    result = []
    for i in range(depth):
        url = host + '/?start=' + str(25 * i)
        res = open_url(url)
        result.extend(find_movies(res))

    save_to_excel(result)

if __name__ == "__main__":
    main()
```



# 打开工作簿

<img src="pic/image-20220826152523209.png" alt="image-20220826152523209" style="zoom:80%;" />

# 处理工作表

## 获取名称

<img src="pic/image-20220826153106478.png" alt="image-20220826153106478" style="zoom:80%;" />

## 打开工作表

<img src="pic/image-20220826153152630.png" alt="image-20220826153152630" style="zoom:80%;" />

## 创建工作表

<img src="pic/image-20220826153226329.png" alt="image-20220826153226329" style="zoom:80%;" />

## 删除工作表

### 方法一

<img src="pic/image-20220826154353964.png" alt="image-20220826154353964" style="zoom:80%;" />

### 方法二

<img src="pic/image-20220826154419693.png" alt="image-20220826154419693" style="zoom:80%;" />

## 定位单元格

<img src="pic/image-20220826155142921.png" alt="image-20220826155142921" style="zoom:80%;" />

## 列数转换

<img src="pic/image-20220826160228425.png" alt="image-20220826160228425" style="zoom:80%;" />

## 切片

<img src="pic/image-20220826160304219.png" alt="image-20220826160304219" style="zoom:80%;" />

<img src="pic/image-20220826160319643.png" alt="image-20220826160319643" style="zoom:80%;" />

<img src="pic/image-20220826160346091.png" alt="image-20220826160346091" style="zoom:80%;" />

## 拷贝工作表

<img src="pic/image-20220826160804834.png" alt="image-20220826160804834" style="zoom:80%;" />

## 修改工作表标签颜色

<img src="pic/image-20220826161751036.png" alt="image-20220826161751036" style="zoom:80%;" />

## 调整行高和列宽

<img src="pic/image-20220826162934006.png" alt="image-20220826162934006" style="zoom:80%;" />

## 合并单元格

### 合并

<img src="pic/image-20220826170405889.png" alt="image-20220826170405889" style="zoom:80%;" />

### 拆分

<img src="pic/image-20220826170639510.png" alt="image-20220826170639510" style="zoom:80%;" />

## 冻结与解冻

### 冻结

<img src="pic/image-20220826172050459.png" alt="image-20220826172050459" style="zoom:80%;" />

### 解冻

![image-20220826172256133](pic/image-20220826172256133.png)
