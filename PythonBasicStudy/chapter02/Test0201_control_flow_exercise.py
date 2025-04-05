# python控制流练习题

import random, sys

print('rock-石头，scissors-剪刀，  paper-布')
wins = 0
losses = 0
ties = 0
while True:
    print('wins=%s, losses=%s, ties=%s' % (wins, losses, ties))
    while True:
        print('type your manCommand: r-rock-石头， s-scissors-剪刀, p-paper-布, q-quit-退出')
        manCommand = input()
        if manCommand == 'q':
            sys.exit()
        if manCommand == 'r' or manCommand == 'p' or manCommand == 's':
            break
        print('4 types of manCommand: r, s, p, or q')

    # 演示人工的选择
    if manCommand == 'r':
        print('human: rock versus')
    elif manCommand == 's':
        print('human: scissors versus')
    elif manCommand == 'p':
        print('human: paper versus')

    # 演示计算机随机的选择
    randomNumber = random.randint(1, 3)
    if randomNumber == 1:
        computerCommand = 'r'
        print("computer: rock-石头")
    elif randomNumber == 2:
        computerCommand = 's'
        print("computer: scissors-剪刀")
    elif randomNumber == 3:
        computerCommand = '【'
        print("computer: paper-布")
    
    # 判断人工与计算机输赢
    if manCommand == computerCommand:
        print('tie!')
        ties += 1
    elif manCommand == 'r' and computerCommand == 's':
        print('man win!')
        wins += 1
    elif manCommand == 'p' and computerCommand == 'r':
        print('man win!')
        wins += 1
    elif manCommand == 's' and computerCommand == 'p':
        print('man win!')
        wins += 1
    elif manCommand == 'r' and computerCommand == 'p':
        print('man lose!')
        losses += 1
    elif manCommand == 'p' and computerCommand == 's':
        print('man lose!')
        losses += 1
    elif manCommand == 's' and computerCommand == 'r':
        print('man lose!')
        losses += 1
