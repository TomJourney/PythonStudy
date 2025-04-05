# 9 读写文件
# 9.1 文件与文件路径
from pathlib import Path

print('\n\n=== pathlib模块的Path()函数打印路径分隔符')
print(Path('a', 'b', 'c')) # a\b\c
print(type(Path('a', 'b', 'c'))) #  <class 'pathlib.WindowsPath'>

# 把文件名称连接到文件夹名称末尾
print('\n\n===把文件名称连接到文件夹名称末尾')
myFiles = ['a.txt', 'b.txt']
for fileName in myFiles:
    print(Path(r'D:\studynote\05-python_discover\file', fileName))

# D:\studynote\05-python_discover\file\a.txt
# D:\studynote\05-python_discover\file\b.txt

# 9.1.2 使用/运算符连接路径
print(Path('a') / 'b' / 'c') # a\b\c

# 9.1.3 当前工作目录 使用Path.cwd()函数获取
print('\n\n===当前工作目录：', Path.cwd())
# D:\studynote\00-ai-llm\workbench\PythonBasicStudy\chapter09_rw_file

# 9.1.4 Path.home() 主目录
print(Path.home()) # C:\Users\xxx

# 9.1.5 绝对路径与相对路径
# 9.1.6 使用os.makedirs 创建新文件夹(同时创建多个嵌套子文件夹)
print('\n\n=== 使用os.makedirs 创建新文件夹(同时创建多个嵌套子文件夹)')
import os
# os.makedirs(str(Path.cwd()) + '/d3/d33/d333')
# # mkdir()只能创建一个目录
# Path(Path.cwd() / 'e2').mkdir()

def diy_makedirs_if_not_exist(path):
    if not path.exists():
        os.makedirs(path)

def diy_mkdir_if_not_exist(path):
    if not path.exists():
        path.mkdir()


# 创建嵌套子文件夹
diy_makedirs_if_not_exist(Path.cwd() / '/d4/d44/d444')
# 创建单个文件夹
diy_mkdir_if_not_exist(Path.cwd() / '/e4')




# 9.1.7 处理绝对路径与相对路径
print(Path.cwd().is_absolute()) # True

# 从相对路径获取绝对路径
print('\n\n===从相对路径获取绝对路径(把 Path.cwd()放在相对路径Path对象的前面)')
print(Path('d1/d2/d3')) # d1\d2\d3
print(Path.cwd() / Path('d1/d2/d3'))
# D:\studynote\00-ai-llm\workbench\PythonBasicStudy\chapter09_rw_file\d1\d2\d3

# os.path() 提供的一些函数
print('\n\n===os.path() 提供的一些函数')
absolutePath = Path.cwd() / Path('d1/d2/d3')
relativePath = Path('d1/d2/d3')

# 返回参数的绝对路径的字符串
print(os.path.abspath(absolutePath))
# 若参数path是一个绝对路径，则返回True； 若是相对路径，则返回False
print(os.path.isabs(absolutePath))
# 返回从开始路径start到path的相对路径的字符串； 若没有提供start开始路径，则把当前工作目录作为开始路径
print(os.path.relpath(absolutePath))

# D:\studynote\00-ai-llm\workbench\PythonBasicStudy\chapter09_rw_file\d1\d2\d3
# True
# d1\d2\d3

# 9.1.8 取得文件路径的各个部分
print('\n\n=== 取得文件路径的各个部分')
filePath01 = Path(Path.cwd() / Path('a1/a1_temp.txt'))
print('file01.anchor = ' + filePath01.anchor)
print('file01.parent = ' + str(filePath01.parent))
print('file01.name = ' + filePath01.name)
print('file01.stem = ' + filePath01.stem) # stem表示主干名，即基本文件名（不包括后缀）
print('file01.suffix = ' + filePath01.suffix)
print('file01.drive = ' + filePath01.drive)

# file01.anchor = D:\
# file01.parent = D:\studynote\00-ai-llm\workbench\PythonBasicStudy\chapter09_rw_file\a1
# file01.name = a1_temp.txt
# file01.stem = a1_temp
# file01.suffix = .txt
# file01.drive = D:

