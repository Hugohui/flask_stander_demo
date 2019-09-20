# coding: utf-8
"""
策略相关Model
:author: huiwenhua
:date: 2019-09-05
"""

from flask import current_app
from models import db
import uuid
from utils.util import Util
from models.log import LogModel

stragegy_col = db["stragegies"]
bucket_col = db["buckets"]
test_col = db["tests"]

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
                    "b_id": data_list[item].get("buckets").get("_id"),
                    "s_id": data_list[item].get("s_id"),
                    "section_min": data_list[item].get("buckets").get("section_min"),
                    "section_max": data_list[item].get("buckets").get("section_max"),
                    "s_name": data_list[item].get("s_name"),
                    "s_desc": data_list[item].get("buckets").get("s_desc")
                })
            return result
        except Exception as e:
            current_app.logger.error(e)
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
            if len(result) != 0:
                return result
            else:
                return 1
        except Exception as e:
            current_app.logger.error(e)
            return 0

    @classmethod
    def insert_stragegy(cls, t_id, s_name, s_desc, section_min, section_max, user_id):
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
                    "create_time": Util.timeFormat()
                })
            bucket_id = str(uuid.uuid1())
            bucket_col.insert({
                "_id": bucket_id,
                "s_id": s_id,
                "t_id": t_id,
                "s_desc": s_desc,
                "section_min": section_min,
                "section_max": section_max,
                "create_time": Util.timeFormat(),
                "creator_id": user_id
            })
            log_str = "策略名称：{}；策略ID：{}；策略描述：{}；分桶ID：{}；分桶区间：{}".format(s_name, s_id, s_desc, bucket_id, str(section_min) + " ~ " +str(section_max))
            log_result = LogModel.add_log("创建策略", log_str, user_id, "insert")
            return 1
            
        except Exception as e:
            current_app.logger.error(e)
            return 0

    @classmethod
    def update_stragegy(cls, t_id, s_id, b_id, s_name, s_desc, section_min, section_max, user_id):
        """
        更新策略
        """
        try: 
            # 更新策略描述
            stragegy_col.update({
                "s_id": s_id,
                "s_desc": {
                    "$ne": s_desc
                }
            },{
                "$set": {
                    "s_desc": s_desc,
                    "update_time": Util.timeFormat()
                }
            })
            # 更新分桶
            bucket_data = bucket_col.find({
                "t_id": t_id,
                "_id": {
                    "$ne": b_id
                }
            })
            for item in bucket_data:
                temp_min = int(item.get("section_min"))
                temp_max = int(item.get("section_max"))
                if max(temp_min, int(section_min)) <= min(temp_max, section_max):
                    return -3002
            data = bucket_col.update({
                "s_id": s_id,
                "_id": b_id,
                "$or": [
                    {
                        "section_min": {
                            "$ne": section_min
                        }
                    },
                    {
                        "section_max": {
                            "$ne": section_max
                        }
                    },
                    {
                        "s_desc": {
                            "$ne": s_desc
                        }
                    }
                ]
            },{
                "$set": {
                    "s_desc": s_desc,
                    "section_min": section_min,
                    "section_max": section_max,
                    "update_time": Util.timeFormat()
                }
            })
            if data.get("ok") == 1:
                log_str = "策略ID：{}；策略描述：{}；分桶ID：{}；分桶区间：{}".format(s_id, s_desc, b_id, str(section_min) + " ~ " +str(section_max))
                log_result = LogModel.add_log("修改策略", log_str, user_id, "update")
                return 1
            else:
                return 0              
        except Exception as e:
            current_app.logger.error(e)
            return 0

    @classmethod
    def delete(cls, s_id, b_id, user_id):
        """
        删除分桶
        """
        try:
            bucket_col.remove({
                "_id": b_id
            })
            log_str = "策略ID：{}；分桶ID：{}".format(s_id, b_id)
            log_result = LogModel.add_log("删除分桶", log_str, user_id, "remove")
            if bucket_col.find({"s_id": s_id}).count() == 0:
                stragegy_col.remove({
                    "s_id": s_id
                })
            return 1
        except Exception as e:
            current_app.logger.error(e)
            return 0

    @classmethod
    def get_stragegy_id(cls, test_id, md5_value):
        """根据实验ID和md5值获取策略ID
        :param test_id: 实验ID
        :param md5_value: md5值
        """
        try:
            t_data = test_col.find_one({
                "_id": test_id
            })
            
            data = bucket_col.find_one({
                "t_id": test_id,
                "section_min": {
                    "$lte": md5_value
                },
                "section_max": {
                    "$gte": md5_value
                }
            })
            if data:
                result = {
                    "code": 1,
                    "message": "成功",
                    "data": data.get("s_id")
                }
                return result
            else:
                result = {
                    "code": -1003,
                    "message": "分桶区间未定义"
                }
                return result
        except Exception as e:
            current_app.logger.error(e)
            result = {
                    "code": -1,
                    "message": "系统内部错误"
            }
            return result