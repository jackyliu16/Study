"""
@Target :
@Annotation :
@Author : JackyLiu
@Date   : 2022/5/31 10:49
@Reference  :
    https://github.com/jackyliu16/Study.git     # 我自己的仓库中的Shortest啥的分支【这个是镜像仓库，原仓库在gitee上，但是没法开源】
    https://zhuanlan.zhihu.com/p/106271601
    https://blog.csdn.net/qq_42467563/article/details/86182266
    PPT-第七章图的最小路径
    https://mailscusteducn-my.sharepoint.com/:f:/g/personal/2015002346_mails_cust_edu_cn/EjmW-PrnghhMhowOLVNr9iEBUTS0Po9K6sCaf5DXs2M3kg?e=FWRfF4
        password: scnu group: B
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
    :param city: the number of city
    :return: 城市序号，返回邻接表、总站数、站名-序号查询字典、序号反查字典、站点序号-所属线路字典，线路：站点序号字典，线路-序号反查字典
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

    # ====== 两条线之间是我添加的部分 ======

    station_line = {}  # 注意：这个地方我并没有更正源代码中错误的stationline(个人认为应该为{line_station}描述，仅仅只是使用自己的写法添加了东西

    for line_num in stationline:
        for station_num in stationline[line_num]:
            if station_num in station_line.keys():
                station_line[station_num].append(line_num)
            else:
                station_line[station_num] = [line_num]

    # ====== 两条线之间是我添加的部分 ======

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

    return edge, con, stationame, statiouname, station_line, stationline, linecondict


class Method:
    @abc.abstractmethod
    def __init__(self, city_num: int):
        # self.edge, self.sat_num, self.station_name, self.station_con_name, self.station_line, self.line_con_dict = get_edge(city_num)
        self.edge: List[List[int]]  # 邻接矩阵
        self.sat_num: int  # 总站点数目
        self.station_name: Dict[int, Any]  # 站点编号：名称字典
        self.station_con_name: Dict[Any, int]  # 站点名称：编号字典
        self.station_line: Dict[int, List[int]]  # 站点编号：站点所属的线路
        self.line_station: Dict[int, List]  # 线路编号：线路字典
        self.line_name: Dict[int, Any]  # 线路：线路编号字典

    @abc.abstractmethod
    def get_path(cls, start_station: str, end_station: str) -> str:
        pass

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

    def find_where_we_need_to_transfer(self, apath:List[str])->List[str]:
        """
        give a apath return if need transfer
        :param apath:   运行路径
        :return:        换乘站点
        """
        transfer_station = []
        for i in range(len(apath)):
            station_num = self.station_con_name[apath[i]]
            if len(self.station_line[station_num]) > 1:
                # is transfer station
                if i - 1 >= 0 and i + 1 < len(apath):
                    # check if a, b, c is in same line
                    # TODO 连续换乘多站会出现bug
                    if self.station_line[self.station_con_name[apath[i-1]]] == self.station_line[self.station_con_name[apath[i+1]]]:
                        # you will not change your line in this transfer station
                        pass
                    else:
                        transfer_station.append(apath[i])
                else:
                    # is start station or end station
                    pass
        return transfer_station


class ShortestPath(Method):
    """
    最短距离模块
    """
    def __init__(self, city_num: int):
        self.edge, self.sat_num, self.station_name, self.station_con_name, self.station_line, self.line_station, self.line_name = get_edge(city_num)
        self.dist_matrix, self.path_matrix = self._floyd()

    def get_path(cls, start_station: str, end_station: str) -> str:
        """
        实现结果（最小路径 /站数)以及路径的呈现
        :param start_station:   the name of start station in self.vertx
        :param end_station:     the name of end station in self.vertx
        :return:
        """
        # from station name get index of station
        start_station, end_station = cls.station_con_name[start_station], cls.station_con_name[end_station]
        k = cls.path_matrix[start_station][end_station]
        apath = [cls.station_name[end_station]]

        while k != -1 and k != start_station:
            apath.append(cls.station_name[k])
            k = cls.path_matrix[start_station][k]
        apath.append(cls.station_name[start_station])
        apath.reverse()

        transfer = cls.find_where_we_need_to_transfer(apath)
        return "你可以通过{}到达目标点, {},距离为:{:.2f}KM".format(apath, "不需要换乘" if len(transfer) == 0 else "你需要在以下站点换乘" + str(transfer), cls.dist_matrix[start_station][end_station])


class MinimumSites(Method):
    """
    最小站点数目模块
    """
    def __init__(self, city_num: int):
        self.edge, self.sat_num, self.station_name, self.station_con_name, self.station_line, self.line_station, self.line_name = get_edge(city_num)

        self.edge = [[1 if self.edge[i][j] != INF else INF for i in range(self.sat_num)] for j in range(self.sat_num)]
        self.dist_matrix, self.path_matrix = self._floyd()

    def get_path(cls, start_station: str, end_station: str) -> str:
        start_station, end_station = cls.station_con_name[start_station], cls.station_con_name[end_station]

        k = cls.path_matrix[start_station][end_station]
        apath = [cls.station_name[end_station]]

        while k != -1 and k != start_station:
            apath.append(cls.station_name[k])
            k = cls.path_matrix[start_station][k]
        apath.append(cls.station_name[start_station])
        apath.reverse()

        transfer = cls.find_where_we_need_to_transfer(apath)
        return "你可以通过{}到达目标点,{},通过的站点数目为:{}".format(apath, "不需要换乘" if len(transfer) == 0 else "你需要在以下站点换乘" + str(transfer), cls.dist_matrix[start_station][end_station])


class MinimumTransfer(Method):
    """
    最小换乘计算类
    """
    def __init__(self, city_num: int):
        self.edge, self.sat_num, self.station_name, self.station_con_name, self.station_line, self.line_station, self.line_name = get_edge(city_num)
        self.sat_num = len(self.line_name)
        self.edge = [[INF if i != j else 0 for i in range(self.sat_num)] for j in range(self.sat_num)]  # setting as INF
        self.transfer_station:List[List[int, int], List[int]] = []  # unhashable type: 'list'
        # find which line and which line have connection
        for key, value in self.station_line.items():
            if len(value) > 1 :
                for i in range(len(value)):
                    value[i], value[0] = value[0], value[i]
                    for j in range(1, len(value)):
                        if self.edge[value[0]][value[j]] == INF:
                            self.edge[value[0]][value[j]] = 1
                        else:
                            self.edge[value[0]][value[j]] += 1
                        # add station to line-line -- station_num list
                        Flag = False
                        for item in self.transfer_station:
                            if item[0] == [value[0], value[j]]:
                                Flag = True
                                item[1].append(key)
                                break
                        # if not found
                        if not Flag :
                            self.transfer_station.append([[value[0], value[j]], [key]])


        # # For debug
        # for row in self.edge:
        #     for col in row:
        #         print(col if col != INF else "INF" , end="\t")
        #     print()

        # 这个地方更倾向于采用通过(如果两条线路之间存在换乘站点，则这两条线路之间的距离为1) 的方案，但是在做结果输出的时候，存在一定的问题

        self.dist_matrix, self.path_matrix = self._floyd()

    def get_path(cls, start_station: str, end_station: str) -> str:
        # TODO Finish get_path
        start_line, end_line = cls.station_line[cls.station_con_name[start_station]], cls.station_line[cls.station_con_name[end_station]]

        apath = [None for _ in range(cls.sat_num)]
        end_flag = False
        for i in range(len(start_line)):
            for j in range(len(end_line)):
                tmp_apath = apath

                # if not end_flag:
                k = cls.path_matrix[start_line[i]][end_line[j]]
                tmp_apath = [[end_line[j]]]

                while k != -1 and k != start_line:
                    tmp_apath.append([k])
                    k = cls.path_matrix[start_line[i]][k]
                tmp_apath.append([start_line[i]])
                tmp_apath.reverse()

                # label:
                if len(tmp_apath) < len(apath):
                    apath = tmp_apath

        apath = [item[0] for item in apath]

        # remove same line
        delete_list = []
        for i in range(0, len(apath)-1):
            if apath[i] == apath[i+1]:
                delete_list.append(apath[i]) # 避免删除元素对于后面索引的影响
        for i in delete_list:
            apath.remove(i)


        transfer_list = []
        for i in range(len(apath)-1):
            for item in cls.transfer_station:
                if [apath[i], apath[i+1]] == item[0]:
                    transfer_list.append(cls.station_name[item[1][0]])
                # TODO 这个地方可能存在两个换乘战的情况
        line = [cls.line_name[apath[i]] for i in range(len(apath))]
        return f"{'您不需要换乘' if len(transfer_list) == 0 else f'您可以通过{line}的轨迹到达目的地, 其中您需要于{transfer_list}进行换乘'}"


class Context:
    def __init__(self, strategy=ShortestPath):
        city_num = -1                           # 默认使用广州
        self.warehouse = [ShortestPath(city_num), MinimumSites(city_num), MinimumTransfer(city_num) ]
        self.strategy = self.warehouse[0]       # 默认使用最短路径模式

    def using_strategy(self, start_station: str, end_station: str) -> str:
        return self.strategy.get_path(start_station, end_station)

    def change_model(self, model: int=0):
        self.strategy = self.warehouse[model]

    def get_model_name(self):
        return "最短距离模式" if isinstance(self.strategy, ShortestPath) else "最少站点模式" \
            if isinstance(self.strategy, MinimumSites) else "最少换乘模式"
