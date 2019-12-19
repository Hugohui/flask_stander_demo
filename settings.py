# coding:utf-8

"""
设置
:author: huiwenhua
:date: 2019-08-27
"""

IS_DEBUG = False
PORT = 5200

# 是否开启扫码登陆
FORCE_LOGIN = True

# MongoDB
MONGO_HOST = ""

# redis
REDIS_HOST = "127.0.0.1" if IS_DEBUG else "r-2zes5pw8ebs7v11z20.redis.rds.aliyuncs.com"
REDIS_PORT = 6379
REDIS_PASSWORD  = "" if IS_DEBUG else ""
REDIS_DB = 0

# 扫码登陆用户MongoDB
USER_MONGO_HOST = 
# 扫码登录
# 项目访问地址
DINGDING_SRC = "http://10.0.100.76:8080" if IS_DEBUG else "
# 分配的key
DINGDING_KEY = "ABTest-devFhWCJi32po56HvoKJ"

# 权限后台地址ECS部署
# IF_PERMISSION_URL = "http://scancode.liquidnetwork.com"
# 权限后台地址k8s部署
IF_PERMISSION_URL = "http://base-login:80"
