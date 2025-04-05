import json

# 16.4.1 使用loads()函数读取json字符串并转为json对象(python的字典类型)
print("====== 使用loads()函数读取json字符串并转为json对象 ======")
jsonData01 = '{"id":"201", "name":"张三201", "addr":"成都201"}'
jsonObj01 = json.loads(jsonData01)
print(type(jsonObj01)) # jsonObj01 是字典类型
print(jsonObj01)
# <class 'dict'>
# {'id': '201', 'name': '张三201', 'addr': '成都201'}

# 16.4.2 用dumps函数把json对象转为json字符串
print("\n====== 用dumps函数把json对象转为json字符串 ======")
jsonStr02 = json.dumps(jsonObj01)
print(type(jsonStr02))
print(jsonStr02)
# <class 'str'>
# {"id": "201", "name": "\u5f20\u4e09201", "addr": "\u6210\u90fd201"}
