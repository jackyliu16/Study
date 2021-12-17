"""
Author： 刘逸珑
Time：   2021/12/8 22:22
Reference:
        https://www.bilibili.com/video/BV1X54y1R7cu?from=search&seid=17433072440613079399&spm_id_from=333.337.0.0
"""
import json
import MapDraw
import dataGet


Map = MapDraw.Draw_map()
Data = dataGet.GetData()
Data.getData()
updateTime = Data.getTime()
Data.parseData()
with open('../data.json', 'r') as file:
    data = file.read()
    data = json.loads(data)
# 将地区与数据相对应
def china_map():
    area = []
    confirmed = []
    for each in data:
        # print(each)
        # print("*"*50)
        area.append(each['area'])
        confirmed.append(each['confirmed'])
    Map.tp_map_china(area, confirmed, updateTime)

        # print(area)
        # print(confirmed)

def province_map():
    for each in data:
        city = []
        confirmeds = []
        province = each['area']
        for eachCity in each['subList']:
            city.append(eachCity['city'])
            confirmeds.append(eachCity['confirmed'])
        # print(city)
        # print(confirmeds)

china_map()