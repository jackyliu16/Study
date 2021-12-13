"""
Author： 刘逸珑
Time：   2021/12/14 0:49
"""
import json
test_dict = {'one':1, 'two':{2.1:['a', 'b']}}
print(test_dict)
print(type(test_dict))

with open('temp.json', 'w') as f:
    f.write(json.dumps(test_dict))

with open('temp.json', 'r') as f:
    temp = f.read()
    new_dict = json.loads(temp)
    print(new_dict)
    print(type(new_dict))

