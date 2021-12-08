"""
Author： 刘逸珑
Time：   2021/12/8 22:03
"""
import json
import re
import requests
from lxml import etree      # 解析数据

class GetData():
    # 获取数据
    def getData(self):
        response = requests.get("https://voice.baidu.com/act/newpneumonia/newpneumonia")
        with open('html.txt', 'w') as file:
            file.write(response.text)

    # 提取更新时间
    def getTime(self):
        with open('html.txt', 'r') as file:
            text = file.read()
        time = re.findall('"mapLastUpdatedTime":"(.*?)"',text)[0]               # 这个地方使用了正则表达式
        return time

    # 解析数据
    def parseData(self):
        with open('html.txt', 'r') as file:
            text = file.read()
        html = etree.HTML(text)
        result = html.xpath('//script[@type="application/json"]/text()')
        # script 标签 中有个type属性=application/json 因为我们想要得到内容所以说要加/text()
        '''这个地方读取的是一个列表，我们需要将列表转化成为字符串，然后再转化成为字典'''
        result = result[0] # 列表只有一个元素
        result = json.loads(result)
        result = result['component'][0]['caseList']
        result = json.dumps(result)          # 可以将python的数据类型转化成为字符串？
        with open('../data.json', 'w') as file:
            file.write(result)
            # print('数据[粗提取]写入完成')



