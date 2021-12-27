"""
Author： 刘逸珑
Time：   2021/12/25 11:21
Reference:

"""
import json
import GetData
from AdjGraph import AdjMatrix

# TODO 待解决问题： 如何在此函数判断输入特殊语句之后直接退出input输入模式，直接进行切换，这样就不需要input两次再输出结果
# def input_validity_check(str:str):
#     global graph
#     global flag
#     if str.upper == "CM":
#         model = int(input("请输入你想使用的模式名称：最短路径模式0，最少站点模式1，最少换乘模式2"))
#         del graph
#         graph = AdjMatrix(json_data[0], json_data[2], model)
#     if str.lower() == 'quit':
#         flag = False
#         print("欢迎下次使用本系统")
#     return



print("欢迎使用地铁路径自动规划系统！")
model = int(input("请输入你想使用的模式名称：最短路径模式0，最少站点模式1，最少换乘模式[如果输入换乘站会报错]2"))
# json_data = GetData.initialization()
GetData.initialization()
with open("original_data.json", 'r') as File:
    json_data = json.load(File)
graph = AdjMatrix(json_data[0], json_data[2], model)
flag = True

while flag:
    print("请依据提示输入对应的站点名称")
    print("help[将下列字符输入到任意站点位置即可]:更换模式[cm],退出系统[exit]")
    start = str(input("请输入起始站点"))
    end = str(input("请输入终止站点"))
    if start not in json_data[0] or end not in json_data[0]:
        if start.upper() == "CM" or end.upper() == "CM":
            model = int(input("请输入你想使用的模式名称：最短路径模式0，最少站点模式1，最少换乘模式2"))
            del graph
            graph = AdjMatrix(json_data[0], json_data[2], model)
        elif start.lower()  == "exit" or end.lower() == "exit":
            flag = False
        else:
            print("您输入的站点名称不存在！")
    else:
        graph.interface(start, end)
print("欢迎再次使用地铁路径自动规划系统!")

