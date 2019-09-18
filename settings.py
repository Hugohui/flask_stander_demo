# coding:utf-8

"""
设置
:author: huiwenhua
:date: 2019-08-27
"""

IS_DEBUG = False
PORT = 5203

# 是否开启扫码登陆
FORCE_LOGIN = False

# MongoDB
# 外网 "mongodb://admin:n3tw0rk@dds-2ze4b601d1f5a9141374-pub.mongodb.rds.aliyuncs.com:3717,dds-2ze4b601d1f5a9142107-pub.mongodb.rds.aliyuncs.com:3717/ab_test?replicaSet=mgset-16573833"
# 内网 "mongodb://admin:n3tw0rk@dds-2ze4b601d1f5a9141.mongodb.rds.aliyuncs.com:3717,dds-2ze4b601d1f5a9142.mongodb.rds.aliyuncs.com:3717/ab_test?replicaSet=mgset-16573833"
MONGO_HOST = "127.0.0.1" if IS_DEBUG else "mongodb://admin:n3tw0rk@dds-2ze4b601d1f5a9141374-pub.mongodb.rds.aliyuncs.com:3717,dds-2ze4b601d1f5a9142107-pub.mongodb.rds.aliyuncs.com:3717/ab_test?replicaSet=mgset-16573833"

# 扫码登陆用户MongoDB
USER_MONGO_HOST = "mongodb://liquid:n3tw0rk@dds-2ze5fffe69c1c5541874-pub.mongodb.rds.aliyuncs.com:3717,dds-2ze5fffe69c1c5542283-pub.mongodb.rds.aliyuncs.com:3717/activity?replicaSet=mgset-13269097" if IS_DEBUG else "mongodb://liquid:n3tw0rk@dds-2ze5fffe69c1c5541.mongodb.rds.aliyuncs.com:3717,dds-2ze5fffe69c1c5542.mongodb.rds.aliyuncs.com:3717/activity?replicaSet=mgset-13269097"

# 扫码登录
# 项目访问地址
DINGDING_SRC = "http://10.0.100.76:8081" if IS_DEBUG else "http://xxx.liquidnetwork.com"

# 分配的key
DINGDING_KEY = "ABTest-devFhWCJi32po56HvoKJ"

# 权限后台地址
IF_PERMISSION_URL = "http://scancode.liquidnetwork.com"