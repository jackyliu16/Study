"""
Author： 刘逸珑
Time：   2021/12/8 20:24
"""
import re
import json
import requests
from lxml import etree
import openpyxl

URL = "https://voice.baidu.com/act/newpneumonia/newpneumonia"
response = requests.get(URL)

html = etree.HTML(response.text)
result = html.xpath('//script[@type="application/json"]/text()')
result = result[0]
# 通过 json。loads() 将字符串转化成为 json 数据类型
result = json.loads(result)
# print(result)
# 创建工作表
wb = openpyxl.Workbook()
# 创建工作簿
ws = wb.active
ws.title = "国内疫情"
ws.append(['省份','累计确诊','死亡','治愈','现有确诊','累计确诊增量','死亡增量','治愈增量','现有确诊增量'])
resultIn = result['component'][0]['caseList']
resultOut= result['component'][0]['globalList']
# 可以通过对于列表的遍历，来得到结果
for each in resultIn:
    tempList = [each['area'],each['confirmed'],each['died'],each['crued'],each['curConfirm'],each['confirmedRelative']
              ,each['curConfirm'],each['diedRelative'],each['curedRelative'],each['curConfirmRelative']]
    for i in range(len(tempList)):
        if tempList[i] == "" :
            tempList[i] = "0"
    ws.append(tempList)
for each in resultOut:
    sheet_title = each['area']
    # 创建新的工作表
    ws_out = wb.create_sheet(sheet_title)
    ws_out.append(['国家','累计确诊','死亡','治愈','现有确诊','累计确诊增量'])
    for country in each['subList']:
        tempList = [country['country'],country['confirmed'],country['died'],country['crued'],country['curConfirm'],country['confirmedRelative']]
        if i in range(len(tempList)):
            if tempList[i] == "":
                tempList[i] = "0"
        ws_out.append(tempList)

wb.save("./data.xlsx")