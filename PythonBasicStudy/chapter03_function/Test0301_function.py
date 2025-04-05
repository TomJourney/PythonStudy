print('\n=== 定义有参函数 ===')


def hello(username):
    print('hello ' + username)


# 调用有参函数
hello('tom')


print('\n=== 定义有返回值函数 ===')

def hello2(user_id, username):
    if user_id % 2 == 0:
        return '\nid为偶数， hello ' + username
    else:
        return '\nid为奇数， hello ' + username

# 调用有返回值函数
desp = hello2(3, 'zhangsan')
print(desp)
print(hello2(4, 'lisi'))

# None值：表示没有值。 None是NoneType数据类型的唯一值（如java的null）。与布尔值True，False相同，None首字母必须大写。
result = print(None) # None
print(result == None)  # True

# 关键字参数和print函数
print('\n=== 普通print函数 ===')
print('Hello')
print('World')

# 设置end关键字参数
print('\n=== 设置end关键字参数 ===')
# HelloWorld
print('Hello', end='')
print('World')

# 向print函数传入多个字符串
print('\n=== 向print函数传入多个字符串 ===')
print('a', 'b', 'c') # a b c
print('a', 'b', 'c', sep=', ') # a, b, c


## 局部和全局作用域
# 局部作用域：
def spam():
    eggs = 1
    print("eggs=" + str(eggs))
spam()

# 全局作用域：
print("=== 在一个函数内部修改全局变量 === ")
def spam2():
    global apples
    apples = 'giveByLocalScope'
apples = 'giveByGlobalScope'
spam2()
print(apples) # giveByLocalScope

# 异常处理
print('\n=== 异常处理 ===')
def handleExp(operator):
    try:
        return 42 / operator
    except ZeroDivisionError:
        print(str(operator) + '， 导致0除异常')
        return None

print(handleExp(1))
print(handleExp(2))
# 0除异常
print(handleExp(0))
print(handleExp(3))

