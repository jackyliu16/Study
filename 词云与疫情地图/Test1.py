import csv




filename = 'D:\COVID-19-master\csse_covid_19_data\csse_covid_19_daily_reports_us\Jan/01-01-2021.csv'
with open(filename) as f:
    reader = csv.DictReader(f)
    Province_State = []

    #初始化一个新列表把所有的州放进去
    for row in reader:
        # Max TemperatureF是表第一行的某个数据，作为key
        Province = row['Province_State']
        Province_State.append(Province)
    print(Province_State)