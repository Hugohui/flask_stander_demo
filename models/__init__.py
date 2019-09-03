# coding:utf-8

"""
数据库
:author: huiwenhua
:date: 2019-09-03
"""

from pymongo import MongoClient
import settings

mongo_client = MongoClient(host=settings.MONGO_HOST)
db = mongo_client["ab_test"]