print('\n\n=== 使用os.path的函数')
filePath01 = Path(Path.cwd() / Path('a1/a1_temp.txt'))
print(os.path.dirname(filePath01))
print(os.path.basename(filePath01))
print(os.path.split(filePath01))
print(str(filePath01).split(os.sep)) # 通过字符串分割

# D:\studynote\00-ai-llm\workbench\PythonBasicStudy\chapter09_rw_file\a1
# a1_temp.txt
# ('D:\\studynote\\00-ai-llm\\workbench\\PythonBasicStudy\\chapter09_rw_file\\a1', 'a1_temp.txt')
# ['D:', 'studynote', '00-ai-llm', 'workbench', 'PythonBasicStudy', 'chapter09_rw_file', 'a1', 'a1_temp.txt']

# 9.1.9 查看文件大小和文件夹内容
print('\n\n===查看文件大小和文件夹内容')
filePath01 = Path(Path.cwd() / Path('a1/a1_temp.txt'))
print(os.path.getsize(filePath01)) # 34
print(os.listdir(Path.cwd())) # ['a1', 'd1', 'test01', 'test09_rw_file.py']

print('\n\n===计算某个文件夹下文件总大小')
totalSize = 0
for fileName in os.listdir(Path.cwd()):
    tempPath = os.path.join(Path.cwd(), fileName)
    print(str(tempPath) + '的文件大小=' + str(os.path.getsize(tempPath)))
    totalSize += os.path.getsize(tempPath)
print('文件总大小 = ' + str(totalSize))

# ===计算某个文件夹下文件总大小
# D:\studynote\00-ai-llm\workbench\PythonBasicStudy\chapter09_rw_file\a01.txt的文件大小=128
# D:\studynote\00-ai-llm\workbench\PythonBasicStudy\chapter09_rw_file\a02.txt的文件大小=3
# D:\studynote\00-ai-llm\workbench\PythonBasicStudy\chapter09_rw_file\a1的文件大小=0
# D:\studynote\00-ai-llm\workbench\PythonBasicStudy\chapter09_rw_file\d1的文件大小=0
# D:\studynote\00-ai-llm\workbench\PythonBasicStudy\chapter09_rw_file\d2的文件大小=0
# D:\studynote\00-ai-llm\workbench\PythonBasicStudy\chapter09_rw_file\d3的文件大小=0
# D:\studynote\00-ai-llm\workbench\PythonBasicStudy\chapter09_rw_file\e2的文件大小=0
# D:\studynote\00-ai-llm\workbench\PythonBasicStudy\chapter09_rw_file\temp01_binary.data.bak的文件大小=19
# D:\studynote\00-ai-llm\workbench\PythonBasicStudy\chapter09_rw_file\temp01_binary.data.dat的文件大小=39
# D:\studynote\00-ai-llm\workbench\PythonBasicStudy\chapter09_rw_file\temp01_binary.data.dir的文件大小=19
# D:\studynote\00-ai-llm\workbench\PythonBasicStudy\chapter09_rw_file\temp02.py的文件大小=86
# D:\studynote\00-ai-llm\workbench\PythonBasicStudy\chapter09_rw_file\test01的文件大小=0
# D:\studynote\00-ai-llm\workbench\PythonBasicStudy\chapter09_rw_file\test09_rw_file.py的文件大小=8270
# D:\studynote\00-ai-llm\workbench\PythonBasicStudy\chapter09_rw_file\__pycache__的文件大小=0
# 文件总大小 = 8564

# 9.1.10
print('\n\n===使用通配符模式修改文件列表')
dirPath = Path.cwd()
list01 = list(dirPath.glob('*.txt'))
print(list01)
# [WindowsPath('D:/studynote/00-ai-llm/workbench/PythonBasicStudy/chapter09_rw_file/a01.txt'),
# WindowsPath('D:/studynote/00-ai-llm/workbench/PythonBasicStudy/chapter09_rw_file/a02.txt')]

# 9.1.11 检查路径有效性
print('\n\n===检查路径有效性')
filePath01 = Path(Path.cwd() / Path('a1/a1_temp.txt'))
print(filePath01.exists()) # True
print(filePath01.is_file()) # True
print(filePath01.is_dir()) # False
