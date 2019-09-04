# coding:utf-8

"""
工具类
:author: huiwenhua
:date: 2019-09-02
"""

from datetime import datetime
from flask import request

class Util(object):
    '工具类'

    def __init__(self):
        pass

    @classmethod
    def timeFormat(cls,formStr="%Y-%m-%d %H:%M:%S"):
        try:
            return datetime.now().strftime(formStr)
        except Exception as e:
            print(e)
            return datetime.now()

    @classmethod
    def form_or_json(cls):
        """
        获取request参数，json或者form
        """
        data = request.get_json(silent=True)
        return data if data is not None else request.values