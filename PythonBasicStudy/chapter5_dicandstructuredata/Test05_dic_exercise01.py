
# 字典练习题
print("\n\n=== 字典练习题")
birthdays = {'zhangsan' : '2025-03-03', 'lisi' : '2025-04-04','wangwu' : '2025-05-05','zhaoliu' : '2025-06-06'}
while True:
    print("enter a name (blank to quit)")
    name = input()
    if name == '':
        break
    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)
    else:
        print('cannot find birthday of ' + name)
        print('please type your birthday')
        temp = input()
        birthdays[name] = temp
        print("your birthday is updated")
