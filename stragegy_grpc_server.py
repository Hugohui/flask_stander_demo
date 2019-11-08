# coding: utf-8

"""获取策略grpc服务端
:author: huiwenhua
:date: 2019-09-10
"""

from concurrent import futures
import time, json, grpc, stragegy_pb2, stragegy_pb2_grpc
from utils.util import Util
from models.test import TestsModel
from models.stragegy import StragegyModel
import logging, redis, settings, json
from logging.handlers import RotatingFileHandler


# 日志服务
logging.basicConfig(level=logging.INFO, format="%(message)s")
log_handler = RotatingFileHandler("logs/rpc.log", maxBytes=1024*1024*10, backupCount=10)
logger = logging.getLogger()
logger.addHandler(log_handler)

rds = redis.Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=settings.REDIS_DB, password=settings.REDIS_PASSWORD)

# 实现 proto 文件中定义的 StragegyServicer
class Stragegy(stragegy_pb2_grpc.StragegyServicer):
    # 实现 proto 文件中定义的 rpc 调用
    def GetStragegy(self, request, context):
        try:
            test_id = request.test_id
            md5_id = request.md5_id

            if not test_id or not md5_id:
                result = {
                    "code": -1000,
                    "message": "参数错误"
                }
                logger_data = {
                    "method": "GetStragegy",
                    "test_id": test_id,
                    "md5_id": md5_id,
                    "query_result": result
                }
                logger.info(json.dumps(logger_data))
                return stragegy_pb2.GetReply(result = json.dumps(result))

            # redis
            redis_key = str(md5_id) + "&" + str(test_id)

            redis_value = rds.get(redis_key)

            if redis_value:
                result = {
                    "code": 1,
                    "message": "成功",
                    "data": redis_value.decode()
                }
                logger_data = {
                    "method": "GetStragegy",
                    "test_id": test_id,
                    "md5_id": md5_id,
                    "query_result": result
                }
                logger.info(json.dumps(logger_data))
                return stragegy_pb2.GetReply(result = json.dumps(result))
 
            # 获取加盐字符取模
            md5_str = TestsModel.get_str_by_id(test_id)

            # 加盐字符串查询和实验状态判断
            if md5_str.get("code") != 1:
                logger_data = {
                    "method": "GetStragegy",
                    "test_id": test_id,
                    "md5_id": md5_id,
                    "query_result": md5_str
                }
                logger.info(json.dumps(logger_data))
                return stragegy_pb2.GetReply(result = json.dumps(md5_str))

            md5_value = Util.id_md5(md5_id, md5_str.get("data"))

            # 获取策略ID
            query_result = StragegyModel.get_stragegy_id(test_id, md5_value)

            s_id = ""
            # 获取成功
            if query_result.get("code") == 1:
                s_id = query_result.get("data")
                rds.set(redis_key, s_id, ex=60 * 3)

            # 日志
            logger_data = {
                "method": "GetStragegy",
                "test_id": test_id,
                "md5_id": md5_id,
                "md5_str": md5_str,
                "md5_value": md5_value,
                "query_result": query_result
            }
            logger.info(json.dumps(logger_data))

            return stragegy_pb2.GetReply(result = json.dumps(query_result))
        except Exception as e:
            result = {
                "code": -1,
                "message": "系统内部错误"
            }
            logger_data = {
                "method": "GetStragegy",
                "query_result": result
            }
            logger.info(json.dumps(logger_data))
            return stragegy_pb2.GetReply(result = json.dumps(result))

def serve():
    # 启动 rpc 服务
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    stragegy_pb2_grpc.add_StragegyServicer_to_server(Stragegy(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(60*60*24) # one day in seconds
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()