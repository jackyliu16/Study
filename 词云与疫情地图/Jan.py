import csv
import getProvinceName
import pandas as pd
import os
import glob
from pathlib import Path
import json

ConfirmedForMonth = []
for i in range(1, len(getProvinceName.Province_State)):
    ConfirmedForMonth.append(0)
print(f"Confirmed_List: {ConfirmedForMonth}")

#打印出所有要批处理的文件
p = Path(r"C:\Programma\Python\Study\词云与疫情地图\Jan")       # 注： 在考虑转换成为相对路径的时候出现不知名错误
FileList = list(p.glob("*.csv"))        # 用作保存所有需要阅读的list


for File in FileList:
    confirmedForDay = []
    with open(File) as f:
        reader = csv.DictReader(f)      #csv.DictReader()返回一个csv.DictReader对象，可以将读取的信息映射为字典，其关键字由可选参数fieldnames来指定
        # 初始化一个新列表把所有的确诊人数放进去
        for row in reader:
            Confirmed = row['Confirmed']        # 这个部分似乎可以更加优化，通过csv。DictReader所能实现的功能进行优化
            confirmedForDay.append(Confirmed)   # 具体操作方式应该类似于 row['Province_State'] : row['Confirmed']
        # 把列表内的字符串全部转化成数字                                      但是基于我们操作精度而言这样的方案并不是最优的

        # 对于函数中的 每一个元素调用 function 方法，再将返回的map object转化成为list对象
        confirmedForDay = list(map( int, confirmedForDay))
        for i in range(0, len(ConfirmedForMonth)):
            ConfirmedForMonth[i] = ConfirmedForMonth[i] + confirmedForDay[i]


#创建一个字典
Province_Confirmed = []
for i in range(0,len(getProvinceName.Province_State)-1):
    confirmedForProvince = {'Province': getProvinceName.Province_State[i], 'Confirmed': ConfirmedForMonth[i]}
    Province_Confirmed.append(confirmedForProvince)

print("#" * 75 + " the output of a mouth " + "#" * 75 )
print(Province_Confirmed)

# 将汇总的一个月份的数据放到json文件中等待后续使用
savefile = str(p).split('/')[-1] + '.json'
with open(savefile,'w') as File:                        # 这个地方可以通过改成dump来提高效率，但是我懒得操作了
    File.write(json.dumps(Province_Confirmed))







