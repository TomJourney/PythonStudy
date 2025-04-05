# 10.1 shutil 模块
# shutil(或称为shell工具) 包含一些函数，可以复制，移动，重命名和删除文件
import shutil, os
import time
from pathlib import Path

# 创建文件 src/src03_A.txt
def newSrc01TxtFileIfNotExist():
    local_path = Path.cwd() / 'src/src03_A.txt'
    if local_path.exists():
        return
    temp_file = open(local_path, 'w')
    temp_file.write('hello,\nmy name is src03_A.txt.')
    temp_file.close()

def force_new_dir(temp_path):
    if os.path.exists(temp_path):
        shutil.rmtree(temp_path)
    os.makedirs(temp_path)

def force_new_file(temp_path):
    if os.path.exists(temp_path):
        os.remove(temp_path)
    temp_file = open(temp_path, 'w')
    temp_file.close()

# 删除文件夹与其下各层级文件夹及文件
def force_remove_dir(temp_path):
    if os.path.exists(temp_path):
        shutil.rmtree(temp_path)

# 强行删除一个文件
def force_remove_file(temp_path):
    if os.path.exists(temp_path):
        os.remove(temp_path) # os.remove() 等同于 os.unlink()

# 删除文件夹delete_dir_a与其下各层级文件夹及文件
force_remove_dir(Path.cwd() / "delete_dir_a")

# 10.1.1 复制文件和文件夹
print('\n\n===复制文件')
newSrc01TxtFileIfNotExist() # 创建文件 src/src03_A.txt
force_new_dir(Path.cwd() / 'target')
copyResult = shutil.copy(Path.cwd() / 'src/src03_A.txt', Path.cwd() / 'target')
print(copyResult)
# D:\studynote\00-ai-llm\workbench\PythonBasicStudy\chapter10\target\src03_A.txt

copyResult2 = shutil.copy(Path.cwd() / 'src/src03_A.txt', Path.cwd() / 'target/src03_A.txt')
print(copyResult2)
# D:\studynote\00-ai-llm\workbench\PythonBasicStudy\chapter10\target\src03_A.txt

# 10.1.1.1 复制文件夹及其下文件-shutil.copytree
# 先删除目的地文件夹
force_remove_dir('target_backup')
# 复制到目的地文件夹
copyDirResult = shutil.copytree(Path.cwd() / 'target', Path.cwd() / 'target_backup')
print(copyDirResult)
# D:\studynote\00-ai-llm\workbench\PythonBasicStudy\chapter10\target_backup

# 10.1.2 文件和文件夹的移动与重命名
# 情况1：src是文件夹名，des是文件夹名；等同于移动文件夹并重命名文件夹；
# 先删除目的地文件夹
force_remove_dir('target_backup2')
tempResult = shutil.move(Path.cwd() / 'target_backup', Path.cwd() / 'target_backup2')
print(tempResult)
# D:\studynote\00-ai-llm\workbench\PythonBasicStudy\chapter10\target_backup2

# 情况2： 情况2：src是文件名，des是文件夹名；等同于把文件剪切到文件夹
# 先删除目的地文件夹下的文件
# force_remove_file(Path.cwd() / 'move_dir/src03.txt')
# # 剪切文件
# tempResult = shutil.move(Path.cwd() / 'target_backup3/src03.txt', Path.cwd() / 'move_dir')
# print(tempResult)
# D:\studynote\00-ai-llm\workbench\PythonBasicStudy\chapter10\move_dir\src03.txt

# 情况3： src是文件名，des是文件名； 等同于移动文件并重命名文件；
# 先删除目的地文件夹下的文件
# force_remove_file(Path.cwd() / 'move_dir/src03_A_moved.txt')
# tempResult = shutil.move(Path.cwd() / 'target_backup3/src03_A.txt', Path.cwd() / 'move_dir/src03_A_moved.txt')
# print(tempResult)
# # D:\studynote\00-ai-llm\workbench\PythonBasicStudy\chapter10\move_dir\src03_A_moved.txt
#
# # 情况4: src是文件名，des是文件夹名称；但des不存在， 则把src表示的文件重命名为des(把target_backup3/src03_C.txt文件重命名为./move_dir2)
# tempResult = shutil.move(Path.cwd() / 'target_backup3/src03_C.txt', Path.cwd() / 'move_dir2')
# print(tempResult)
# # D:\studynote\00-ai-llm\workbench\PythonBasicStudy\chapter10\move_dir2