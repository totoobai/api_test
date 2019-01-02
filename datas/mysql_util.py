# -*- coding:utf-8 -*-
# @Time    : 2018/12/26 23:22
# @Author  : totoo

# 数据库操作封装类
# 1、连接数据库
# 2、读取数据库数据，编写sql语句
# 3、建立游标
# 4、execute

import pymysql
from common.config import ConfigLoader

class MysqlUtil:

    def __init__(self):
        config=ConfigLoader()
        host=config.get_conf_str("mysql","host")
        port = config.get_conf_int("mysql", "port")
        user=config.get_conf_str("mysql","user")
        pwd=config.get_conf_str("mysql","pwd")
        # 异常处理
        try:
            self.mysql=pymysql.connect(host=host,user=user,password=pwd,database=None,
                                       port=port,cursorclass=pymysql.cursors.DictCursor) # 返回字典对象
        except Exception as e:
            print("Mysql connect failed!")

    def fetch_one(self,sql): # 查找一条数据，并返回
        cursor=self.mysql.cursor()
        cursor.execute(sql) # 根据sql进行查询
        return cursor.fetchone()   # 返回元祖
    
    def fetch_all(self,sql): # 查找多条 数据，并返回 元祖套元祖
        cursor=self.mysql.cursor()

        cursor.execute(sql) # 根据sql进行查询
        return cursor.fetchall()   # 元祖套元祖，多条数据用逗号隔开


if __name__ == '__main__':
    sql="SELECT MobilePhone from future.member where MobilePhone!='' ORDER BY MobilePhone DESC LIMIT 1"
    mysql=MysqlUtil()
    value=mysql.fetch_one(sql) # fetch匹配一个结果
    max_mobile=int(value['MobilePhone'])+1
    # print(max_mobile)
    print(value['MobilePhone']) # 元祖取值可读性差，不知道是哪一列

