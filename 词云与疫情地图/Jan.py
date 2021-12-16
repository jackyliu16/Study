import csv
import Test1
import pandas as pd
import os
import glob
from pathlib import Path

Confirmed_List = []
for i in range(1, len(Test1.Province_State)):
    Confirmed_List.append(0)


#打印出所有要批处理的文件
p = Path(r"D:\COVID-19-master\csse_covid_19_data\csse_covid_19_daily_reports_us\all")
FileList = list(p.glob("*.csv"))
print(FileList)


total_data = []

for File in FileList:
    Confirmed_List1 = []
    with open(File) as f:
        reader = csv.DictReader(f)
        # 初始化一个新列表把所有的确诊人数放进去
        for row in reader:
            Confirmed = row['Confirmed']
            Confirmed_List1.append(Confirmed)
    Confirmed_Num = [];
    for n in Confirmed_List1:
        Confirmed_Num.append(int(n));
        Confirmed_List1 = Confirmed_Num


        #创建一个字典

    month_dict = {}
    Province_Confirmed = []
    for i in range(0,len(Test1.Province_State)-1):
        Province_Confirmed1 = {}
        Province_Confirmed1['Province'] = Test1.Province_State[i]
        Province_Confirmed1['Confirmed'] = Confirmed_List1[i]
        Province_Confirmed.append(Province_Confirmed1)