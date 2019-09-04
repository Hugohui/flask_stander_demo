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

class TestsModel(object):
    '实验Model类'
    def __init__(self):
        pass

    @classmethod
    def add_test(cls, p_id, t_name, t_str, t_desc):
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