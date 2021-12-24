#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Target  ：
@Author  ：jackyliu
@Date    ：2021/12/24 0:23 
'''
from typing import *
from AdjGraph import ArcNode,AdjGraph

class GraphAX:
    def __init__(self, vertx, mat): #vertx 顶点表；mat邻接矩阵
        self.vnum = len(vertx)  # 顶点数目
        self.vertx = vertx      # 顶点
        self.mat = mat #[mat[i][:] for i in range(vnum)]    # 邻接矩阵

def From_AdjacencyList_Create_GraphAx( graph:AdjGraph, nodes:list) -> GraphAX:
    mat = [[0] * graph.n for i in range(graph.n)]
    for i in range(graph.n):
        # 对行进行遍历
        for j in range(len(graph.adjlist[i])):
            # 对于出边节点进行遍历
            mat[i][graph.adjlist[i][j].adjvex] = graph.adjlist[i][j].weight
    temp = GraphAX( nodes, mat)
    return temp



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
    nodes = ['a','b','c','d','e']   # 节点映射名称
    # 通过邻接表创建图
    graph = AdjGraph()
    graph.CreateAdjGraph(input)
    # graph.DisAdjGraph()
    # 通过邻接表生成邻接矩阵
    From_AdjacencyList_Create_GraphAx(graph,nodes)

