# -*- coding:utf-8 -*-
# @Time    : 2018/12/28 21:33
# @Author  : totoo


# 正则表达式--完成字符串的查找

import re




#
# s1 = 'world hello'
# pattern = 'hello'  # 全文匹配的正则表达式
# re1=re.match(pattern=pattern,string=s1) # match,只从目标字符串起始位置去找
# re2=re.findall(pattern=pattern,string=s1)  # findall, 找到所有位置，返回列表
# re3 = re.search(pattern=pattern,string=s1)   # 从人任意位置开始找
# print(re1)
# print(re2)
# print(re3)

# 正则中的分组
# url = 'www.baidu,.com'
# p = '(w)(ww)'
# m = re.search(p,url)
# print(m.group())   # 全匹配
# print(m.group(1))  # 拿到第一个分组
# print(m.group(2))  # 拿到第二个分组





s='{"mobilephone":"${normal_user}","pwd":"${pwd}"}' # 目标字符串,包含参数化

# re4=re.findall(pattern='\$\{(.*?)\}',string=s) # 查找到要替换的参数, 万能匹配正则表达式
# print(re4)
# ss=re.sub('\$\{(.*?)\}','4567',s)  # 替换目标字符串
# print(ss)


p = '\$\{(.*?)\}'

while re.search(p,s):  # 一次匹配并且替换参数化
    m = re.search(p,s)
    # print(m.group())
    # print(m.group(1))
    key = m.group(1)
    from common.basic_data import Context
    user = getattr(Context,key)
    # print(user)
    s=re.sub(p,user,s,count=1)
print(s)


