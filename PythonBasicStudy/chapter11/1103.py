# 定义函数，使用断言做判断
# （在生产环境中不要参考该代码，仅做测试，因为运行时的程序不应该使用断言，而在程序或应用启动时可以使用）
# def callPhoneWithAssert(phoneNumber):
#     assert len(phoneNumber) == 11, phoneNumber + 'is not a valid phone number'
#     print('Calling Phone Number:', phoneNumber)
#
# # 调用函数
# callPhoneWithAssert('110')


import logging

# 设置日志格式
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
# 禁用 ERROR 及以下日志的写法
logging.disable(logging.ERROR)
def callPhoneWithLogging(phoneNumber):
    logging.debug('calling callPhoneWithLogging() , phoneNumber:%s', phoneNumber)
    logging.info('calling callPhoneWithLogging() , phoneNumber:%s', phoneNumber)
    logging.warning('calling callPhoneWithLogging() , phoneNumber:%s', phoneNumber)
    logging.error('calling callPhoneWithLogging() , phoneNumber:%s', phoneNumber)
    logging.critical('calling callPhoneWithLogging() , phoneNumber:%s', phoneNumber)
    if (len(phoneNumber) != 11):
        logging.error('%s is not a valid phone number', phoneNumber)
    print('Calling Phone Number:', phoneNumber)

# 调用函数，打印日志
callPhoneWithLogging('110')

logging.basicConfig(filename="diyLog.txt", level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')