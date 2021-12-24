#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Target  ：测试样例 1 采用书本中实现的G1(p235)
@Author  ：jackyliu
@Date    ：2021/12/23 16:09 
'''
INF = 0x3f3f3f


# 这个步骤通过人工手动从图片中获取信息，以生成邻接表
class ArcNode:
    def __init__(self, adjv, w):  # 采用类似于链表的形式生成
        self.adjvex = adjv  # 邻接点
        self.weight = w  # 边的权重


class AdjGraph:
    def __init__(self, n=0, e=0):
        self.adjlist = []  # 邻接表数组
        self.vexs = []  # vex[i]存放顶点i的边数
        # self.n = n  # 顶点数
        # self.e = e          # 边数

    def CreateAdjGraph(self, a):
        self.n = len(a)
        # 生成 self.vexs
        for i in range(len(a)):
            self.vexs.append(len(a[i]))
        # 生成对应链表
        for i in range(len(a)):
            # 节点的出边
            adi = []
            for j in a[i]:
                # 节点
                adi.append(ArcNode(j[0], j[1]))
            self.adjlist.append(adi)

    def DisAdjGraph(self):
        for i in range(self.n):
            # 对于节点的出边进行遍历
            print("[{0}]".format(i), end=" ")
            for j in range(len(self.adjlist[i])):
                print("->[{0},{1}]".format(self.adjlist[i][j].adjvex, self.adjlist[i][j].weight), end="")
            print("->Λ")


if __name__ == "__main__":
    input = [
        [[1, 1], [3, 1], [4, 1]],
        [[0, 1], [2, 1], [3, 1]],
        [[1, 1], [3, 1], [4, 1]],
        [[0, 1], [1, 1], [2, 1], [4, 1]],
        [[0, 1], [2, 1], [3, 1]]
    ]
    graph = AdjGraph()
    graph.CreateAdjGraph(input)
    graph.DisAdjGraph()
