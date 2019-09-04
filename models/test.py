# coding: utf-8
"""
实验MOdel
:author: huiwenhua
:date: 2019-09-04
"""

from models import db
import uuid
from utils.util import Util

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
            print(e)
            return []


    @classmethod
    def add_test(cls, p_id, t_name, t_str, t_desc):
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
                test_col.insert({
                    "_id": str(uuid.uuid1()),
                    "p_id": p_id,
                    "t_name": t_name,
                    "t_str": t_str,
                    "t_desc": t_desc,
                    "t_status": 1,
                    "create_time": Util.timeFormat()
                })
                return 1
        except Exception as e:
            print(e)
            return 0

    @classmethod
    def update_test_info(cls, p_id, t_id, t_name, t_str, t_desc):
        """
        修改实验信息
        """
        try:
            data = test_col.find({
                "p_id": p_id,
                "t_name": t_name,
                "t_id": {
                    "$ne": t_id
                }
            })
            if len(list(data)) != 0:
                return -2001
            else:
                print(t_name)
                test_col.update({
                    "p_id": p_id,
                    "_id": t_id
                },
                {
                    "$set": {
                        "t_name": t_name,
                        "t_str": t_str,
                        "t_desc": t_desc,
                        "update_time": Util.timeFormat()
                    }
                })
                return 1
        except Exception as e:
            print(e)
            return 0

    @classmethod
    def toggle_status(cls, t_id, status):
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
                return 1
            else:
                return 0
        except Exception as e:
            print(e)
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
            print(e)
            return []