#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Target  ：
@Author  ：jackyliu
@Date    ：2021/12/24 0:23
Reference:
    https://zhuanlan.zhihu.com/p/106271601
    PPT-第七章图的最小路径
'''
from typing import *
from AdjGraph import ArcNode, AdjGraph

INF = 0x3f3f3f


class GraphAX:
    def __init__(self, vertx:list, mat:list):  # vertx 顶点表；mat邻接矩阵
        self.vnum = len(vertx)  # 顶点数目
        self.vertx = vertx  # 顶点
        self.mat = mat  # [mat[i][:] for i in range(vnum)]    # 邻接矩阵
        if len(self.vertx) != len(self.mat):
            print("站点数出错")


def From_AdjacencyList_Create_GraphAx(graph: AdjGraph, nodes: list) -> GraphAX:
    mat = [[INF] * graph.n for i in range(graph.n)]
    for i in range(graph.n):
        # 对行进行遍历
        mat[i][i] = 0
        for j in range(len(graph.adjlist[i])):
            # 对于出边节点进行遍历
            mat[i][graph.adjlist[i][j].adjvex] = graph.adjlist[i][j].weight
    temp = GraphAX(nodes, mat)
    return temp


def Floyd(graph: GraphAX) -> list:
    # 初始化二维数组【注： 此处不能在一行中进行赋值，否则会出现引用相同的情况】
    dist_matrix = [[0] * graph.vnum for i in range(graph.vnum)]
    path_matrix = [[0] * graph.vnum for i in range(graph.vnum)]
    for i in range(graph.vnum):
        for j in range(graph.vnum):
            dist_matrix[i][j] = graph.mat[i][j]
            if i != j and graph.mat[i][j] < INF:  # 如果存在该出边
                path_matrix[i][j] = i
            else:
                path_matrix[i][j] = 1

    for k in range(graph.vnum):  # 将第k个节点作为中间节点
        for i in range(graph.vnum):
            for j in range(graph.vnum):
                if dist_matrix[i][j] > dist_matrix[i][k] + dist_matrix[k][j]:
                    # 如果引入中间节点会降低 i 到 j 的距离
                    dist_matrix[i][j] = dist_matrix[i][k] + dist_matrix[k][j]
                    path_matrix[i][j] = path_matrix[k][j]
    # return [dist_matrix, path_matrix]
    DisAllPath(dist_matrix, path_matrix, graph)


def DisAllPath(dist_Matrix: list, path_Matrix: list, graph: GraphAX):
    for i in range(graph.vnum):
        for j in range(graph.vnum):
            if dist_Matrix[i][j] != INF and i != j:
                # 如果存在路径
                print("  顶点%d到%d的最短路径长度: %d\t路径:" % (i, j, dist_Matrix[i][j]), end='')
                k = path_Matrix[i][j]
                apath = [j]
                while k != -1 and k != i:
                    apath.append(k)
                    k = path_Matrix[i][k]
                apath.append(i)
                apath.reverse()
                print(apath)

# def getDistAndPath(start:int, end:int) -> list:
#     k = path_Matrix[start][end]
#     apath = [end]
#     while k != -1 and k != start:
#         apath.append(start)
#         apath.reverse()
#     print("节点{0}与节点{1}之间的最短路径长度为: {2}, 其最短路径为：{3}".format(nodes[start], nodes[end], dist_Matrix[start][end], apath))


if __name__ == "__main__":
    INPUT = [
        [[1, 1], [3, 1], [4, 1]],
        [[0, 1], [2, 1], [3, 1]],
        [[1, 1], [3, 1], [4, 1]],
        [[0, 1], [1, 1], [2, 1], [4, 1]],
        [[0, 1], [2, 1], [3, 1]]
    ]
    nodes = ['a', 'b', 'c', 'd', 'e']  # 节点映射名称
    # 通过邻接表创建图
    graph = AdjGraph()
    graph.CreateAdjGraph(INPUT)
    # graph.DisAdjGraph()
    # 通过邻接表生成邻接矩阵
    ''' 测试用例 
    _ = INF
    graph = [[0, 2, _, 4, 7, _],
             [_, 0, 2, _, 5, _],
             [_, _, 0, _, _, 3],
             [_, _, _, 0, 4, _],
             [_, _, 3, _, 0, 1],
             [_, _, _, _, _, 0],
             ]'''
    graph = From_AdjacencyList_Create_GraphAx(graph, nodes)
    # graph = GraphAX(nodes, graph)
    print(graph.mat)
    dist_Matrix, path_Matrix = Floyd(graph)

    # ''' 输入模块 '''
    # start = input("请输入起点：")
    # end = input("请输入终点：")
    # model = input("请输入选用模式名称(默认距离优先)：")
    #
    #
    # # 开始进行节点展示
    # getDistAndPath(start,end)


