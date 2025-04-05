# 11.2 获取回溯字符串
import traceback


def dinner():
    bacon()


def bacon():
    raise Exception('this is the error msg.')


# 调用函数，打印异常的回溯信息
# dinner()

# Traceback (most recent call last):
#   File "D:\studynote\00-ai-llm\workbench\PythonBasicStudy\chapter11\1102.py", line 9, in <module>
#     dinner()
#   File "D:\studynote\00-ai-llm\workbench\PythonBasicStudy\chapter11\1102.py", line 4, in dinner
#     bacon()
#   File "D:\studynote\00-ai-llm\workbench\PythonBasicStudy\chapter11\1102.py", line 6, in bacon
#     raise Exception('this is the error msg.')
# Exception: this is the error msg.

import traceback
from pathlib import Path

def dinnerWithTraceBack():
    try:
        dinner()
    except:
        errorFile = open(Path.cwd() / 'errorInfo.txt', 'w')
        # 把异常的回溯信息写入文件
        errorFile.write(traceback.format_exc())
        errorFile.close()
        print('the traceback info was written to errorInfo.txt')


# 调用函数，使用traceback收集异常信息
dinnerWithTraceBack()
