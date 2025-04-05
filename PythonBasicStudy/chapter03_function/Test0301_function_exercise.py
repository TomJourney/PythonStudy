import time, sys

indent = 0 # 缩进空格数量
indentIncreasing = True # 是否增加缩进空格数量
try:
    while True:
        print(' ' * indent, end='')
        print('********')
        time.sleep(0.1)

        if indentIncreasing:
            indent += 1
            if indent == 10:
                indentIncreasing = False
        else:
            indent -= 1
            if indent == 0:
                indentIncreasing = True
except KeyboardInterrupt:
    sys.exit()
