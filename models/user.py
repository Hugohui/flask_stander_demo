# coding: utf-8

"""user Model
:author: huiwenhua
:date: 2019-09-10
:desc: Happy teacher's day!
"""

from pymongo import MongoClient
import settings

mongo_client = MongoClient(host=settings.USER_MONGO_HOST)
user_db = mongo_client["activity"]
user_info_col = user_db["ddUserInfo"]

class UserModel(object):
    "UserModel"
    def __init__(self):
        pass

    @classmethod
    def get_userinfo_by_id(cls, user_id):
        """获取用户信息
        """
        try:
            data = user_info_col.find_one({
                "_id": user_id
            })
            print(data)
            return data
        except Exception as e:
            print(e)
            return 0
