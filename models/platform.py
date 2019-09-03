# coding: utf-8
"""
平台相关Model
"""

from models import db
from utils.util import Util
import uuid

platform_col  = db["platforms"]

class PlatformModel(object):

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
                "create_time": Util.timeFormat()
            })
            return 1

    @classmethod
    def get_list(cls):
        try:
            data = platform_col.aggregate([
                {
                    "$lookup": {
                        "from": "tests",
                        "localField": "_id",
                        "foreignField": "p_id",
                        "as": "tests"
                    }
                },
                {
                    "$unwind": {
                        "path": "$tests",
                        "preserveNullAndEmptyArrays": True
                    }
                },
                {
                    "$group": {
                        "_id": "$_id",
                        "p_name": {
                            "$first": "$p_name"
                        },
                        "p_logo": {
                            "$first": "$p_logo"
                        },
                        "p_type": {
                            "$first": "$p_type"
                        },
                        "tests_num": {
                            "$sum": 1
                        }
                    }
                }
            ])
            list_data = list(data)
            return list_data
        except Exception as e:
            print(e)
            return []