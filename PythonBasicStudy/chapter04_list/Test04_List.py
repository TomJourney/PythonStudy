import random
import copy

list00 = ['1', '2', 3, 4, True]
print(list00)

# 用索引取得列表中的单个值
list01 = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(list01[0]) # a

# 列表中的元素还可以是列表
twoDimensionArr = [['a11', 'a12', 'a13'], ['a21', 'a22', 'a23'], ['a31', 'a32', 'a33'], [41, 42.2, 'a43', 'a44', 'a45']]
print(twoDimensionArr[0])
print(twoDimensionArr[1])
print(twoDimensionArr[2])
print(twoDimensionArr[3])

# ['a11', 'a12', 'a13']
# ['a21', 'a22', 'a23']
# ['a31', 'a32', 'a33']
# [41, 42.2, 'a43', 'a44', 'a45']

# 负数索引
list01 = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(list01[-1]) # g
print(list01[-2]) # f

# 利用切片取得子列表
print("利用切片取得子列表")
list01 = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(list01[1:4]) # ['b', 'c', 'd']
print(list01[0:-1]) # ['a', 'b', 'c', 'd', 'e', 'f']
print(list01[:])  # ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(list01[0:])  # ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(list01[0:len(list01)])  # ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(list01[:2])  # ['a', 'b'] 下标0,1，不包含下标2的元素

# 列表长度
print(len(list01)) # 7

# 修改列表中的元素
list01[0] = 'a_v2'
print(list01)
# ['a_v2', 'b', 'c', 'd', 'e', 'f', 'g']

# 列表连接和列表复制
list02 = ['a1', 'a2', 'a3']
list03 = list02 + ['a4', 'a5', 'a6']
print(list03[:])
# ['a1', 'a2', 'a3', 'a4', 'a5', 'a6']

list04 = list02 * 2
print(list04[:])
# ['a1', 'a2', 'a3', 'a1', 'a2', 'a3']

# 用del语句删除列表中的元素
list05 = [1, 2, 3]
del list05[0]
print(list05[:])
# [2, 3]


# 列表用于循环
# 遍历列表
for i in range(4):
    print(i)
# 0
# 1
# 2
# 3

# 遍历列表
for i in [1, 2, 3]:
    print(i)

# 1
# 2
# 3

# 遍历列表2
arr01 = ['10', 20, 30, 40]
for i in range(len(arr01)):
    print('index=' + str(i) + ', value=' + str(arr01[i]))

# index=0, value=10
# index=1, value=20
# index=2, value=30
# index=3, value=40

# in 和 not in 操作符
print('10' in arr01)
print('20' in arr01)
print(20 in arr01)
print(20 not in arr01)
# True
# False
# True
# False

# 20存在于arr01数组
print("=== 20存在于arr01数组 ===")
if 20 not in arr01:
    print(str(20) + '不存在于arr01数组')
else:
    print(str(20) + '存在于arr01数组')


# 多重赋值技巧 （类似于react的解构赋值）
print("=== 多重赋值技巧 === ")
colorArr = ['red', 'green', 'blue']
e1, e2, e3 = colorArr
print(e1, e2, e3) # red green blue

# enumerate()与列表一起使用（类似于java的foreach循环）
print("\nenumerate()与列表一起使用（类似于java的foreach循环）")
colorArr = ['red', 'green', 'blue']
for index, value in enumerate(colorArr):
    print('index[' + str(index) + '] = ' + value)

# enumerate()与列表一起使用（类似于java的foreach循环）
# index[0] = red
# index[1] = green
# index[2] = blue

# random.choice() 和 random.shuffle() 与列表一起使用
print("\n === random.choice() 和 random.shuffle() 与列表一起使用")
peopleArr = ['zhangsan', 'lisi', 'wangwu', 'zhaoliu']
print(random.choice(peopleArr)) # lisi

# 洗牌函数shuffle() 将就地修改列表，而不是返回新列表
print("\n\n=== 洗牌函数shuffle() 将就地修改列表，而不是返回新列表")
random.shuffle(peopleArr)
print(peopleArr)
print(peopleArr[:])

