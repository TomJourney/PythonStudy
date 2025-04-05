import pprint

# 字典例子
student = {'name':'zhangsan', 'age':10}
print(student) # {'name': 'zhangsan', 'age': 10}
# 根据键获取值
print(student['name']) # zhangsan


# 5.1.2 keys(), values(), items()
print("\n\n===keys(), values(), items()")
dict01 = {'zhangsan':'cd03', 'lisi':'cd04'}
for temp in dict01.values():
    print(temp)

# cd03
# cd04

# 遍历键
print("\n\n=== 遍历键")
for temp in dict01.keys():
    print(temp)

# zhangsan
# lisi

# 遍历值
print("\n\n=== 遍历值")
for item in dict01.items():
    print(item)

# ('zhangsan', 'cd03')
# ('lisi', 'cd04')

# 遍历键值
print("\n\n=== 遍历键值")
for k,v in dict01.items():
    print('key = ' + k + ', value = ' + v)

# key = zhangsan, value = cd03
# key = lisi, value = cd04

# 返回为列表（使用list函数）
print("\n\n=== 返回值转为列表（使用list函数）")
keyList01 = list(dict01.keys())
valueList01 = list(dict01.values())
itemList01 = list(dict01.items())
print(keyList01)
print(valueList01)
print(itemList01)

# ['zhangsan', 'lisi']
# ['cd03', 'cd04']
# [('zhangsan', 'cd03'), ('lisi', 'cd04')]

# 5.1.3 检查字典中是否存在键或值
print("\n\n === 检查字典中是否存在键或值")
dict01 = {'zhangsan':'cd03', 'lisi':'cd04'}
print('zhangsan' in dict01.keys()) # True
print('zhangsan' in dict01) # True
print('cd03' not in dict01.values()) # False

# 5.1.4 get(key,default_value) 方法 获取键key在字典中的值，若键不存在返回默认值default_value
print("\n\n === get(key,default_value) 方法 获取键key在字典中的值，若键不存在返回默认值default_value")
print(dict01.get('zhangsan')) # cd03
print(dict01.get('wangwu', 'None')) # None

# 5.1.5 setdefault(key,newValue) 设置键的值为newValue，若键不存在时；若键存在，则返回键的初始值
print("\n\n=== setdefault(key,newValue) 设置键的值为newValue，若键不存在时；若键存在，则返回键的初始值")
dict01 = {'zhangsan':'cd03', 'lisi':'cd04'}
dict01.setdefault("wangwu", "cd05")
dict01.setdefault("zhangsan", "beij03")
print(dict01)
# {'zhangsan': 'cd03', 'lisi': 'cd04', 'wangwu': 'cd05'}

# 练习题： 计算一个字符串中每个字符出现的次数
print("\n\n=== 计算一个字符串中每个字符出现的次数")
message = 'hello world'
count = {}
for temp in message:
    count.setdefault(temp, 0)
    count[temp] += 1
print(count)
# {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}

## 5.2 美观的输出 引入 pprint模块  import pprint
print('\n\n=== 美观的输出 引入 pprint模块  import pprint')
print('count = ' + str(count))
pprint.pprint(count)
# {' ': 1, 'd': 1, 'e': 1, 'h': 1, 'l': 3, 'o': 2, 'r': 1, 'w': 1} 键是排序过的

print(pprint.pformat(count))
# {' ': 1, 'd': 1, 'e': 1, 'h': 1, 'l': 3, 'o': 2, 'r': 1, 'w': 1}

## 5.3 使用数据结构对真实世界建模
# 5.3.2 嵌套的字典和列表
print('\n\n=== 使用数据结构对真实世界建模')
allGuests = {'zhangsan': {'apple': 1, 'egg': 2}
             , 'lisi': {'apple': 3, 'egg': 4}
             , 'wangwu': {'orange': 5, 'salad': 6}
}

def totalBring(guests, item):
    numBring = 0
    for k, v in guests.items():  # 遍历键值对
        numBring += v.get(item, 0)
    return numBring


# 统计带了多少个apple
appleNum = totalBring(allGuests, 'apple')
print("appleNum = " + str(appleNum))

#





