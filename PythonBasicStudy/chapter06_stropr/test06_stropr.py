import pyperclip

# 6.1.1 字符串字面量
print("\n\n=== 字符串字面量")
# 字符串中有单引号
text01 = "this is tom's cat"
text02 = 'this is tom\'s cat'
text03 = ''' this is tom's cat '''
print(text01)
print(text02)
print(text03)

# this is tom's cat
# this is tom's cat
#  this is tom's cat

#  补充： 三行注释使用多行字符串三重引号 '''

# 原始字符串
text04 = r'this is tom\'s cat'
print("text04 = " + text04)
# text04 = this is tom\'s cat

print('使用三重引号注释多行-start')
'''
    代码行1
    代码行2
    代码行3
    ....
'''
print('使用三重引号注释多行-end')
# 使用三重引号注释多行-start
# 使用三重引号注释多行-end

# 6.1.2 字符串索引与切片
print('\n\n=== 字符串索引与切片')
text01 = 'hello world !'
print(text01[0]) # h
print(text01[-1]) # !
print(text01[0:5]) # hello 打印0到4的字符，不包括5
subText01 = text01[0:5]
print(subText01) # hello
print(text01) # hello world !

# 6.1.3 字符串的in与not in 操作
print('hello' in text01) # True
print('hello' not in text01) # False

# 6.2 将字符串放入到其他字符串
# 方法1 用 + 操作符拼接字符串
# 方法2： 利用字符串插值
name = 'AI'
age = 33
print('my name is %s, i am %s yeas old' % (name, age))
# 方法3： 使用f字符串
print(f'my name is {name}, i am {age} yeas old')

# my name is AI, i am 33 yeas old
# my name is AI, i am 33 yeas old

# 6.3 有用的字符串方法
# 6.3.1 字符串方法 upper() lower() isupper() islower()
print("\n\n=== 字符串方法 upper() lower() isupper() islower()")
text01 = 'Hello world'
print(text01.upper()) # 全部转为大写
print(text01.lower()) # 全部转为小写
print(text01.isupper()) # 是否全部为大写 False
print(text01.islower()) # 是否全部为小写 False
print(text01.upper().isupper()) # 是否全部为大写 True
print(text01.lower().islower()) # 是否全部为小写 True

# HELLO WORLD
# hello world
# False
# False
# True
# True

# 6.3.2 isX()字符串方法 isalpha()  isalnum()  isdecimal()  isspace()  istitle()
print('\n\n===isX()字符串方法 isalpha()  isalnum()  isdecimal()  isspace()  istitle()')
print('hello'.isalpha()) # True
print('hello123'.isalnum()) # True
print('123'.isdecimal()) # True
print(' '.isspace()) # True
print('Hello123'.istitle()) # True


# 【6.3.3】字符串方法 startswith() 与 endswith()
print('\n\n===字符串方法 startswith() 与 endswith()')
print('Hello123'.startswith('Hello')) # True
print('Hello123'.startswith('hello')) # False
print('Hello123'.endswith('123')) # True
print('Hello123'.endswith('12')) # False

# 6.3.4 字符串方法 join 和 split
# join() 对字符串列表做连接
print('\n\n=== join() 对字符串列表做连接')
list01 = ['aa', 'bb', 'cc']
joinResult = ','.join(list01)
print(joinResult) # aa,bb,cc

print('\n\n=== split() 把字符串分割为字符串列表')
joinResult = 'hello#world'
list02 = joinResult.split('#')
print(list02) # ['hello', 'world']
print(joinResult.split('ll'))  # ['he', 'o#world']

# 6.3.5 partition()分隔字符串
print('\n\n===partition()分隔字符串')
text01 = 'Hello world'
partitionResult = text01.partition('worl')
print(partitionResult) # ('Hello ', 'worl', 'd')

partitionResult02 = text01.partition('tom')
print(partitionResult02) # ('Hello world', '', '')

# 利用多重赋值技巧接收partition()的结果
before, seperator, after = text01.partition('worl')
print(before)  # Hello
print(seperator) # worl
print(after) # d

# 6.3.6 使用 rjust(), ljust()， center() 对其文本
print('\n\n=== 使用 rjust(), ljust()， center() 对其文本')
print('Hello'.rjust(10))
print('Hello'.rjust(10, '*'))
print('Hello'.ljust(10))
print('Hello'.ljust(10, '*'))
print('Hello'.center(10))
print('Hello'.center(10, '*'))

#      Hello
# *****Hello
# Hello
# Hello*****
#   Hello
# **Hello***

# 6.3.7 使用strip(), rstrip()和lstrip()删除空白字符
print('\n\n===使用strip(), rstrip()和lstrip()删除空白字符')
str07 = '  hello '
print('[' + str07.strip() + ']') # [hello]
print('[' + str07.rstrip() + ']') # [  hello]
print('[' + str07.lstrip() + ']') # [hello ]

# 6.4 使用ord()获取单字符字符串的ascii码，chr()函数获取ascii码对应的单字符字符串
print('\n\n===使用ord()获取单字符字符串的ascii码，chr()函数获取ascii码对应的单字符字符串')
print(ord('A')) # 65
print(chr(65)) # A
print(chr(ord('a'))) # a

# 6.5 使用 pyperclip模块 复制粘贴字符串
# pyperclip模块有copy与paste函数，用于向计算机的剪贴板发送文本或接收文本
print('\n\n===pyperclip模块有copy与paste函数，用于向计算机的剪贴板发送文本或接收文本')
pyperclip.copy('hello, world')
print('pyperclip.paste() = ' + pyperclip.paste())  # pyperclip.paste() = hello, world







