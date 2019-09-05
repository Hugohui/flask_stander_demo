# coding: utf-8
"""
策略相关Model
:author: huiwenhua
:date: 2019-09-05
"""

from models import db
import uuid
from utils.util import Util

stragegy_col = db["stragegies"]
bucket_col = db["buckets"]

class StragegyModel(object):
    '策略Model类'
    def __init__(self):
        pass

    @classmethod
    def get_stragegy(cls, t_id):
        """
        策略list
        """
        try:
            data = stragegy_col.aggregate([
                {
                    "$match": {
                        "t_id": t_id
                    }
                },
                {
                    "$lookup": {
                        "from": "buckets",
                        "localField": "s_id",
                        "foreignField": "s_id",
                        "as": "buckets"
                    }
                },
                {
                    "$unwind": { 
                        "path": "$buckets",
                        "preserveNullAndEmptyArrays": True
                    }
                }
            ])
            data_list = list(data)
            data_len = len(data_list)
            result = []
            for item in range(data_len):
                result.append({
                    "b_id": data_list[item].get("_id"),
                    "s_id": data_list[item].get("s_id"),
                    "section_min": data_list[item].get("buckets").get("section_min"),
                    "section_max": data_list[item].get("buckets").get("section_max"),
                    "s_name": data_list[item].get("s_name"),
                    "s_desc": data_list[item].get("s_desc")
                })
            return result
        except Exception as e:
            print(e)
            return 0

    @classmethod
    def pre_check(cls, t_id, s_name):
        """
        提交前检查策略是否存在
        """
        try:
            data = stragegy_col.find({
                "t_id": t_id,
                "s_name": s_name
            })
            result = []
            for item in data:
                bucket_data = bucket_col.find_one({"s_id": item.get("_id")})
                result.append({
                    "section_min": bucket_data.get("section_min"),
                    "section_max": bucket_data.get("section_max")
                })
            if data != 0:
                return result
            else:
                return 1
        except Exception as e:
            print(e)
            return 0

    @classmethod
    def insert_stragegy(cls, t_id, s_name, s_desc, section_min, section_max):
        """
        新增策略
        """
        try:
            # 分桶区间逻辑判
            # 查询实验的所有策略
            data = stragegy_col.aggregate([
                {
                    "$match": {
                        "t_id": t_id
                    }
                },
                {
                    "$lookup": {
                        "from": "buckets",
                        "localField": "s_id",
                        "foreignField": "s_id",
                        "as": "buckets"
                    }
                },
                {
                    "$unwind": { 
                        "path": "$buckets",
                        "preserveNullAndEmptyArrays": True
                    }
                }
            ])

            # 如果有策略则进行判断（区间是否有重合）
            data_list = list(data)
            data_len = len(data_list)
            s_id = ""
            if  data_len> 0:
                for item in range(data_len):
                    temp_min = int(data_list[item].get("buckets").get("section_min"))
                    temp_max = int(data_list[item].get("buckets").get("section_max"))
                    if max(temp_min, int(section_min)) <= min(temp_max, int(section_max)):
                        return -3002          
                    if s_name == data_list[item].get("s_name"):
                        s_id = data_list[item].get("_id")

            if s_id == "":
                # 如果没有策略则直接插入
                _id = str(uuid.uuid1())
                s_id = stragegy_col.insert({
                    "_id": _id,
                    "s_id": _id,
                    "t_id": t_id,
                    "s_name": s_name,
                    "s_desc": s_desc,
                    "create_time": Util.timeFormat()
                })
            bucket_col.insert({
                "_id": str(uuid.uuid1()),
                "s_id": s_id,
                "t_id": t_id,
                "section_min": section_min,
                "section_max": section_max,
                "create_time": Util.timeFormat()
            })
            return 1
            
        except Exception as e:
            print(e)
            return 0