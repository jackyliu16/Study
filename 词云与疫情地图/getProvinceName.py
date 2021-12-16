import csv




filename = r'C:\Users\刘逸珑\PycharmProjects\DataAnalyse\词云与疫情地图\Jan\01-02-2021.csv'
with open(filename) as f:
    reader = csv.DictReader(f)
    Province_State = []

    #初始化一个新列表把所有的州放进去
    for row in reader:
        # Max TemperatureF是表第一行的某个数据，作为key
        Province = row['Province_State']
        Province_State.append(Province)
    print(f'Province List: {Province_State}')