# ['wangwu', 'zhangsan', 'zhaoliu', 'lisi']
# ['wangwu', 'zhangsan', 'zhaoliu', 'lisi']

print("\n\n === 增强的赋值操作")

# 4.3 增强的赋值操作
age = 42
age += 1
print(age) # 43

age -= 3
print(age) # 40

# 用index发发发在列表中查找值，返回索引下标
peopleArr = ['a', 'b', 'c', 'd']
print(peopleArr.index('a')) # 0

# 4.4.2 用append()方法和insert()方法在列表中添加值， 列表被就地修改
alphabetArr = ['a', 'b', 'c', 'd']
alphabetArr.append('e1')
print(alphabetArr)  # ['a', 'b', 'c', 'd', 'e1']

alphabetArr.insert(1, 'f1')
print(alphabetArr) # ['a', 'f1', 'b', 'c', 'd', 'e1']

# 4.4.3 用remove方法删除列表中的值
print('\n=== 用remove方法删除列表中的值')
alphabetArr = ['a', 'b', 'c', 'd']
alphabetArr.remove('a')
print(alphabetArr) # ['b', 'c', 'd']

# 4.4.4 使用 sort()方法将列表的值排序
print("\n\n=== 使用 sort()方法将列表的值排序")
alphabetArr = ['f', 'e', 'a', 'b', 'd', 'c']
alphabetArr.sort()
print(alphabetArr) # ['a', 'b', 'c', 'd', 'e', 'f']

alphabetArr.sort(reverse=True)
print(alphabetArr) # ['f', 'e', 'd', 'c', 'b', 'a']

# 4.4.5 使用 reverse()方法 反转列表中的值
print("使用 reverse()方法 反转列表中的值")
alphabetArr = ['a', 'b', 'c', 'd']
alphabetArr.reverse()
print(alphabetArr) # ['d', 'c', 'b', 'a']


# 4.6 序列数据类型
name = 'Student'
print(name[0]) # S
print(name[-2]) # n
print(name[0:4]) # Stud
print('St' in name) # True
print('t' in name) # True
for i in name:
    print(i)

# S
# t
# u
# d
# e
# n
# t

# 4.6.1 可变与不可变数据类型
# 列表是可变的， 字符串是不可变的

# 4.6.2 元组数据类型
print('\n=== 元组数据类型 === ')
eggs = ('hello', 42, 53)
print(eggs[0]) # hello
print(eggs[1:]) # (42, 53)
print(len(eggs)) #

# 类型
print('\n=== 变量的数据类型 === ')
print(type(('hello', ))) # <class 'tuple'>
print(type(('hello')))  # <class 'str'>

# 4.6.3 使用list()和tuple()来转换类型， 分别转换为列表与元组
print('\n=== 使用list()和tuple()来转换类型， 分别转换为列表与元组')
tuple01 = tuple(['a1', 'a2', 'a3'])
print(type(tuple01)) # <class 'tuple'>
print(list(tuple01)) # ['a1', 'a2', 'a3']
print(list('hello')) # ['h', 'e', 'l', 'l', 'o']

# 4.7 引用
print('\n\n=== 引用')

# 4.7.1 标识和id()函数
a = 'hello'
print(id(a)) # 2897082779712
a += ' wolrd'
print(id(a)) # 2897082736432

# append()方法不会创建新的列表，而是就地修改对象
print("\n\n === append()方法不会创建新的列表，而是就地修改对象")
arr = ['a', 'b', 'c']
print(id(arr)) # 2844017850560
arr.append('d')
print(id(arr)) # 2844017850560


# 4.7.3 copy模块的copy() 和 deepcopy()
# import copy
print('\n=== copy模块的copy() 和 deepcopy()')
arr = ['a', 'b', 'c', 'd']
print(id(arr)) # 2250866974592

# copy模块的copy()复制
arr2 = copy.copy(arr)
print(id(arr2)) # 2250866981056

# 修改arr2的第1个元素
arr2[0] = 'apple'
print(arr2)  # ['apple', 'b', 'c', 'd']
print(arr) # ['a', 'b', 'c', 'd']

# 如果要复制的列表中包含了列表， 那就使用copy.deepcopy()函数来代替，
# deepcopy()将同时复制它们内部的列表


