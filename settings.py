# coding:utf-8

"""
设置
:author: huiwenhua
:date: 2019-08-27
"""

IS_DEBUG = True
PORT = 5203

# MongoDB
MONGO_HOST = "127.0.0.1" if IS_DEBUG else ""

# 扫码登录
# 项目访问地址
DINGDING_SRC = "http://10.0.100.76:8081/#/index" if IS_DEBUG else "http://xxx.liquidnetwork.com"

# 分配的key
DINGDING_KEY = "ABTest-devFhWCJi32po56HvoKJ" 

# 权限后台地址
IF_PERMISSION_URL = "http://scancode.liquidnetwork.com"