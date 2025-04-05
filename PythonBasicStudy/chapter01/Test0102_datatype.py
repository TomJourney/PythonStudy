# python问答式小程序

print('hello world')

print('what is your name')
myName = input()
print('nice to meet you, ' + myName)
# 会报错，python无法自动把int转为字符串类型
# print('the legnth of your name is ' + len(myName))
print('the legnth of your name is ' + str(len(myName)))

# 询问年龄
print('what is your age')
myAge = int(input())
print('you will be ' + str(int(myAge + 1)) + ' in next year')

# python中常见的数据类型有3种： 整形，浮点型，字符串

# 函数介绍
# print() 打印
# input() 等待输入
# len() 字符串中字符个数
# str(x) 把x转为字符串
# int(x) 把x转为整型数值
# float(x) 把x转为浮点型数值
