from pathlib import Path
import datetime

# 9.2 文件读写过程
print('\n\n===文件读写过程')
filePath01 = Path(Path.cwd() / Path('a1/a2_temp.txt'))
filePath01.write_text('hello, my name is a2_temp.txt. now=' + str(datetime.datetime.now()))
print(filePath01.read_text()) # hello, my name is a2_temp.txt.

print('\n\n=== 使用open函数打开文件对象')
tempFile01 = open(Path(Path.cwd() / Path('a1/a2_temp.txt')))
tempFile02 = open(Path(Path.cwd() / Path('a1/a2_temp.txt')), 'r')
# File.read() 把文件内容读取为一个字符串
print(tempFile01.read())
print(tempFile02.read())
# hello, my name is a2_temp.txt. now=2025-03-25 22:26:52.686045
# hello, my name is a2_temp.txt. now=2025-03-25 22:26:52.686045

# 读取文件的行
print('\n\n===读取文件的行')
tempFile03 = open(Path(Path.cwd() / Path('a01.txt')), 'r')
print(tempFile03.readlines())
# ['hello zhangsan.\n', ' my name is a01.txt 2025-03-25 22:26:45.921792\n', 'hello zhangsan.\n', ' my name is a01.txt 2025-03-25 22:26:45.922780']

# 9.2.3 写入文件 (有2种模式， 写模式-w， 追加模式-a)
print('\n\n===写入文件后读取文件，写模式-w')
tempFile03 = open(Path(Path.cwd() / Path('a01.txt')), 'w')
tempFile03.write('hello zhangsan.\n my name is a01.txt ' + str(datetime.datetime.now()))
tempFile03.close()
# 读取写入后的文件
tempFile03 = open(Path(Path.cwd() / Path('a01.txt')), 'r')
print(tempFile03.readlines())
# ['hello zhangsan.\n', ' my name is a01.txt 2025-04-04 09:49:07.844177']

print('\n\n===写入文件后读取文件，追加模式-a')
tempFile03 = open(Path(Path.cwd() / Path('a01.txt')), 'a')
tempFile03.write('\nhello zhangsan.\n my name is a01.txt ' + str(datetime.datetime.now()))
tempFile03.close()
# 读取写入后的文件
tempFile03 = open(Path(Path.cwd() / Path('a01.txt')), 'r')
print(tempFile03.readlines())
# ['hello zhangsan.\n', ' my name is a01.txt 2025-04-04 09:49:07.844177\n', 'hello zhangsan.\n', ' my name is a01.txt 2025-04-04 09:49:07.846173']


# 9.3 使用 shelve 模块保存变量 (shelve-搁置)
import shelve
print('\n\n=== 把变量保存到二进制的shelf文件')
shelfFile = shelve.open(str(Path.cwd() / Path('temp01_binary.data')))
colors = ['red', 'green', 'yellow']
shelfFile['colors'] = colors
shelfFile.close()

print('\n\n=== 从二进制shelf文件读取保存的变量')
shelfFile = shelve.open(str(Path.cwd() / Path('temp01_binary.data')))
print(type(shelfFile))
print(shelfFile['colors'])
shelfFile.close()

# <class 'shelve.DbfilenameShelf'>
# ['red', 'green', 'yellow']

# 如字典一样， shelf文件有keys() values方法
print('\n\n=== 如字典一样， shelf文件有keys() values方法')
shelfFile = shelve.open(str(Path.cwd() / Path('temp01_binary.data')))
print(shelfFile.keys())
print(shelfFile.values())
shelfFile.close()
# KeysView(<shelve.DbfilenameShelf object at 0x000001EB98E80920>)
# ValuesView(<shelve.DbfilenameShelf object at 0x000001EB98E80920>)

# 9.4 使用pprint.pformat() 保存变量到文本文件
import pprint
print('\n\n===使用pprint.pformat() 保存变量到文本文件')
customers = [{'name': 'zhangsan', 'addr': 'cd03'}, {'name': 'lisi', 'addr': 'cd04'}]
pprint.pprint(customers)
# [{'addr': 'cd03', 'name': 'zhangsan'}, {'addr': 'cd04', 'name': 'lisi'}]
fileObj = open(Path.cwd() / Path('temp02.py'), 'w')
fileObj.write('customers = ' + pprint.pformat(customers) + '\n')
fileObj.close()

# 读取保存的文本文件中的变量
print('\n\n===读取保存的文本文件中的变量')
import temp02
print(temp02.customers)
# [{'addr': 'cd03', 'name': 'zhangsan'}, {'addr': 'cd04', 'name': 'lisi'}]





