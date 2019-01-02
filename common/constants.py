# -*- coding:utf-8 -*-
# @Time    : 2018/12/24 22:14
# @Author  : totoo

# 常量管理，一般配置不会改变的值

import os

os.path.split(os.path.split(__file__)[0])[0]
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  #获取根目录的绝对路径
# print(base_dir)

configs_dir=os.path.join(base_dir,"configs")  # configs 文件夹路径
# print(configs_dir)

configs_dir_global=os.path.join(configs_dir,"global.conf")
# print(configs_dir_global)

configs_dir_online=os.path.join(configs_dir,"online.conf")
# print(configs_dir_online)

configs_dir_test=os.path.join(configs_dir,"test.conf")
# print(configs_dir_test)

datas_dir=os.path.join(base_dir,"datas")
case_file=os.path.join(datas_dir,"test_datas.xlsx") # test_datas.xlsx file path
 # print(datas_dir)

reports_dir=os.path.join(base_dir,"reports")
# print(reports_dir)

logs_dir=os.path.join(base_dir,"logs")
# print(logs_dir)