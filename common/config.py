# -*- coding:utf-8 -*-
# @Time    : 2018/12/24 22:10
# @Author  : totoo
# 配置文件读取
import configparser
from common import constants
import os

# 创建实例
# 加载配置文件
# 根据 section option 取到配置项的值


class ConfigLoader:

    def __init__(self):
        # 创建实例
        self.conf = configparser.ConfigParser()
        # 加载配置文件
        file_name = constants.configs_dir_global
        self.conf.read(filenames=file_name, encoding="utf-8")
        if self.conf.getboolean("switch","on"):  # 返回布尔值
            online = constants.configs_dir_online
            self.conf.read(filenames=online, encoding="utf-8")
        else:
            test = constants.configs_dir_test
            self.conf.read(filenames=test, encoding="utf-8")

    def get_conf_str(self,section,option): # 返回str类型的值
        return self.conf.get(section,option)

    def get_conf_boolean(self,section,option): # 返回布尔值类型的值
        return self.conf.getboolean(section,option)

    def get_conf_int(self,section,option):  # 返回int类型的值
        return self.conf.getint(section,option)

    def get_conf_float(self,section,option):  # 返回float类型的值
        return self.conf.getfloat(section,option)


if __name__ == '__main__':
    config1=ConfigLoader()
    url1=config1.get_conf_str("basic","pwd")
    print(url1)
