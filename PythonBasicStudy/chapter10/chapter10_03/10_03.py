import zipfile, os, shutil
from pathlib import Path

# 读取zip文件
print("====== 读取zip文件 ======")
tempZip01 = zipfile.ZipFile(Path.cwd() / 'zipfile01.zip')
fileList = tempZip01.namelist()
print(str(fileList))
# ['zipfile01/a.txt', 'zipfile01/b.txt', 'zipfile01/']
print(type(fileList))
# <class 'list'>

for fileName in fileList:
    tempFile = tempZip01.getinfo(fileName)
    print(str(tempFile))
    print(tempFile.file_size)
    print(tempFile.compress_size)
    print("=== 我是分隔符 === ")
# 关闭zip文件
tempZip01.close()

# 10.3.2 从zip文件中解压缩
print("====== 从zip文件中解压缩所有文件 ======")
# 删除目标文件夹
shutil.rmtree(Path.cwd() / 'target_extract/zipfile01')
tempZip01 = zipfile.ZipFile(Path.cwd() / 'zipfile01.zip')
tempZip01.extractall(Path.cwd() / 'target_extract')
tempZip01.close()

print("====== 从zip文件中解压缩单个 ======")
tempZip01 = zipfile.ZipFile(Path.cwd() / 'zipfile01.zip')
# 删除目标文件夹
shutil.rmtree(Path.cwd() / 'target_extract/zipfile01')
result = tempZip01.extract("zipfile01/a.txt", Path.cwd() / 'target_extract')
print(result)
tempZip01.close()

# 10.3.3 创建和添加到zip文件
print("====== 创建和添加到zip文件 ======")
tempZip02 = zipfile.ZipFile(Path.cwd() / 'zipfile02.zip', "w")
tempZip02.write("10_03.py", compress_type=zipfile.ZIP_DEFLATED)
tempZip02.close()



