# coding: utf-8
"""
平台相关Model
"""

from models import db
from utils.util import Util
import uuid

platform_col  = db["platforms"]
test_col = db["tests"]

class PlatformModel(object):
    '应用Model'
    def __init__(self):
        pass
    
    @classmethod
    def insert_platform(cls, p_name, p_logo, p_type, **kargs):
        """
        添加应用
        """
        data = platform_col.find({
            "p_name": p_name
        })
        if data.count() != 0:
            return -1001
        else:
            platform_col.insert({
                "_id": str(uuid.uuid1()),
                "p_name": p_name,
                "p_logo": p_logo,
                "p_type": p_type,
                "create_time": Util.timeFormat(),
                "deleted": 0
            })
            return 1

    @classmethod
    def update_platform(cls, _id, p_name, p_logo, p_type, **kargs):
        """
        更新应用
        """
        try:
            # 除当前修改的名称以外，是否还存在要修改的名称
            data = platform_col.find({
                "p_name": p_name,
                "_id": {
                    "$ne": _id
                }
            })
            if data.count() != 0:
                return -1001
            else:
                data = platform_col.update({
                    "_id": _id
                },
                {
                    "$set": {
                        "p_name": p_name,
                        "p_logo": p_logo,
                        "p_type": p_type,
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
    def get_list(cls):
        try:
            data = platform_col.find({
                "deleted": 0
            })
            results = []
            for item in data:
                print(item["_id"])
                results.append({
                    "p_id": item["_id"],
                    "p_name": item["p_name"],
                    "p_logo": item["p_logo"],
                    "p_type": item["p_type"],
                    "tests_num": test_col.find({"p_id": item["_id"]}).count()
                })
            return results
        except Exception as e:
            print(e)
            return []

    @classmethod
    def delete_platform(cls, p_id):
        """
        软删除应用
        """
        try:
            data = platform_col.update({
                "_id": p_id
            },{
                "$set": {
                    "deleted": 1
                }
            })
            if data["ok"] == 1:
                return 1
            else:
                return 0
        except Exception as e: 
            print(e)
            return -1