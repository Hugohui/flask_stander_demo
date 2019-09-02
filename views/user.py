# coding:utf-8

"""
用户相关
:author: huiwenhua
:date: 2019-09-02
"""

from flask import Blueprint
from utils.json_response import JsonResponse

user_view = Blueprint("user_view", __name__, url_prefix="/user")

@user_view.route("/login", methods=["POST"])
def login():
    try:
        data = []
        return JsonResponse.response(data=data)
    except Exception as e:
        return JsonResponse.response(code=0, message="系统内部错误")
    