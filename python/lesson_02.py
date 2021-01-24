a = [1, 2, "6", 'summer']
if 'i' in a:
    print('i在这个列表里')
else:
    print('i不在这个列表里')

dict_1 ={"class_id": 45, "num": 20}
num = dict_1.get("num")
if num > 5:
    print("这个班级的人数是：{}".format(num))
else:
    print("这个班级人数不足5人")

list1 = ['肥兔', '露露', '一一', '芒果', '花花', '多多']
dict1 = {'name': '肥兔', 'gender': 'female','age': '18','city': '深圳'}
dict2 = {'name': '露露', 'gender': 'female', 'age': '19', 'city': '广州'}
dict3 = {'name': '一一', 'gender': 'male', 'age': '20', 'city': '广州'}
dict4 = {'name': '芒果', 'gender': 'male', 'age': '19', 'city': '北京'}
dict5 = {'name': '花花', 'gender': 'female', 'age': '18', 'city': '广州'}
dict6 = {'name': '多多', 'gender': 'female', 'age': '22', 'city': '上海'}
list2 = [dict1, dict2, dict3, dict4, dict5, dict6]
print(list2)

