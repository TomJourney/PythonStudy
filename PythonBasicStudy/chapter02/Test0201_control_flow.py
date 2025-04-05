# python 控制流 （if判断 + 循环）

import random
import sys

# 布尔类型
a1 = True and False
# -> False
print(a1)

a1 = not True
# -> False
print(a1)

a1 = not not True
# -> True
print(a1)

# 代码块： 根据代码行的缩进判断代码块的开始与结束。
# if控制流语句
print('\n=== if控制流语句 ===')
name = 'Tom01'
password = ''
if name == 'Tom01':
    print('Hello, ' + name)
    if password == '123456':
        print('check succ.')
    elif password == '':
        print('password 不能为空')
    else:
        print('check fail.')

# while 循环
print('\n=== while 循环 ===')
index = 0
while index < 5:
    print(index)
    index += 1
    if index <= 2:
        continue
    if index % 2 == 0:
        break

# for循环
print('\n=== for循环 ===')
for j in range(5):
    print('times = ' + str(j))

# for循环 + range函数(范围函数)
print('\n=== range函数，范围[2,5) , 步长递增1 ===')
for j in range(2, 5, 1):
    print('times = ' + str(j))

# for循环 + range函数(范围函数)
print('\n=== range函数，步长递减2 ===')
for j in range(5, -2, -2):
    print('times = ' + str(j))

# for循环 + 引入random模块 (import random)
print('\n=== 引入random模块 ===')
for i in range(5):
    print(random.randint(1, 10))

# 引入sys模块(import sys)， 调用sys.exit()函数
print('\n=== 使用sys.exit()函数 ===')
for i in range(1, 5):
    if i % 3 == 0:
        print("系统退出")
        sys.exit()
    print(i)
