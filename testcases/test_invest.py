# -*- coding:utf-8 -*-
# @Time    : 2019/1/5 9:50
# @Author  : totoo
# encoding=utf-8

# 测试投资接口
# 步骤：管理员登陆--》管理员增加标的--》借款人加标--》投资人投标

# 增加其他表数据校验


import unittest
from common.do_excel import DoExcel
from common.config import constants
from common.request import Request
from common.basic_data import DoRegex,Context
import json
from ddt import ddt,data,unpack,file_data
from datas.mysql_util import MysqlUtil

do_excel = DoExcel(constants.case_file)  # 实例化一个DoExcel对象
cases = do_excel.get_cases("invest")  #返回case列表

@ddt
class InvestTest(unittest.TestCase):

    def setUp(self):
        self.mysql = MysqlUtil()
        # 投资前账户余额
        self.select_member = 'select * from future.member where mobilephone = {0}'.format(Context.normal_user)
        self.before_amount = self.mysql.fetch_one(self.select_member)['LeaveAmount']
        # 自己去添加
        pass

    @data(*cases)
    def test_invest(self, case):
        # 参数化处理
        data = DoRegex.replace(case.data)
        # 将测试数据由字符串序列化成字典
        data = json.loads(data,encoding="UTF-8")
        print("Test data:{}".format(data))
        if hasattr(Context, 'cookies'):  # 判断是否有cookies
            cookies = getattr(Context, 'cookies')  # 获取放到上下文里面的cookies
        else:
            cookies = None
        # 通过封装的Request类来完成接口的调用
        resp = Request(method=case.method, url=case.url, data=data, cookies=cookies)
        print(resp.get_text())
        resp_dict = resp.get_json()  # 获取请求响应，字典
        # 优先判断响应返回的code 是否与期望结果一致
        self.assertEqual(case.expected, int(resp_dict['code']))


        # 判断有没有cookie
        if resp.get_cookies():  # 判断返回里面是否有cookies
            setattr(Context, 'cookies', resp.get_cookies())  # 放入到上下文中


        # 当创建标的成功时，根据借款人ID查看数据库loan表是否与添加数据
        if resp_dict['msg'] == '加标成功':
            select_loan = 'select * from future.loan where memberId = {0} order by createtime desc limit 1'.format(Context.loan_member_id)
            loan = self.mysql.fetch_one(select_loan)
            if loan is not None:  # 如果从数据库里面查询出来不是空，则创建标的成功
                # 判断数据库里面的标的详情是否与测试数据一致,可以优化
                # self.assertEqual(float(data['amount']), float(loan['Amount']))  # 多个字段一致才assert通过
                # # self.assertEqual(data['title'], str(loan['Title']))
                # self.assertEqual(int(data['loanRate']), int(loan['LoanRate']))
                # self.assertEqual(data['loanTerm'], loan['LoanTerm'])
                # self.assertEqual(data['loanDateType'], loan['LoanDateType'])
                # self.assertEqual(data['repaymemtWay'], loan['RepaymemtWay'])
                # self.assertEqual(data['biddingDays'], loan['BiddingDays'])

                # self.assertDictEqual(data,loan)   # 断言优化
                # 将创建成功的标的ID写入到上下文中，用于之后投资用
                setattr(Context, 'loan_id', str(loan['Id']))  # 放一个str类型的进去，以备后面正则替换
            else:
                raise AssertionError  # 如果数据库里面没有数据，就测试失败


        # 当审核成功，需校验数据库loan表中status字段更改，自己添加
        if resp_dict['msg'] == '成功':
            select_status="select * from future.loan where loan_id={0}".format(Context.loan_id)
            loan_status=self.mysql.fetch_one(select_status)
            self.assertEqual(data['status'],loan_status['status'])



        # 当投资成功时，根据投资人ID查看数据member表中验证余额是否减少
        if resp_dict['msg'] == '竞标成功':
            amount = data['amount']  # 投资金额
            actual = self.mysql.fetch_one(self.select_member)['LeaveAmount']  # 投资后的金额
            expect = float(self.before_amount) - float(amount)  # 期望 = 投资前的余额 - 投资金额
            self.assertEqual(str(expect), str(actual))
        elif resp_dict['code'] != '10001':  # 投资失败，余额不变
            actual = self.mysql.fetch_one(self.select_member)['LeaveAmount'] # 投资后的金额
            expect = float(self.before_amount)  # 期望 = 投资前的余额
            self.assertEqual(str(expect), str(actual))
        # else:
        #     raise AssertionError  # 如果数据库里面没有数据，就测试失败

    def tearDown(self):
        pass

