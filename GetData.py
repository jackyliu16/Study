#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Target  ：按照线路图生成邻接矩阵并且保存到json中方便进一步调用
@Author  ：jackyliu
@Date    ：2021/12/25 1:16
@annotation：由于使用random函数来设置各站点之间距离，因此尽可能不要重复运行本文件！！！
            否则有可能出现最优结果不一致的情况
@Reference:
    1. https://blog.csdn.net/phpLara/article/details/82705907
    2. https://blog.csdn.net/qq_42467563/article/details/86182266
@data source:
    1. http://gz.bendibao.com/ditie/xl_215.shtml
    2. https://gzmtr.com/
'''

import random
from collections import Counter
import csv
import json
INF = 0x3f3f3f


def making_connection_in_line(line:list):
    global Adjacent_matrix
    global total_site_list
    for station_index in range(0,len(line)-1):
        # 不能使之等于倒数第二个元素
        rand = int(random.random()*100 + 1)
        Adjacent_matrix[total_site_list.index(line[station_index])][total_site_list.index(line[station_index+1])] = rand
        Adjacent_matrix[total_site_list.index(line[station_index+1])][total_site_list.index(line[station_index])] = rand


def finding_interchange_station(total_site : list) -> list:
    dict_count = Counter(total_site)
    interchange_station = []
    for k,v in dict_count.items():
        if v > 1:
            interchange_station.append(k)
    return interchange_station

# source 1
line1 = """广州东站
体育中心
体育西路
杨箕
东山口
烈士陵园
农讲所
公园前
西门口
陈家祠
长寿路
黄沙
芳村
花地湾
坑口
西朗"""
line2 = """广州南站
石壁
会江
南浦
洛溪
南洲
东晓南
江泰路
昌岗
江南西
市二宫
海珠广场
公园前
纪念堂
越秀公园
广州火车站
三元里
飞翔公园
白云公园
白云文化广场
萧岗
江夏
黄边
嘉禾望岗"""
line3 = """天河客运站
五山
华师
岗顶
石牌桥
体育西路
珠江新城
广州塔
客村
大塘
沥滘
厦滘
大石
汉溪长隆
市桥
番禺广场"""
line4 = """机场北
机场南
高增
人和
龙归
嘉禾望岗
白云大道北
永泰
同和
京溪南方医院
梅花园
燕塘
广州东站
林和西"""
line1 = line1.split("\n")
line2 = line2.split("\n")
line3 = line3.split("\n")
line4 = line4.split("\n")

line_list = [line1,line2,line3,line4]
total_site = line1.copy()
total_site.extend(line2)
total_site.extend(line3)
total_site.extend(line4)
# 参考1 去除站点列表中的重复元素
total_site_list = list(set(total_site))
total_site_list.sort(key=total_site.index)

# initialization
Adjacent_matrix = [[INF] * len(total_site_list) for i in range(len(total_site_list))]

# initialization the distance of station : make sure the distance from a station to a station is 0
for i in range(len(Adjacent_matrix)):
    Adjacent_matrix[i][i] = 0

# making connection between line
for line in [line1,line2,line3,line4]:
    making_connection_in_line(line)


# making connection interchange station
# interchange_station = finding_interchange_station(total_site)
# 由于换乘站在两条线中都被考虑了，因此不应该单独为换乘站制作一个连接操作

save = [total_site_list, line_list, Adjacent_matrix]
with open("original_data.json",'w') as File:
    json.dump(save,File)
