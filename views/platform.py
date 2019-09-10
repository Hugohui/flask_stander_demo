# coding: utf-8

"""
应用相关
:author: huiwenhua
:date: 2019-09-02
"""

from flask import Blueprint, request
from utils.json_response import JsonResponse
from models.platform import PlatformModel
import json
from utils.util import Util

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
        return JsonResponse.response(code=-1)

@platform_view.route("/update", methods=["POST"])
def add_platfrom():
    """
    创建/修改应用
    """
    try:
        _id = Util.form_or_json().get('p_id')
        p_name = Util.form_or_json().get('p_name')
        p_logo = Util.form_or_json().get('p_logo')
        p_type = Util.form_or_json().get('p_type')
        user_id = Util.form_or_json().get('user_id')
        if not p_name or not p_type or not p_logo:
            return JsonResponse.response(code=0, message="参数错误")
        if _id:
            result = PlatformModel.update_platform(_id, p_name, p_logo, p_type, user_id)
        else:
            result = PlatformModel.insert_platform(p_name, p_logo, p_type, user_id)
        return JsonResponse.response(code=result,data=None)
    except Exception as e:
        print(e)
        return JsonResponse.response(code=-1)

@platform_view.route("/delete", methods=["POST"])
def delete_platform():
    """
    删除应用
    """
    try:
        p_id = Util.form_or_json().get("p_id")
        user_id = Util.form_or_json().get("user_id")
        if not p_id:
            return JsonResponse.response(code=-1000)
        else:
            result = PlatformModel.delete_platform(p_id, user_id)
            return JsonResponse.response(code=result)
    except Exception as e:
        print(e)
        return JsonResponse.response(code=-1)
