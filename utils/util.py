# coding:utf-8

"""
工具类
:author: huiwenhua
:date: 2019-09-02
"""

from datetime import datetime

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