# -*- coding:utf-8 -*-
# @Time    : 2018/12/28 23:22
# @Author  : totoo
# 测试充值
# 配置文件设置基础登陆数据--》 通过context类获取 --》 regex正则匹配 --》 request发起请求 --》 context中添加cookie属性
# --》 进行recharge请求 --》 context中获取cookies--》 数据库校验（使用mysql模块）



import unittest
from common.do_excel import DoExcel
from common.config import constants
from common.request import Request
import json
from ddt import ddt,data,unpack,file_data
from common.basic_data import DoRegex
from common.basic_data import Context

do_excel = DoExcel(constants.case_file)  # 实例化一个DoExcel对象
cases=do_excel.get_cases("recharge")  #返回case列表

@ddt
class TestRecharge(unittest.TestCase):

    def setUp(self):
        print("-"*100)

    @data(*cases)
    def test_charge(self,case):
        # 对取到的数据，做参数化处理
        data = DoRegex.replace(case.data)
        data = json.loads(data)
        print("===test data===",data)
        if hasattr(Context,'cookies'):  # 通过上下文判断，来赋值cookies
            cookies=getattr(Context,'cookies')
        else:
            cookies = None
        resp = Request(method=case.method, url=case.url, data=data,cookies=cookies)  # 通过封装的Request类来完成接口的调用

        # 判断有没有cookie，如果有cookies（也就是在登陆的时候获取到了cookie），就给上下问context，增加一个cookies属性，
        # 将登陆获取到的cookies存储起来
        if resp.get_cookies():
            setattr(Context,'cookies',resp.get_cookies())

        print('status_code:', resp.get_status_code())  # 打印响应码
        resp_dict = resp.get_json()  # 获取请求响应，字典
        self.assertEqual(case.expected,resp.get_json_code())


    def tearDown(self):
        print("-"*100)