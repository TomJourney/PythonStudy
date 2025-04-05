import send2trash

# 使用send2trash模块，把文件夹和文件发送到回收站，而不是永久删除它们
# tempResult = send2trash.send2trash("send2trash_test_dir")
# print(tempResult)
# None

# 使用os.walk()遍历文件夹下的子文件夹及文件
import os
from pathlib import Path
root_dir = Path.cwd() / "src"
for cur_dir, sub_dirs, sub_files in os.walk(root_dir):
    print("当前文件夹=" + cur_dir)
    print("子文件夹列表=" + str(sub_dirs))
    print("子文件列表=" + str(sub_files))
    print("========== 我是分隔符 ==========")
