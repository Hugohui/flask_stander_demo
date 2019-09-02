# coding:utf-8

"""
格式化返回值
:author: huiwenhua
:date: 2019-09-02
"""

from flask import jsonify

class JsonResponse(object):
    'json response 类'
    code_dict = {
        0: [200, "失败"],
        1: [200, "成功"]
    }

    def __init__(self):
        pass

    @classmethod
    def response(cls, code=1, message="", data=None, **kwargs):
        """
        response封装
        :param code: 标识码
        :param message: 返回信息
        :param data: 返回数据
        :param kwargs: 其他参数
        :return: josn化格式
        """

        res = dict()
        
        res["code"] = code
        
        http_status = cls.code_dict.get(code, [200, ""])[0]

        if message:
            res["message"] = message
        else:
            res["message"] = cls.code_dict.get(code, [200, ""])[1]
        
        if data or data == []:
            res["data"] = data
        else:
            res["data"] = []

        return jsonify(res), http_status