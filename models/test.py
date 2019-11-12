# coding: utf-8

"""
实验MOdel
:author: huiwenhua
:date: 2019-09-04
"""

from flask import current_app
from models import db
import uuid
from utils.util import Util
from models.log import LogModel

test_col = db["tests"]
bucket_col = db["buckets"]

class TestsModel(object):
    '实验Model类'
    def __init__(self):
        pass

    @classmethod
    def get_tests(cls, p_id):
        """
        获取实验
        """
        try:
            data = test_col.find({
                "p_id": p_id
            })
            results = []
            for item in data:
                results.append({
                    "t_id": item["_id"],
                    "t_name": item["t_name"],
                    "t_desc": item["t_desc"],
                    "t_str": item["t_str"],
                    "t_status": item["t_status"],
                    "bucket_num": bucket_col.find({"t_id": item["_id"]}).count()
                })
            return results
        except Exception as e:
            current_app.logger.error(e)
            return []


    @classmethod
    def add_test(cls, p_id, t_name, t_str, t_desc, user_id):
        """
        创建实验
        """
        try:
            data = test_col.find({
                "p_id": p_id,
                "t_name": t_name
            })
            data_len = len(list(data))
            if data_len != 0:
                return -2001
            else:
                t_id = str(uuid.uuid1())
                test_col.insert({
                    "_id": t_id,
                    "p_id": p_id,
                    "t_name": t_name,
                    "t_str": t_str,
                    "t_desc": t_desc,
                    "t_status": 1,
                    "create_time": Util.timeFormat(),
                    "creator_id": user_id
                })
                log_str = "实验名称：{}；实验ID：{}；实验描述：{}；加盐字符：{}".format(t_name, t_id, t_desc, t_str)
                log_result = LogModel.add_log("创建实验", log_str, user_id, "insert")
                return 1
        except Exception as e:
            current_app.logger.error(e)
            return 0

    @classmethod
    def update_test_info(cls, p_id, t_id, t_name, t_str, t_desc, user_id):
        """
        修改实验信息
        """
        try:
            data = test_col.find({
                "p_id": p_id,
                "t_name": t_name,
                
            })
            test_col.update({
                    "p_id": p_id,
                    "_id": t_id,
                    "t_id": {
                        "$ne": t_id
                    }
                },
                {
                    "$set": {
                        "t_name": t_name,
                        "t_str": t_str,
                        "t_desc": t_desc,
                        "update_time": Util.timeFormat()
                    }
                })
            log_str = "实验名称：{}；实验ID：{}；实验描述：{}；加盐字符：{}".format(t_name, t_id, t_desc, t_str)
            log_result = LogModel.add_log("修改实验", log_str, user_id, "update")
            return 1
        except Exception as e:
            current_app.logger.error(e)
            return 0

    @classmethod
    def toggle_status(cls, t_id, status, user_id):
        """
        改变实验状态
        """
        try:
            data = test_col.update(
                {
                    "_id": t_id
                },
                {
                    "$set": {
                        "t_status": int(status),
                        "update_time": Util.timeFormat()
                    }
            })
            if data["ok"] == 1:
                test_status = "启用" if int(status) == 1 else "停用"
                log_str = "实验ID：{}；状态：{}".format(t_id, int(status))
                log_result = LogModel.add_log("启用/停用实验", log_str, user_id, "update")
                return 1
            else:
                return 0
        except Exception as e:
            current_app.logger.error(e)
            return 0

    @classmethod
    def search(cls, p_id, search):
        """
        实验Id/实验名称模糊查询
        """
        try:
            data = test_col.find({
                "p_id": p_id,
                "$or": [
                    {
                        "_id": {
                            "$regex": search
                        }
                    },
                    {
                        "t_name": {
                            "$regex": search
                        }
                    }
                ]
            })
            results = []
            for item in data:
                results.append({
                    "t_id": item["_id"],
                    "t_name": item["t_name"],
                    "t_desc": item["t_desc"],
                    "t_str": item["t_str"],
                    "t_status": item["t_status"],
                    "bucket_num": bucket_col.find({"t_id": item["_id"]}).count()
                })
            return results
            return []
        except Exception as e:
            current_app.logger.error(e)
            return []

    @classmethod
    def get_str_by_id(cls, test_id):
        """根据实验ID获取加盐字符
        :param test_id: 实验ID
        """
        try:
            data = test_col.find_one({
                "_id": test_id
            })

            # 实验不存在
            if not data:
                result = {
                    "code": -1001,
                    "message": "实验不存在"
                }
                return result

            # 实验已停用
            if data.get("t_status") == 0:
                result = {
                    "code": -1002,
                    "message": "实验已停用"
                }
                return result

            if not data.get("t_str") is None:
                result = {
                    "code": 1,
                    "message": "成功",
                    "data": data.get("t_str")
                }
                return result
            else:
                result = {
                    "code": -1004,
                    "message": "获取加盐字符失败"
                }
                return result
        except Exception as e:
            current_app.logger.error(e)
            result = {
                "code": -1,
                "message": "系统内部错误"
            }
            return result