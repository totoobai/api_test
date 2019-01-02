# -*- coding:utf-8 -*-
# @Time    : 2019/1/2 21:06
# @Author  : totoo

import unittest
from common.do_excel import DoExcel
from common.config import constants
from common.request import Request
import json
from ddt import ddt,data,unpack,file_data
from datas.mysql_util import MysqlUtil

do_excel = DoExcel(constants.case_file)  # 实例化一个DoExcel对象
cases = do_excel.get_cases("register")  #返回case列表

@ddt
class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global mysql
        mysql = MysqlUtil()
        sql = "SELECT MobilePhone from future.member where MobilePhone!='' ORDER BY MobilePhone DESC LIMIT 1"

        global max_phone
        max_phone = int(mysql.fetch_one(sql)['MobilePhone'])

    # def setUp(self):
    #     print("=" * 100)
    #     # 查询最大手机号
    #     self.mysql = MysqlUtil()
    #     self.sql = "SELECT MobilePhone from future.member where MobilePhone!='' ORDER BY MobilePhone DESC LIMIT 1"
    #     self.max_phone = int(self.mysql.fetch_one(self.sql)['MobilePhone'])

    @data(*cases)
    def test_login(self,case):
        data=json.loads(case.data)  # 对取到的data做序列化
        if data['mobilephone']=='${register}':
            data['mobilephone']=max_phone-90000
        resp = Request(method=case.method, url=case.url, data=data)  # 通过封装的Request类来完成接口的调用
        print('test data:',data)
        print('status_code:', resp.get_status_code())  # 打印响应码
        resp_dict = resp.get_json()  # 获取请求响应，字典
        self.assertEqual(case.expected,resp.get_json_code())

        # 注册成功，在数据库校验是否有这条数据
        if resp.get_status_code() == "20010":
            sql='select * from future.member where MobilePhone = "{0}"'.format(max_phone-90000)
            expected = max_phone-90000
            member=mysql.fetch_one(sql)
            if member is not None:
                self.assertEqual(expected,member["MobilePhone"])
            else:
                raise AssertionError
        else:
            print("注册失败！")
    # def tearDown(self):
    #     self.mysql.mysql.close()
    #     print("=" * 100)

    @classmethod
    def tearDownClass(cls):
        mysql.mysql.close()
        print("=" * 100)