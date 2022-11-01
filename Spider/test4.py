import re

template = "我要听<歌手名>的<歌曲名>"


def subString(template):
    rule = r'<(.*?)>'  # 正则规则
    slotList = re.findall(rule, template)
    return slotList

slotList = subString(template)
for slot in slotList:
    print(slot)
