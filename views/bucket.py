# coding: utf-8
"""
分桶策略相关
:author: huiwenhua
:date: 2019-09-05
"""

from flask import Blueprint
from utils.util import Util
from utils.json_response import JsonResponse

bucket_view = Blueprint("bucket_view", __name__, url_prefix="/bucket")

@bucket_view.route("/update", methods=["POST"])
def update_bucket():
    """
    创建/修改bucket
    """
    try:
        t_id = Util.form_or_json().get("t_id")
        b_id = Util.form_or_json().get("b_id")
        b_name = Util.form_or_json().get("b_name")
        b_desc = Util.form_or_json().get("b_desc")
        b_min = Util.form_or_json().get("b_section_min")
        b_max = Util.form_or_json().get("b_section_max")
        result = 1
        return JsonResponse.response(code=result)
    except Exception as e:
        print(e)
        return JsonResponse.response(code=-1)