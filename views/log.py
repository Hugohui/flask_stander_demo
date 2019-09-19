# coding: utf-8

"""日志相关
:author: huiwenhua
:date: 2019-09-10
:desc: Happy teacher's day!
"""

from flask import Blueprint, request, current_app
from models.log import LogModel
from utils.json_response import JsonResponse

log_view = Blueprint("log_view", __name__, url_prefix="/log")

@log_view.route("/record", methods=["GET"])
def get_record():
    """获取操作日志
    """
    try:
        user_id = request.args.get("user_id")
        page = request.args.get("page", '1')
        if not user_id:
            return JsonResponse.response(code=-1000)
        result = LogModel.get_list(user_id, int(page))
        return JsonResponse.response(data=result)
    except Exception as e:
        current_app.logger.error(e)
        return JsonResponse.response(code=-1)
