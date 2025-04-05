import csv
from pathlib import Path

csvFileA01 = open(Path.cwd() / '1601A01.csv')
csvFileA01Reader = csv.reader(csvFileA01)
print(list(csvFileA01Reader))
# [['id', 'name', 'addr'], ['1', '张三01', '成都01'], ['2', '张三02', '成都02'], ['3', '张三03', '成都03']]
csvFileA01.close()

# 遍历每行
print("====== 遍历每行 ======")
csvFileA01 = open(Path.cwd() / '1601A01.csv')
reader01 = csv.reader(csvFileA01)
for row in reader01:
    print(f"row[%d]=%s" % (reader01.line_num, str(row)))
csvFileA01.close()
# ====== 遍历每行 ======
# row[1]=['id', 'name', 'addr']
# row[2]=['1', '张三01', '成都01']
# row[3]=['2', '张三02', '成都02']
# row[4]=['3', '张三03', '成都03']

# 16.1.3 writer对象写入数据到csv文件
print("\n====== writer对象写入数据到csv文件 ======")
csvFileA01 = open(Path.cwd() / '1601A01.csv', "w", newline='')
writer01 = csv.writer(csvFileA01)
writer01.writerow(['4', '张三04', '成都04'])
writer01.writerows([['5', '张三05', '成都05'], ['6', '张三06', '成都06']])
csvFileA01.close()

# 16.1.5 DictReader 和 DictWriter的csv对象
print("\n====== 使用DictReader读取csv对象 ======")
csvFileA01 = open(Path.cwd() / '1601A01.csv', "r")
tempDictReader = csv.DictReader(csvFileA01, ['id', 'name', 'addr'])
for row in tempDictReader:
    print(str(row['id']), str(row['name']), str(row['addr']), end=' ')
    print()
csvFileA01.close()


# ====== 使用DictReader读取csv对象 ======
# 4 张三04 成都04
# 5 张三05 成都05
# 6 张三06 成都06


print("\n====== 使用DictWriter保存数据到csv对象 ======")
csvFileA01 = open(Path.cwd() / '1601A01.csv', "w", newline='')
tempDictWriter = csv.DictWriter(csvFileA01, ['id', 'name', 'addr'])
# 写入标题行
tempDictWriter.writeheader()
# 写入字典数据
tempDictWriter.writerow({'id':'101', 'name':'张三101', 'addr':'成都101'})
csvFileA01.close()


