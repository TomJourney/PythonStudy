
# 定义函数，抛出异常
def callPhone(phoneNumber):
    if phoneNumber == '110':
        raise Exception("110不是合法电话号码")
    elif phoneNumber == '120':
        raise Exception("120不是合法电话号码")
    print('Calling Phone Number:', phoneNumber)

def iphone(phoneNumber):
    try:
        callPhone(phoneNumber)
    except Exception as error:
        print("exception happened: " + str(error))

# 调用函数
iphone("110")
iphone("120")
iphone("130")

# exception happened: 110不是合法电话号码
# exception happened: 120不是合法电话号码
# Calling Phone Number: 130