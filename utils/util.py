# coding:utf-8

"""
工具类
:author: huiwenhua
:date: 2019-09-02
"""

from datetime import datetime
from flask import request
import hashlib

class Util(object):
    '工具类'

    def __init__(self):
        pass

    @classmethod
    def timeFormat(cls,formStr="%Y-%m-%d %H:%M:%S"):
        """时间格式化
        """
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

    @classmethod
    def id_md5(cls, id, md5_str="", bucket_num=100):
        """ID加盐取模
        :param id: device_id or user_id
        :param str: 加盐字符串
        :return: 取模的结果
        """
        md5_int = int(hashlib.md5((str(id)+md5_str).encode("utf-8")).hexdigest(), 16)
        result = md5_int % bucket_num
        return int(result)