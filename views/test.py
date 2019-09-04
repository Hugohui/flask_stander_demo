# coding: utf-8
"""
实验相关
:author: huiwenhua
:date: 2019-09-04
"""

from flask import Blueprint, request
from utils.json_response import JsonResponse
from models.test import TestsModel

test_view = Blueprint("test_view", __name__, url_prefix="/test")

@test_view.route("/list", methods=["GET"])
def get_tests():
    """
    获取实验列表
    """
    try:
        p_id = request.args.get("p_id")
        results = TestsModel.get_tests(p_id)
        return JsonResponse.response(data=results)
    except Exception as e:
        print(e)
        return JsonResponse.response(code=0, message="系统内部错误")


@test_view.route("/insert", methods=["POST"])
def add_test():
    """
    为应用创建实验
    """
    try:
        p_id = request.values.get("p_id")
        t_name = request.values.get("t_name")
        t_str = request.values.get("t_str")
        t_desc = request.values.get("t_desc")
        result = TestsModel.add_test(p_id, t_name, t_str, t_desc)
        return JsonResponse.response(code=result)
    except Exception as e:
        print(e)
        return JsonResponse.response(code=0, message="系统内部错误")

