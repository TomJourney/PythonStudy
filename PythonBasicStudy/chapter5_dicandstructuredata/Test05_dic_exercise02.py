
# 字典练习题  国际象棋字典验证器

stuff = {'zhangsan' : 3, 'lisi' : 4 , 'wangwu' : 5, 'zhaoliu' : 6}
def displayInventory(inventory):
    print('Inventory:')
    itemTotal = 0
    for k, v in inventory.items():
        itemTotal += v
    print('total number of items:' + str(itemTotal))

displayInventory(stuff)

# 添加物品到清单
print('添加物品到清单')
stuff = {'zhangsan' : 3, 'lisi' : 4 , 'wangwu' : 5, 'zhaoliu' : 6}

def addToInventory(inventory, k, v):
    inventory[k] = v
addToInventory(stuff, 'tianqi', 7)
print(stuff)
