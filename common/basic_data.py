# -*- coding:utf-8 -*-
# @Time    : 2018/12/28 23:03
# @Author  : totoo

# 测试上下文
# 反射机制：提供一些方法，在没有实例化对象的时候，获取对象信息，甚至更改对象

import re
from common.config import ConfigLoader

class Context:
    config=ConfigLoader()
    normal_user = config.get_conf_str('basic','normal_user') # 类变量
    pwd = config.get_conf_str('basic','pwd')

# 正则匹配的方法
class DoRegex:
    @staticmethod
    def replace(target):   # 查找并且替换参数
        pattern='\$\{(.*?)\}'
        while re.search(pattern, target):  # 一次匹配并且替换参数化
            m = re.search(pattern,target)
            key = m.group(1)
            from common.basic_data import Context
            user = getattr(Context, key)
            target = re.sub(pattern, user, target, count=1)
        return target



if __name__ == '__main__':
    x = Context(123, 33)
    # x.normal_user
    # a = getattr(Context,'normal_user')  # 获取类中属性的值
    # print(a)
    #
    # setattr(Context,'admin_user','admin') # 增加属性值
    # print(x.admin_user)
    # if hasattr(Context,'pwd'): # 判断是否有属性值
    #     delattr(Context,'pwd') # 删除成员变量
    #     print(x.pwd)
    # else:
    #     print("has no attribute")

    print(getattr(x, "a"))