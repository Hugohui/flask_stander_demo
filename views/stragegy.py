# coding: utf-8
"""
策略相关
:author: huiwenhua
:date: 2019-09-05
"""

from flask import Blueprint,request
from utils.util import Util
from utils.json_response import JsonResponse
from models.stragegy import StragegyModel

stragegy_view = Blueprint("stragegy_view", __name__, url_prefix="/stragegy")


@stragegy_view.route("/list", methods=["GET"])
def get_stragegy():
    """
    获取策略
    """
    try:
        t_id = request.args.get("t_id")
        if not t_id:
            return JsonResponse.response(code=-1000)
        result = StragegyModel.get_stragegy(t_id)
        return JsonResponse.response(data=result)
    except Exception as e:
        print(e)
        return JsonResponse.response(code=-1)


@stragegy_view.route("/pre_check", methods=["POST"])
def pre_check():
    """
    创建前检测是否存在
    """
    try:
        t_id = Util.form_or_json().get("t_id")
        s_name = Util.form_or_json().get("s_name")
        if not t_id or not s_name:
            return JsonResponse.response(-1000)
        result = StragegyModel.pre_check(t_id, s_name)
        if result == 1:
            return JsonResponse.response(code=result)
        else: 
            return JsonResponse.response(code=-3001,data=result)
    except Exception as e:
        print(e)
        return JsonResponse.response(code=-1)


@stragegy_view.route("/update", methods=["POST"])
def update_stragegy():
    """
    创建/更新策略
    """
    try:
        s_id = Util.form_or_json().get("s_id")
        b_id = Util.form_or_json().get("b_id")
        t_id = Util.form_or_json().get("t_id")
        s_name = Util.form_or_json().get("s_name")
        s_desc = Util.form_or_json().get("s_desc")
        section_min = Util.form_or_json().get("section_min")
        section_max = Util.form_or_json().get("section_max")

        if not t_id or not s_name or not s_desc or not section_min or not section_max or int(section_min) > int(section_max):
            return JsonResponse.response(code=-1000)
        if s_id and b_id:
            # 修改
            result = StragegyModel.update_stragegy(t_id, s_id, b_id, s_name, s_desc, section_min, section_max)
            return JsonResponse.response(code=result)
        else:
            # 新增
            result = StragegyModel.insert_stragegy(t_id, s_name, s_desc, section_min, section_max)
            return JsonResponse.response(code=result)
    except Exception as e:
        print(e)
        return JsonResponse.response(code=-1)

@stragegy_view.route("/delete", methods=["POST"])
def delete():
    """
    删除策略
    """
    try:
        b_id = Util.form_or_json().get("b_id")
        s_id = Util.form_or_json().get("s_id")
        if not b_id or not s_id:
            return JsonResponse.response(code=-1000)
        result = StragegyModel.delete(s_id, b_id)
        return JsonResponse.response(code=result)
    except Exception as e:
        print(e)
        return JsonResponse.response(code=-1)