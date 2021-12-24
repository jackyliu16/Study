#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Target  ：获取随机数，并且保存到邻接矩阵中
@Author  ：jackyliu
@Date    ：2021/12/25 1:16
Reference:
    https://blog.csdn.net/phpLara/article/details/82705907
'''

import random
import csv
import json

# 导入站点数据，该数据为直接从http://gz.bendibao.com/ditie/xl_215.shtml中复制下来
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
line1 = line1.split("\n")
line2 = line2.split("\n")
line3 = line3.split("\n")

total_site_list = line1.copy()
total_site_list.extend(line2)
total_site_list.extend(line3)
# 参考1
temp_set = list(set(total_site_list))
temp_set.sort(key=total_site_list.index)
total_site_list = temp_set
print(total_site_list)

