import re

# 7.2.2 匹配regex对象
phonenumRegExpr = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
matchObj = phonenumRegExpr.search('Tom\'s number is 123-456-7890')
print('matched = ' + matchObj.group()) # matched = 123-456-7890


## 7.3 用正则表达式匹配更多模式
# 7.3.1 利用括号分组
print('\n\n==== 利用括号分组')
phonenumRegExpr = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
matchObj = phonenumRegExpr.search('Tom\'s number is 123-456-7890')
print(matchObj.group()) # 123-456-7890
print(matchObj.group(0)) # 123-456-7890
print(matchObj.group(1)) # 123
print(matchObj.group(2)) # 456-7890

# 遍历分组（分组实际上是一个元组）
print('\n\n===遍历分组（分组实际上是一个元组）')
groupTuple = matchObj.groups()
for group in groupTuple:
    print(group)
# 123
# 456-7890

# 也可以使用多重赋值
print('\n\n===使用多重赋值读取正则表达式分组')
first, second = matchObj.groups()
print(first, second, sep=',') # 123,456-7890

# 正则表达式中的特殊字符需要转移 包括
# . ^ $ * + ? { } [ ] \ | ( )
# 转译写法： \. \^ \$ \* \+ \? \{ \} \[ \] \\ \| \( \)

# 7.3.2 用管道匹配多个分组
# 字符|称为管道， 希望匹配许多表达式中的一个时，就可以使用它
print('\n\n===用管道匹配多个分组')
heroRegExpr = re.compile(r'zhangsan|lisi')
print(heroRegExpr.search('zhangsan and lisi').group()) # zhangsan
print(heroRegExpr.search('lisi and zhangsan').group()) # lisi

# 使用管道来匹配多个模式中的一个，这些模式可以是正则表达式中的一部分
print('\n\n===使用管道来匹配多个模式中的一个')
tempRegExpr01 = re.compile(r'Zhangsan(01|02|03)')
print(tempRegExpr01.search('Zhangsan01 is a student').group()) # Zhangsan01
print(tempRegExpr01.search('Zhangsan01 is a student').group(0)) # Zhangsan01
print(tempRegExpr01.search('Zhangsan01 is a student').group(1)) # 01

# 7.3.3 用?问号匹配0次或1次(如果匹配真正的?号，使用\?)
print('\n\n===用问号?实现可选匹配 ?匹配0次或1次')
regExpr03 = re.compile(r'zhangsan(110)?')
print(regExpr03.search('zhangsan111').group()) # zhangsan
print(regExpr03.search('zhangsan1100').group()) # zhangsan110

# 7.3.4 用*星号匹配0次或多次(如果匹配真正的*号，使用\*)
print('\n\n===用*星号匹配0次或多次')
regExpr04 = re.compile(r'Abc(wo)*man')
print(regExpr04.search('my name is Abcwoman').group()) # Abcwoman
print(regExpr04.search('my name is Abcman').group()) # Abcman
print(regExpr04.search('my name is Abcwowowoman').group()) # Abcwowowoman

# 7.3.5 用+加号匹配一次或多次 (如果匹配真正的+号，使用\+)
print('\n\n===用+加号匹配一次或多次')
regExpr05 = re.compile(r'Abc(wo)+man')
print(regExpr05.search('my name is Abcwoman').group()) # Abcwoman
print(regExpr05.search('my name is Abcman')) # 匹配失败，返回None, 调用None.group()报错
print(regExpr05.search('my name is Abcwowowoman').group()) # Abcwowowoman

# 7.3.6 用花括号匹配特定次数 (ha){3} 匹配 'HaHaHa' (ha){3,5} 匹配最少3个ha且最多5个ha的字符串
print('\n\n===用花括号匹配特定次数')
regExpr06 = re.compile(r'Abc(wo){3,5}man')
print(regExpr06.search('my name is Abcwoman')) # None 调用None的group()方法会报错
print(regExpr06.search('my name is Abcwowowoman').group()) # Abcwowowoman
print(regExpr06.search('my name is Abcwowowowoman').group()) # Abcwowowowoman
print(regExpr06.search('my name is Abcwowowowowoman').group()) # Abcwowowowowoman
print(regExpr06.search('my name is Abcwowowowowowoman')) # None 调用None的group()方法会报错


