"""
Author： 刘逸珑
Time：   2021/12/25 9:46
Reference:
    https://zhuanlan.zhihu.com/p/106271601
    PPT-第七章图的最小路径
"""
import json

INF = 0x3f3f3f


class AdjMatrix:
    def __init__(self, vertx: list, mat: list, model=0):
        self.vertx = vertx
        self.mat = mat
        self.satNum = len(vertx)
        self.dist = 0
        self.path = 0
        self.outputDetail = "的最小路径长度为"
        if model != 0:
            self.outputDetail = "的最短站点数为"
            for i in range(len(self.mat)):
                for j in range(len(self.mat[i])):
                    if self.mat[i][j] != INF and self.mat[i][j] != 0:
                        self.mat[i][j] = 1



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

    def floyd(self, start: int, end: int):
        '''
        封装floyd算法的实现
        :param start:   the index of start stations in vertx
        :param end:     the index of end   stations in vertx
        :return:
        '''
        if self.dist == 0 or self.path == 0:
            # 如果还没有进行初始化
            self.dist, self.path = self._floyd()
        # 输出结果
        k = self.path[start][end]
        apath = [self.vertx[end]]
        while k != -1 and k != start:
            apath.append(self.vertx[k])
            k = self.path[start][k]
        apath.append(self.vertx[start])
        apath.reverse()
        print("{} 与 {} 之间的{}为{}， 其最短路径为：{}".format(self.vertx[start], self.vertx[end], self.outputDetail, self.dist[start][end], apath))


if __name__ == '__main__':
    with open('original_data.json', 'r') as File:
        json_data = json.load(File)

    graph = AdjMatrix(json_data[0], json_data[2],1)
    graph.floyd(31,4)
