from lxml import etree

xml = """
<nitf>
    <head>
        <title>Colombia Earthquake</title>
    </head>
    <body>
        <headline>
            <hl1>143 Dead in Colombia Earthquake</hl1>
        </headline>
        <byline>
            <bytag>By Jared Kotler, Associated Press Writer</bytag>
        </byline>
        <date>Monday January 25 2000</date>
        <dateline>
            <location>Bogota, Colombia</location>
            <date>Monday January 25 1999 7:28 ET</date>
        </dateline>
        <div>
            <date>Monday January 25 3000</date>
        </div>
    </body>
</nitf>
"""

tree = etree.XML(xml)
# result = tree.xpath("/nitf/head/title/text()")
# result = tree.xpath("/nitf/head/text()")
# result = tree.xpath("/nitf/head/title/text()")    #['Colombia Earthquake']

# result = tree.xpath("/nitf/body/date/text()")    #['Monday January 25 2000']
# result = tree.xpath("/nitf/body//date/text()")     # 后代 ['Monday January 25 2000', 'Monday January 25 1999 7:28 ET', 'Monday January 25 3000']
# result = tree.xpath("/nitf/body/*/date/text()")    # 通配符 ['Monday January 25 1999 7:28 ET', 'Monday January 25 3000']
result = tree.xpath("/nitf//date/text()")     #nift下的所有date的信息提取出来  ['Monday January 25 2000', 'Monday January 25 1999 7:28 ET', 'Monday January 25 3000']
print(result)