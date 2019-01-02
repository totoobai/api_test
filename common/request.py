# -*- coding:utf-8 -*-
# @Time    : 2018/12/17$
# @Author  : totoo

# 封装请求类，所有请求都通过这个类来调用
import requests
import json
from common.config import ConfigLoader

class Request:

    def __init__(self,method,url,data=None,cookies=None,headers=None):
        config1 = ConfigLoader()
        url_pre = config1.get_conf_str("api", "url_pre")
        url = url_pre+url
        try:
            if method=="get":
                self.resp=requests.get(url=url,params=data,cookies=cookies,headers=headers)
            elif method=="pose":
                self.resp=requests.post(url=url,data=data,cookies=cookies,headers=headers)
            elif method=="delete":
                self.resp=requests.delete(url=url,data=data,cookies=cookies,headers=headers)
        except Exception as e:
            raise e

    def get_status_code(self):
        return self.resp.status_code

    def get_text(self):
        return self.resp.text

    def get_json(self):
        json_dict = self.resp.json()
        # 通过json.dumps函数将字典转换成格式化后的字符串
        resp_text = json.dumps(json_dict, ensure_ascii=False, indent=4)
        print('response: ', resp_text)  # 打印响应
        return json_dict

    def get_json_code(self):
        return eval(self.resp.json()["code"])

    def get_cookies(self,key=None):
        if key is not None:
            return self.resp.cookies[key]
        else:
            return self.resp.cookies

if __name__ == '__main__':
    resq=requests.Request()

