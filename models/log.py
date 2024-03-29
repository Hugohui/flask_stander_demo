# coding: utf-8

"""日志相关
:author: huiwenhua
:date: 2019-09-10
:desc: Happy teacher's day！
"""

from flask import Flask, current_app
from models import db
from utils.util import Util
import uuid
from models.user import UserModel

log_col = db["logs"]

class LogModel(object):
    'Log类'
    def __init__(self):
        pass
    
    @classmethod
    def get_list(cls, user_id, page=1, page_limit=40):
        """获取日志列表
        :param user_id: user_id
        """
        try:
            skip = page_limit * (page -1)
            data = log_col.find().limit(page_limit).skip(skip).sort([("create_time",-1)])
            total = log_col.find().count()
            result = {
                "total": total,
                "limit": page_limit,
                "list": []
            }
            for item in data:
                result["list"].append({
                    "create_time": item.get("create_time"),
                    "title": item.get("l_title"),
                    "content": item.get("l_content"),
                    "user_name": UserModel.get_userinfo_by_id(item.get("user_id")).get("nickname")
                })
            return result
        except Exception as e:
            current_app.logger.error(e)
            return 0

    @classmethod
    def add_log(cls, title, content, user_id, l_type):
        """添加日志
        :param title: 标题
        :param content: 内容
        :param user_id: 用户ID
        :param type: 类型 insert、remove、update
        :return:
        """
        try:
            log_col.insert({
                "_id": str(uuid.uuid1()),
                "l_title": title,
                "l_content": content,
                "user_id": user_id,
                "l_type": l_type,
                "create_time": Util.timeFormat()
            })
            return 1
        except Exception as e:
            current_app.logger.error(e)
            return 0
