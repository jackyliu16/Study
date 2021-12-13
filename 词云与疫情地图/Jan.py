import csv
import Test1
import pandas as pd
import os
import glob
from pathlib import Path

Confirmed_List = []
for i in range(1, len(Test1.Province_State)):
    Confirmed_List.append(0)
print(Confirmed_List)

#打印出所有要批处理的文件
p = Path("D:\COVID-19-master\csse_covid_19_data\csse_covid_19_daily_reports_us\Jan")
FileList = list(p.glob("*.csv"))


for File in FileList:
    Confirmed_List1 = []
    with open(File) as f:
        reader = csv.DictReader(f)
        # 初始化一个新列表把所有的确诊人数放进去
        for row in reader:
            Confirmed = row['Confirmed']
            Confirmed_List1.append(Confirmed)
        # 把列表内的字符串全部转化成数字
        Confirmed_Num = [];
        for n in Confirmed_List1:
            Confirmed_Num.append(int(n));
        Confirmed_List1 = Confirmed_Num
        for i in range(0,len(Confirmed_List)-1):
            Confirmed_List[i] = Confirmed_List[i] + Confirmed_List1[i]


        #创建一个字典
        Province_Confirmed = []
        for i in range(0,len(Test1.Province_State)-1):
            Province_Confirmed1 = {}
            Province_Confirmed1['Province'] = Test1.Province_State[i]
            Province_Confirmed1['Confirmed'] = Confirmed_List[i]
            Province_Confirmed.append(Province_Confirmed1)
print(Province_Confirmed)







