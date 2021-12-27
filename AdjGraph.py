"""
Author： 刘逸珑
Time：   2021/12/25 9:46
Reference:
    https://zhuanlan.zhihu.com/p/106271601
    PPT-第七章图的最小路径
"""
import json
from functools import wraps
import time
import psutil
import os

import GetData

INF = 0x3f3f3f
from typing import *

def Testit(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        r = func(*args, **kwargs)
        end = time.perf_counter()
        print('{}.{} : {}'.format(func.__module__, func.__name__, end - start))
        print(u'当前进程的内存使用：%.4f MB' % (psutil.Process(os.getpid()).memory_info().rss / 1024 / 1024))
        return r
    return wrapper

def finding_interchange_station(line_list: list) -> list:
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
    def __init__(self, save:list, model=0):
        self.vertx = save[0]    # 节点集合
        self.line_list = save[1]# 保存各线的站点名称
        self.mat = save[2]      # 节点邻接矩阵
        self.satNum = len(self.vertx)   # 站点总数
        self.dist = 0           # 距离矩阵
        self.path = 0           # 前驱结点矩阵
        self.outputDetail = "的最小路径长度为"
        self.model = model
        self.interStation = finding_interchange_station(self.line_list)
        if model == 1:
            self.outputDetail = "之间最小站点数为，"
            print(self.satNum)
            for i in range(len(self.mat)):
                self.mat[i][i] = 0
                for j in range(len(self.mat[i])):
                    # 对于其中的每一个元素进行遍历，如果该元素存在
                    if self.mat[i][j] != 0 and self.mat[i][j] != INF:
                        self.mat[i][j] = 1
        if model == 2:
            self.satNum = len(self.line_list)
            self.outputDetail = "之间最少的换乘次数为,"
            # 创造一个全新的矩阵来对于这种特殊的情况进行承载
            self.mat = [[INF] * len(self.line_list) for i in range(len(self.line_list))]
            for i in range(len(self.mat)):
                self.mat[i][i] = 0
                for j in range(len(self.mat)):
                    for interStation in self.interStation:
                        if interStation in self.line_list[i] and interStation in self.line_list[j] and i != j :
                            self.mat[i][j] = 1



    @Testit
    def _floyd(self):
        '''
        实现 floyd 算法
        :return:        dist_matrix, path_matrix
        '''
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

    # def _minTransfer(self, start:int, end:int):
    #     '''
    #     算法设计思路，如果二者都存在于同一条线路中，则直接输出结果
    #     如果二者在不同线路中，尝试通过双指针的方式对于当前线路进行遍历，
    #     并且对于逐个遍历到的元素采用入栈操作，
    #     在遍历完成整个列表之后，再对于输入的元素进行逐一出站，重复刚才进行的操作
    #     :param start: the index of start station in total station
    #     :param end:     the index of end station in total station
    #     :return:
    #     '''
    #
    #     self.__minTransfer(start,end,0,0)
    #
    #
    # def __minTransfer(self, start: int, end: int, dist:int,interTimes:int):
    #     '''
    #     实现自动双指针遍历与自动出栈判定行为
    #     :param start:
    #     :param end:
    #     :param interStation: 换乘站List[str]
    #     :param start_line and end_line: 开始与结束节点所位于的线路名称
    #     :return:
    #     '''
    #     # TODO 在进行遍历的时候带距离会存在指针边界冲突问题,同时进行递归的时候也会出现不知名问题
    #     # 获取start,end station 所在的线路号【此处是从0开始计算的】
    #     start_line = end_line = -1
    #     for line_num in range(len(self.line_list)):
    #         if self.vertx[start] in self.line_list[line_num]:
    #             start_line = line_num
    #         if self.vertx[end] in self.line_list[line_num]:
    #             end_line = line_num
    #
    #     if start_line == end_line:
    #         # 发现end节点在本线路中
    #         print(f"最少换乘次数为{interTimes}")
    #     else:
    #         # 否则对于该线路由开始节点向两端进行遍历【此处由于start和end都是指一个特异性的站点index，因此需要将其转化成为在此节点中的特异编号】
    #         start_index_in_line = self.line_list[start_line].index(self.vertx[start])
    #         for i in range(0,start_index_in_line):
    #             if self.line_list[start_line][i] in self.interStation:
    #                 # 如果该站点为换乘站且没有在栈中，则进行入栈【保留当前距离】,如果不是，则pass
    #                 if self.line_list[start_line][i] not in self.stack:
    #                     save = [self.line_list[start_line][i],dist]
    #                     self.stack.append(save)
    #         dist = dist     # 重新给dist进行赋值
    #         for i in range(start_index_in_line+1,len(self.line_list[start_line])):
    #             if self.line_list[start_line][i] in self.interStation:
    #                 # 如果该站点为换乘站，则进行入栈【保留当前距离】,如果不是，则pass
    #                 save = [self.line_list[start_line][i], dist]
    #                 self.stack.append(save)
    #
    #     temp = interTimes + 1  # 这个地方其实是想用interTimes++的
    #     self.__minTransfer(self.vertx.index(self.stack.pop()[0]), end, dist, temp)


    def interface(self, start, end):
        '''
        封装三种不同的程序执行方案
        :param start:   the name of start stations in vertx
        :param end:     the name of end   stations in vertx
        :return:
        '''

        if self.dist == 0 or self.path == 0:
            # 如果还没有进行初始化
            self.dist, self.path = self._floyd()
        # 输出结果
        if self.model == 0 or self.model == 1:
            start, end = self.vertx.index(start), self.vertx.index(end)
            k = self.path[start][end]
            apath = [self.vertx[end]]
            while k != -1 and k != start:
                apath.append(self.vertx[k])
                k = self.path[start][k]
            apath.append(self.vertx[start])
            apath.reverse()
            print("{} 与 {} 之间的{}为{}， 其路径为：{}".format(self.vertx[start], self.vertx[end], self.outputDetail, self.dist[start][end], apath))
        elif self.model == 2:
            # 获取起止点的index
            start_list = []
            end_list = []
            for lineNum in range(len(self.line_list)):
                for station in self.line_list[lineNum]:
                    if station == start:
                        start_list.append(lineNum)
                    if station == end:
                        end_list.append(lineNum)

            min_choice = [start_list[0],end_list[0]]
            for i in start_list:
                for j in end_list:
                    min_choice = i,j if self.dist[i][j] < self.dist[min_choice[0]][min_choice[1]] else min_choice[0],min_choice[1]
            i,j = min_choice[0],min_choice[1]
            k = self.path[i][j]
            apath = [self.vertx[j]]
            # TODO 这个地方没有适配结果
            while k != -1 and k != i:
                apath.append(self.vertx[k])
                k = self.path[i][k]
            apath.append(self.vertx[i])
            apath.reverse()
            print("{} 与 {} 之间的{}为{}， 其路径为：{}".format(start, end, self.outputDetail,
                                                     self.dist[i][j], apath))


if __name__ == '__main__':
    with open('original_data.json', 'r') as File:
        json_data = json.load(File)

    graph = AdjMatrix(json_data,2)
    graph.interface("芳村", "岗顶")