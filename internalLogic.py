"""
@Target : 
@Annotation : 
@Author : JackyLiu
@Date   : 2022/5/31 10:49
@Reference  : 
    1.
    2.
@Source :
    
"""
import abc
import json
import math
from typing import List, Dict, Any

import requests

INF = 0x3f3f3f3f


def get_edge(city):
    """
    :param city: 城市编号
    :return: 城市序号，返回邻接表、总站数、站名-序号查询字典、序号反查字典、站点序号-线路字典、线路-序号反查字典
    此模块由摘自黄诺然(20202031017), 蒋一帆(20202031069)在21-秋(数据结构与算法-python大作业中)
    在对他们的代码的分析中，发现其内容基本吻合我的要求，并且封装的较为良好，因此选择直接使用他们的模块，而非重新写一个模块
    """
    if city == 0:
        url = "http://map.amap.com/service/subway?_1641228914035&srhdata=1100_drw_beijing.json"
    elif city == 1:
        url = "http://map.amap.com/service/subway?_1641228963002&srhdata=3100_drw_shanghai.json"
    elif city == 3:
        url = "http://map.amap.com/service/subway?_1641229064474&srhdata=4403_drw_shenzhen.json"
    elif city == 4:
        url = "http://map.amap.com/service/subway?_1641229077978&srhdata=4201_drw_wuhan.json"
    elif city == 5:
        url = "http://map.amap.com/service/subway?_1641229093554&srhdata=1200_drw_tianjin.json"
    elif city == 6:
        url = "http://map.amap.com/service/subway?_1641229119913&srhdata=3201_drw_nanjing.json"
    elif city == 7:
        url = "http://map.amap.com/service/subway?_1641229130505&srhdata=8100_drw_xianggang.json"
    elif city == 8:
        url = "http://map.amap.com/service/subway?_1641229144217&srhdata=5000_drw_chongqing.json"
    elif city == 9:
        url = "http://map.amap.com/service/subway?_1641229158953&srhdata=3301_drw_hangzhou.json"
    else:
        url = "http://map.amap.com/service/subway?_1641229051978&srhdata=4401_drw_guangzhou.json"

    response = requests.get(url)  # 以下为爬虫部分，爬取地铁站的站名、序号、经纬度、所属线路等信息
    result = json.loads(response.text)
    stations = {}
    stationame = {}
    statiouname = {}
    con = 0
    incon = []
    for i in result['l']:
        station = {}
        for a in i['st']:
            if a['n'] not in incon:
                station[con] = [float(b) for b in a['sl'].split(',')]  # 记录sl标签下的经纬度信息
                stationame[con] = a['n']
                statiouname[a['n']] = con
                incon.append(a['n'])
                con += 1
            else:
                shuttle = statiouname[a['n']]
                station[shuttle] = [float(b) for b in a['sl'].split(',')]
        stations[i['kn']] = station  # 记录kn标签下的线路信息

    stationline = {}  # 以下部分用于生成站名-序号查询字典、序号反查字典
    linecon = 0
    linecondict = {}
    for i, k in stations.items():
        stationstf = []
        for j in k.keys():
            stationstf.append(j)
            stationline[linecon] = stationstf
        linecondict[linecon] = i
        linecon += 1

    edge = [[INF] * con for i in range(con)]  # 以下部分生成站点间的邻接表、其中距离为权值
    for l in range(con):
        edge[l][l] = 0

    for lines in stations.values():
        staname = []
        for j in lines.keys():
            staname.append(j)
        staspace = []
        for k in lines.values():
            staspace.append(k)
        for i in range(len(lines) - 1):
            distance = math.sqrt((staspace[i][0] - staspace[i + 1][0]) ** 2 + (
                    staspace[i][1] - staspace[i + 1][1]) ** 2) * 111.1  # 使用直线距离近似表达两站间的距离
            edge[staname[i]][staname[i + 1]] = distance
            edge[staname[i + 1]][staname[i]] = distance

    return edge, con, stationame, statiouname, stationline, linecondict


class Method:
    @abc.abstractmethod
    def __init__(self, city_num: int):
        # self.edge, self.sat_num, self.station_name, self.station_con_name, self.station_line, self.line_con_dict = get_edge(city_num)
        self.edge: List[List[int]]                  # 邻接矩阵
        self.sat_num: int                           # 总站点数目
        self.station_name: Dict[int, Any]           # 站点编号：名称字典
        self.station_con_name: Dict[Any, int]       # 站点名称：编号字典
        self.station_line: Dict[int, List]          # 线路编号：线路字典
        self.line_con_dict: Dict[int, Any]          # 线路：线路编号字典

    @abc.abstractmethod
    def get_path(cls):
        pass

    @classmethod
    def _floyd(self):
        """
        实现 floyd 算法
        :return:        dist_matrix, path_matrix
        """
        # 如果在同一行进行赋值，则会出现指针引用相同的情况
        dist_matrix = [[INF] * self.sat_num for i in range(self.sat_num)]
        path_matrix = [[INF] * self.sat_num for i in range(self.sat_num)]

        # initialization
        for i in range(self.sat_num):
            for j in range(self.sat_num):
                dist_matrix[i][j] = self.edge[i][j]
                if i != j and self.edge[i][j] < INF:
                    # 如果边存在
                    path_matrix[i][j] = i
                else:
                    path_matrix[i][j] = -1

        for k in range(self.sat_num):  # 中间点的选择
            for i in range(self.sat_num):
                for j in range(self.sat_num):
                    if dist_matrix[i][j] > dist_matrix[i][k] + dist_matrix[k][j]:
                        # if i->k->j is lower than i->j:
                        dist_matrix[i][j] = dist_matrix[i][k] + dist_matrix[k][j]
                        path_matrix[i][j] = path_matrix[k][j]

        return dist_matrix, path_matrix


class ShortestPath(Method):
    """
    最短距离模块
    """
    def __init__(self, city_num: int):
        pass

    def get_path(cls):
        return "hello"


class MinimumSites(Method):
    """
    最小站点数目模块
    """
    def __init__(self, city_num: int):
        pass

    def get_path(cls):
        pass


class MinimumTransfer(Method):
    """
    最小换乘计算类
    """
    def __init__(self, city_num: int):
        pass

    def get_path(cls):
        pass


class Context:
    def __init__(self, strategy=ShortestPath):
        self.strategy: Method=strategy(1)
        # eval(f"self.strategy= new {strategy}()")

    def using_strategy(self):
        # TODO return model method of finding path
        return self.strategy.get_path()
