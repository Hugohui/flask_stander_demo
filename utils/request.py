# coding:utf-8

"""
request请求类
:author: huiwenhua
:date: 2019-09-02
"""

import requests

class Request():
    'Request 类'

    def __init__(self):
        pass

    @classmethod
    def get(cls, url, params={}, headers={}):
        """
        get 请求
        """
        try:
            r = requests.get(url, params=params, headers=headers)
            json_r = r.json()
            return json_r
        except Exception as e:
            print("请求失败",str(e))

    @classmethod
    def post(cls, url, params={}, headers={}):
        try:
            r = requests.post(url, data=params, headers=headers)
            json_r = r.json()
            return json_r
        except BaseException as e:
            print("请求失败！", str(e))