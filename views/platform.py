# coding: utf-8

"""
应用相关
:author: huiwenhua
:date: 2019-09-02
"""

from flask import Blueprint
from utils.json_response import JsonResponse

platform_view = Blueprint('platform_view', __name__, url_prefix='/platform')

@platform_view.route("/list", methods=["GET"])
def get_platforms():
    """
    获取应用列表
    """
    try:
        data = []
        return JsonResponse.response(data=data)
    except Exception as e:
        return JsonResponse.response(code=0,message="系统内部错误")

@platform_view.route("/insert", methods=["POST"])
def add_platfrom():
    """
    创建应用
    """
    try:
        data = []
        return JsonResponse.response()
    except Exception as e:
        return JsonResponse.response(code=0,message="系统内部错误")

@platform_view.route("/update",methods=["POST"])
def update_info():
    """
    更新应用
    """
    try:
        data = []
        return JsonResponse.response(data=data)
    except Exception as e:
        return JsonResponse.response(code=0,message="系统内部错误")