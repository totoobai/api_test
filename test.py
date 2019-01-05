# -*- coding:utf-8 -*-
# @Time    : 2019/1/5 12:08
# @Author  : totoo

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
mysql = MysqlUtil()
select_loan = 'select * from future.loan where memberId = {0} order by createtime desc limit 1'.format(Context.loan_member_id)
loan = mysql.fetch_one(select_loan)
print(loan.decode('UTF-8').encode('GBK')['Title'])