# 7.4 贪心与非贪心匹配
print('\n\n===贪心与非贪心匹配')
# 贪心 （匹配最长）
greedyHaRegExpr = re.compile(r'(Ha){3,5}')
print(greedyHaRegExpr.search('HaHaHaHaHa').group()) # HaHaHaHaHa

# 非贪心 (匹配最短)
nonGreedyHaRegExpr = re.compile(r'(Ha){3,5}?')
print(nonGreedyHaRegExpr.search('HaHaHaHaHa').group()) # HaHaHa


# 7.5 无分组的正则表达式的findall()方法：返回一个字符串列表
print('\n\n===正则表达式的findall()方法')
phonenumRegExpr = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
print(phonenumRegExpr.findall('home: 123-456-7890 work:111-222-3333'))
# ['123-456-7890', '111-222-3333']

# 7.5.2 有分组的正则表达式的findall()方法：返回匹配的元组列表
print('\n\n===有分组的正则表达式的findall()方法：返回元组列表')
phonenumRegExpr = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
print(phonenumRegExpr.findall('home: 123-456-7890 work:111-222-3333'))
# [('123', '456', '7890'), ('111', '222', '3333')]


# 7.8 插入字符^与美元字符$
# 插入字符^ 表示匹配发生在输入字符串的开头
# 美元字符$ 表示匹配发生在输入字符串的结尾
print('\n\n===插入字符^ 表示匹配发生在输入字符串的开头')
startWithHello = re.compile('^Hello')
print(startWithHello.search('Hello Wolrd').group()) # Hello
print(startWithHello.findall('Hello Wolrd'))  # ['Hello']
print(startWithHello.search('Hello Wolrd') == None)  # False

print('\n\n===美元字符$ 表示匹配发生在输入字符串的结尾')
endWithNumber = re.compile(r'\d$')
print(endWithNumber.search('zhangsan001').group()) # 1

# 7.9 通配字符
print('\n\n===通配字符')
# 句点字符(.) 匹配换行符之外的所有字符
pointRegExpr = re.compile(r'.at')
print(pointRegExpr.findall('the cat sat on the flat sofa')) # ['cat', 'sat', 'lat']
# 点星字符(.*) 匹配所有字符
pointStartRegExpr = re.compile(r'.*')
print(pointStartRegExpr.findall('the cat sat on the flat sofa')) # ['the cat sat on the flat sofa', '']

# 7.9.2 让句点字符(.) 匹配换行符
# 传入 re..DOTALL 作为 re.compile()的第2个参数，让句点可以匹配所有字符，包括换行符
newLineRegExpr = re.compile(r'.*', re.DOTALL)
print(newLineRegExpr.search('the cat sat on the flat sofa, \n and i sat on the bed yesterday.'))
print(newLineRegExpr.findall('the cat sat on the flat sofa, \n and i sat on the bed yesterday.'))
# ['the cat sat on the flat sofa, \n and i sat on the bed yesterday.', '']

# 7.11 不区分大小写匹配 把 re.IGNORECASE 或 re.I 作为 re.compile方法的第2个参数

# 7.12 用sub()方法替换字符串 （sub=substitute）
substituteExpr = re.compile(r'zhangsan')
print(substituteExpr.sub('lisi', 'zhangsan is a student.'))
# lisi is a student.

# 7.14 组合使用 re.IGNORECASE  re.DOTALL re.VERBOSE
composedExpr = re.compile(r'zhangsan \n and lisi', re.IGNORECASE | re.DOTALL | re.VERBOSE)
print(composedExpr.search('zhangsan \n and LISI are friends'))  # None

