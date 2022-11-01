from lxml import etree

tree = etree.parse("b.html")

# result = tree.xpath('/html')
# result = tree.xpath('/html/body/ul/li/a/text()')    #['百度', '谷歌', '搜狗']
# result = tree.xpath('/html/body/ul/li[1]/a/text()')    #['百度']
# result = tree.xpath('/html/body/ol/li/a[@href="dapao"]/text()')    #['大炮']

ol_li_list = tree.xpath("/html/body/ol/li")
for li in ol_li_list:
    result = li.xpath("./a/text()")    #在li中继续去寻找，是相对查找，需要./开头
    print(result)
    result2 = li.xpath("./a/@href")    #拿到标签的属性数据
    print(result2)

print(tree.xpath("/html/body/ul/li/a/@href"))    #一次性获得要求的所有节点的href，['http://www.baidu.com', 'http://www.google.com', 'http://www.sogou.com']

print(tree.xpath('/html/body/div[1]/text()'))    #利用浏览器的源码复制