from pathlib import Path

print(Path.cwd())
# D:\studynote\00-ai-llm\workbench\PythonBasicStudy\.venv\Scripts\python.exe D:\studynote\00-ai-llm\workbench\PythonBasicStudy\chapter10\test10_exercise01.py
# D:\studynote\00-ai-llm\workbench\PythonBasicStudy\chapter10

print(type(Path.cwd()))
# <class 'pathlib.WindowsPath'>

print(Path.cwd() / 'a')
# D:\studynote\00-ai-llm\workbench\PythonBasicStudy\chapter10\a

print(type(Path.cwd() / 'a'))
# <class 'pathlib.WindowsPath'>

print(Path.cwd() / Path('a'))
# D:\studynote\00-ai-llm\workbench\PythonBasicStudy\chapter10\a

print(type(Path.cwd() / Path('a')))
# <class 'pathlib.WindowsPath'>