# coding: utf-8

"""
应用相关
:author: huiwenhua
:date: 2019-09-02
"""

from flask import Blueprint, request
from utils.json_response import JsonResponse
from models.platform import PlatformModel

platform_view = Blueprint('platform_view', __name__, url_prefix='/platform')

@platform_view.route("/list", methods=["GET"])
def get_platforms():
    """
    获取应用列表
    """
    try:
        result = PlatformModel.get_list()
        return JsonResponse.response(data=result)
    except Exception as e:
        return JsonResponse.response(code=0,message="系统内部错误")

@platform_view.route("/insert", methods=["POST"])
def add_platfrom():
    """
    创建应用
    """
    try:
        p_name = request.values.get('p_name')
        p_logo = request.values.get('p_logo')
        p_type = request.values.get('p_type')
        result = PlatformModel.insert_platform(p_name, p_logo, p_type)
        return JsonResponse.response(code=result,data=None)
    except Exception as e:
        print(e)
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
        print(e)
        return JsonResponse.response(code=0,message="系统内部错误")