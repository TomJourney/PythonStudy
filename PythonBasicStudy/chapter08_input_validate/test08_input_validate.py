
# 第8章 输入验证

# 8.1 PyInputPlus模块
import pyinputplus as pyip
response = pyip.inputNum()
print(response)

# 有提示的输入
result = pyip.inputInt(prompt='enter a number: ')
print(result)

# 8.1.1 关键字参数 min max greaterThan lessThan
response = pyip.inputInt(prompt='enter a number (value range 4-6): ', min=4, max=6)
print(response)