"""
Author： 刘逸珑
Time：   2021/12/25 9:46
Reference:
    https://zhuanlan.zhihu.com/p/106271601
    https://blog.csdn.net/qq_42467563/article/details/86182266
    PPT-第七章图的最小路径
"""
import copy
import json
import os
import time
from functools import wraps

import psutil

INF = 0x3f3f3f
from typing import *


def Testit(func):
    """
    一个用于检测函数运行时间以及内存消耗的装饰器函数
    :param func: 需要监测运行时间以及内存的函数名称
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        r = func(*args, **kwargs)
        end = time.perf_counter()
        print('{}.{} : {}'.format(func.__module__, func.__name__, end - start))
        print(u'当前进程的内存使用：%.4f MB' % (psutil.Process(os.getpid()).memory_info().rss / 1024 / 1024))
        return r

    return wrapper


def finding_interchange_station(line_list: list) -> List[str]:
    """
    寻找换乘站，算法原理：如果一个站点出现在多个线路的列表中，则该站点为换乘站
    :param line_list:在开始时输入的，一个由[line1, line2, line3, lin4]组成的数组，其中各项包含line中的所有站点名称
    :return:一个由换乘站点名称组成的列表
    """
    total_site = []
    for line in line_list:
        total_site.extend(line)
    dict_count = Counter(total_site)
    interchange_station = []
    for k, v in dict_count.items():
        if v > 1:
            interchange_station.append(k)
    return interchange_station


class AdjMatrix:
    def __init__(self, save: list, model=0):
        self.vertx = save[0]  # 节点集合
        self.line_list = save[1]  # 保存各线的站点名称
        self.mat = copy.deepcopy(save[2])  # 节点邻接矩阵
        # bug 修复: 原因在于self.mat其实是被指向了与save的同一个内存地址，而非重新创建了一个内存地址，
        # 因而会更改形参save也就是输入的json_data中所指向的内存地址中的数据
        self.satNum = len(self.vertx)  # 站点总数
        self.dist = []  # 距离矩阵
        self.path = []  # 前驱结点矩阵
        self.outputDetail = "的最小路径长度为"  # 对于不同模式的输出信息调整
        self.model = model  # 模式名称
        self.interStation = finding_interchange_station(self.line_list)
        self.parameter_passing = []  # 注： 这个地方只是为了不影响到main程序的正常使用，并且也不想修改太多东西，因此偷懒了
        if self.model == 0:
            pass
        elif self.model == 1:
            self.outputDetail = "之间最小站点数为，"
            for i in range(len(self.mat)):
                # self.mat[i][i] = 0
                for j in range(len(self.mat[i])):
                    # 对于其中的每一个元素进行遍历，如果该元素存在
                    if self.mat[i][j] != 0 and self.mat[i][j] != INF:
                        self.mat[i][j] = 1
        elif self.model == 2:
            self.satNum = len(self.line_list)
            self.outputDetail = "之间最少的换乘次数为"
            # 创造一个全新的矩阵来对于这种特殊的情况进行承载
            self.mat = [[INF] * len(self.line_list) for i in range(len(self.line_list))]
            for i in range(len(self.mat)):
                self.mat[i][i] = 0
                for j in range(len(self.mat)):
                    for interStation in self.interStation:
                        if interStation in self.line_list[i] and interStation in self.line_list[j] and i != j:
                            self.mat[i][j] = 1

    @Testit
    def _floyd(self):
        """
        实现 floyd 算法
        :return:        dist_matrix, path_matrix
        """
        # 如果在同一行进行赋值，则会出现指针引用相同的情况
        dist_matrix = [[INF] * self.satNum for i in range(self.satNum)]
        path_matrix = [[INF] * self.satNum for i in range(self.satNum)]

        # initialization
        for i in range(self.satNum):
            for j in range(self.satNum):
                dist_matrix[i][j] = self.mat[i][j]
                if i != j and self.mat[i][j] < INF:
                    # 如果边存在
                    path_matrix[i][j] = i
                else:
                    path_matrix[i][j] = -1

        for k in range(self.satNum):  # 中间点的选择
            for i in range(self.satNum):
                for j in range(self.satNum):
                    if dist_matrix[i][j] > dist_matrix[i][k] + dist_matrix[k][j]:
                        # if i->k->j is lower than i->j:
                        dist_matrix[i][j] = dist_matrix[i][k] + dist_matrix[k][j]
                        path_matrix[i][j] = path_matrix[k][j]

        return dist_matrix, path_matrix

    def dis_path(self, start: int, end: int):
        """
        实现结果（最小路径 /站数)以及路径的呈现
        :param start:   the index of start station in self.vertx
        :param end:     the index of end station in self.vertx
        :return:
        """
        k = self.path[start][end]
        apath = [self.vertx[end]]
        while k != -1 and k != start:
            apath.append(self.vertx[k])
            k = self.path[start][k]
        apath.append(self.vertx[start])
        apath.reverse()
        # 这个部分通过一个类变量对于结果进行传递
        self.parameter_passing = [self.vertx[start], self.vertx[end], self.dist[start][end], apath]
        print("{} 与 {} 之间的{}为{}， 其路径为：{}".format(self.vertx[start], self.vertx[end], self.outputDetail,
                                                 self.dist[start][end], apath))

    def dis_path_min_interchange_station(self, start_station: str, end_station: str, start: int, end: int):
        """
        专门提供最小换乘站的路线输出【注：在此处输入的 start and end 代表 self.path 中的 start_index and end_index】
        :param start_station:   the name of start stations in vertx
        :param end_station:     the name of end   stations in vertx
        :param start:           输入的最优起始线路
        :param end:             输入的最优终止线路
        :return:                void
        """
        # 注意：在修改算法之后apath中保存的是经过的线路名称的index
        k = self.path[start][end]
        apath = []
        while k != -1 and k != start:
            # 这个地方的 k 代表的是经过的线路的index
            apath.append(k)
            k = self.path[start][k]
        apath.reverse()

        # 首先，获取线路中经过的线路名称
        way_line = []
        if start == end:
            way_line.append(start)
        elif apath :
            way_line.append(start)
            for i in apath:
                way_line.append(i)
            way_line.append(end)
        else:
            way_line.append(start)
            way_line.append(end)
        print("way_line:", way_line)

        for i in range(len(way_line)):
            way_line[i] += 1
        # 然后再获取每两个线路之间的换乘站点
        interchange_station = []
        # if len(way_line) == 1:
        #     pass
        # if len(way_line) > 1:
        #     for i in range(0,len(way_line)-1):
        #         for interstation in self.interStation:
        #             for line in self.line_list:
        #                 if interstation in


        self.parameter_passing = [start_station, end_station, self.dist[start][end], way_line]
        print("{}与{}之间的{}{}，其路径为{}".format(start_station, end_station,
                                           self.outputDetail, (self.dist[start][end]), way_line))

    def interface(self, start: str, end: str):
        """
        封装三种不同的程序执行方案
        :param start:   the name of start stations in vertx
        :param end:     the name of end   stations in vertx
        :return:
        """
        if self.dist == 0 or self.path == 0:
            # 如果还没有进行初始化
            self.dist, self.path = self._floyd()
        # 输出结果
        if self.model == 0 or self.model == 1:
            start, end = self.vertx.index(start), self.vertx.index(end)
            self.dis_path(start, end)

        elif self.model == 2:
            print("start")
            print(start, end)
            self.dist, self.path = self._floyd()
            # 获取起止点，终止点在线路在 line_list 中的 index
            start_list = []
            end_list = []
            # 考虑对应针对站点为换乘站的情况【有可能出现一个站对应多条站点的情况】
            for lineNum in range(len(self.line_list)):
                for station in self.line_list[lineNum]:
                    if station == start:
                        start_list.append(lineNum)
                        print(self.line_list[lineNum])
                    if station == end:
                        end_list.append(lineNum)
            # 这个部分的存在是为了解决一个站点对应多线路的情况
            # 【对于起止点列表中的结果进行遍历，并且求出其最优结果，将对应的index读取为i,j】
            i, j = start_list[0], end_list[0]
            for s in start_list:
                for e in end_list:
                    if self.dist[i][j] > self.dist[s][e] and s != e:
                        i, j = s, e
            print(i, j)
            self.dis_path_min_interchange_station(start, end, i, j)


if __name__ == '__main__':
    with open('original_data.json', 'r') as File:
        json_data = json.load(File)

    graph = AdjMatrix(json_data, 2)
    graph.interface("岗顶", "江南西")
