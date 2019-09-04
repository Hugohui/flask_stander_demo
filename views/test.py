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


@test_view.route("/update", methods=["POST"])
def add_test():
    """
    创建/修改实验
    """
    try:
        p_id = request.values.get("p_id")
        t_id = request.values.get("t_id")
        t_name = request.values.get("t_name")
        t_str = request.values.get("t_str")
        t_desc = request.values.get("t_desc")
        print(t_id)
        if t_id:
            result = TestsModel.update_test_info(p_id, t_id, t_name, t_str, t_desc)
        else:
            result = TestsModel.add_test(p_id, t_name, t_str, t_desc)
        return JsonResponse.response(code=result)
    except Exception as e:
        print(e)
        return JsonResponse.response(code=0, message="系统内部错误")

@test_view.route("/toggle_status", methods=["POST"])
def toggle_status():
    """
    修改实验状态
    """
    try:
        t_id = request.values.get("t_id")
        t_status = request.values.get("t_status")
        result = TestsModel.toggle_status(t_id, t_status)
        return JsonResponse.response(code=result)
    except Exception as e:
        print(e)
        return JsonResponse.response(code=0, message="系统内部错误")