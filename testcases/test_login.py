# -*- coding:utf-8 -*-
# @Time    : 2018/12/26 22:04
# @Author  : totoo

# 测试登陆

import unittest
from common.do_excel import DoExcel
from common.config import constants
from common.request import Request
import json
from ddt import ddt,data,unpack,file_data
from datas.mysql_util import MysqlUtil

do_excel = DoExcel(constants.case_file)  # 实例化一个DoExcel对象
cases=do_excel.get_cases("login")  #返回case列表

@ddt
class TestLogin(unittest.TestCase):

    def setUp(self):
        pass

    @data(*cases)
    def test_login(self,case):
        data=json.loads(case.data)
        resp = Request(method=case.method, url=case.url, data=data)  # 通过封装的Request类来完成接口的调用
        print('test data:',data)
        print('status_code:', resp.get_status_code())  # 打印响应码
        resp_dict = resp.get_json()  # 获取请求响应，字典
        self.assertEqual(case.expected,resp.get_json_code())


    def tearDown(self):
        print("test reset")