# coding: utf-8

"""日志相关
:author: huiwenhua
:date: 2019-09-10
:desc: Happy teacher's day！
"""

from models import db
from utils.util import Util
import uuid

log_col = db["logs"]

class LogModel(object):
    'Log类'
    def __init__(self):
        pass
    
    @classmethod
    def get_list(cls, user_id):
        """获取日志列表
        :param user_id: user_id
        """
        try:
            log_col.find({
                "user_id": user_id
            })

            result = list(data)
            return result
        except Exception as e:
            print(e)
            return 0

    @classmethod
    def add_log(cls, title, content, user_id, type):
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
                "create_time": Util.timeFormat()
            })
            return 1
        except Exception as e:
            print(e)
            return 0
