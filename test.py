"""
Author： 刘逸珑
Time：   2021/12/14 0:49
"""
import json
# test_dict = {'one':1, 'two':{2.1:['a', 'b']}}
# print(test_dict)
# print(type(test_dict))

# with open('temp.json', 'w') as f:
#     f.write(json.dumps(test_dict))
#
# with open('temp.json', 'r') as f:
#     temp = f.read()
#     new_dict = json.loads(temp)
#     print(new_dict)
#     print(type(new_dict))



a = ['Alabama', 'Alaska', 'American Samoa', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Diamond Princess', 'District of Columbia', 'Florida', 'Georgia', 'Grand Princess', 'Guam', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Northern Mariana Islands', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Puerto Rico', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virgin Islands', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin']
b = [160716001, 19018419, 0, 265146251, 104154382, 1182316954, 138787549, 89606902, 27625893, 16611, 12999463, 610099857, 321746466, 34917, 2598640, 9261847, 56370464, 390290628, 217430557, 110789562, 96943463, 129317239, 140069384, 14075745, 123938674, 185611151, 211930352, 159602367, 95914971, 185065835, 32722669, 66113894, 96542159, 23654295, 248863380, 60530519, 511750304, 272692668, 33370253, 46055, 314010419, 137712944, 50284443, 301082492, 32697207, 40549740, 161095289, 37231339, 253446850, 851601167, 120953884, 4525139, 848433, 181754533, 109868381, 42495622, 0]
data = zip(a,b)


data = sorted(data,key=(lambda x:x[1]), reverse=True)
print(data)

