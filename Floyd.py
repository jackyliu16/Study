#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Target  ：
@Author  ：jackyliu
@Date    ：2021/12/24 0:23 
'''
from typing import *
from AdjGraph import ArcNode, AdjGraph

INF = 0x3f3f3f


class GraphAX:
    def __init__(self, vertx, mat):  # vertx 顶点表；mat邻接矩阵
        self.vnum = len(vertx)  # 顶点数目
        self.vertx = vertx  # 顶点
        self.mat = mat  # [mat[i][:] for i in range(vnum)]    # 邻接矩阵


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


def Floyd(graph: GraphAX):
    # 初始化二维数组【注： 此处不能在一行中进行赋值，否则会出现引用相同的情况】
    dist_Matix = [[0] * graph.vnum for i in range(graph.vnum)]
    path_Matix = [[0] * graph.vnum for i in range(graph.vnum)]
    for i in range(graph.vnum):
        for j in range(graph.vnum):
            dist_Matix[i][j] = graph.mat[i][j]
            if i != j and graph.mat[i][j] < INF:  # 如果存在该出边
                path_Matix[i][j] = i
            else:
                path_Matix[i][j] = 1

    for k in range(graph.vnum):  # 将第k个节点作为中间节点
        for i in range(graph.vnum):
            for j in range(graph.vnum):
                if dist_Matix[i][j] > dist_Matix[i][k] + dist_Matix[k][j]:
                    # 如果引入中间节点会降低 i 到 j 的距离
                    dist_Matix[i][j] = dist_Matix[i][k] + dist_Matix[k][j]
                    path_Matix[i][j] = path_Matix[k][j]
    DisPath(dist_Matix, path_Matix, graph)


def DisPath(dist_Matix: list, path_Matix: list, graph: GraphAX):
    for i in range(graph.vnum):
        for j in range(graph.vnum):
            if dist_Matix[i][j] != INF and i != j:
                # 如果存在路径
                print("  顶点%d到%d的最短路径长度: %d\t路径:" % (i, j, dist_Matix[i][j]), end='')
                k = path_Matix[i][j]
                apath = [j]
                while k != -1 and k != i:
                    apath.append(k)
                    k = path_Matix[i][k]
                apath.append(i)
                apath.reverse()
                print(apath)


if __name__ == "__main__":
    # nodes = ['v0', 'v1', 'v2', 'v3', 'v4']
    # matrix = [[0, 1, 0, 1, 0],
    #           [1, 0, 1, 0, 1],
    #           [0, 1, 0, 1, 1],
    #           [1, 0, 1, 0, 0],
    #           [0, 1, 1, 0, 0]]
    # graph = GraphAX(nodes,matrix)
    input = [
        [[1, 1], [3, 1], [4, 1]],
        [[0, 1], [2, 1], [3, 1]],
        [[1, 1], [3, 1], [4, 1]],
        [[0, 1], [1, 1], [2, 1], [4, 1]],
        [[0, 1], [2, 1], [3, 1]]
    ]
    nodes = ['a', 'b', 'c', 'd', 'e']  # 节点映射名称
    # 通过邻接表创建图
    graph = AdjGraph()
    graph.CreateAdjGraph(input)
    # graph.DisAdjGraph()
    # 通过邻接表生成邻接矩阵
    graph = From_AdjacencyList_Create_GraphAx(graph, nodes)
    print(graph.mat)
    Floyd(graph)
