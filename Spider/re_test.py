import re

s = """
<div class='jay'><span id='1'>联通</span></div>
<div class='jj'><span id='2'>移动</span></div>
<div class='jolin'><span id='3'>电信</span></div>
<div class='sylar'><span id='4'>广电</span></div>
<div class='tory'><span id='5'>铁通</span></div>
"""

obj = re.compile(r"<div class='.*?'><span id='(?P<id>\d+)'>(?P<name>.*?)</span></div>", re.S)

result = obj.finditer(s)

for it in result:
    print(it.group("id"))
    print(it.group("name"))