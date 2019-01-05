# -*- coding:utf-8 -*-
# @Time    : 2019/1/5 13:02
# @Author  : totoo

# 复习logging的基本使用
"""
步骤：
1、定义一个日志收集器
2、设定日志处理的级别 debug info warning error critical
3、设置日志格式
4、指定输出渠道 console file
5、收集日志
6、关闭渠道
"""
"""
INFO：记录测试运行一些状态，用例名称、用例数据、用例结果、SQL -----输出info.log 文件
DEBUG：记录运行过程
ERROR：记录异常信息

"""




import logging
from common import constants

# 收集日志
my_logger = logging.getLogger("totoo")  # 创建一个日志收集器
my_logger.setLevel("DEBUG")  # 设置基础级别 只有级别大于或等于该基础级别的，才会被输出，小于该级别的日志记录会被丢弃

# 指定输出格式，可以自己扩展
formatter = logging.Formatter("%(asctime)s-%(levelname)s-%(filename)s-%(name)s-日志信息：%(message)s")

# 指定输出的渠道
console = logging.StreamHandler()  # 输出到控制台
console.setLevel("INFO")
console.setFormatter(formatter)

# 添加日志到本地文件
file = logging.FileHandler(filename=constants.logs_file, encoding="utf-8")
file.setLevel("DEBUG")
file.setFormatter(formatter)

# 添加输出渠道到日志收集器
my_logger.addHandler(console)
my_logger.addHandler(file)

my_logger.debug("this is debug log!")  # 默认输出warming以上的信息
my_logger.info("this is info log!")
my_logger.warning("this is warning log!")
my_logger.error("this is error log!")
my_logger.critical("this is critical log!")