import csv
import json
import getProvinceName
from pathlib import Path

Confirmed_List = []
for i in range(1, len(getProvinceName.Province_State)):
    Confirmed_List.append(0)


#打印出所有要批处理的文件
p = Path(r"G:\Tencent\WeChat\WeChat Files\wxid_32w2cfdzdtb222\FileStorage\File\2021-12\all")
FileList = list(p.glob("*.csv"))
# print(FileList)


total_data = []

for num in range(1, len(FileList)+1):
    Confirmed_List1 = []
    with open(f"{p}\\{num}.csv") as f:                      # 这个存在的目的是为了解决不能按照默认文件顺序打开的问题
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

    month_dict = {'time': num}
    Province_Confirmed = []
    for i in range(0,len(getProvinceName.Province_State)-1):
        Province_Confirmed1 = {}
        Province_Confirmed1['Province'] = getProvinceName.Province_State[i]
        Province_Confirmed1['Confirmed'] = Confirmed_List1[i]
        Province_Confirmed.append(Province_Confirmed1)
    month_dict["Data"] = Province_Confirmed
    total_data.append(month_dict)

with open('data.json','w') as File:
    File.write(json.dumps(total_data))