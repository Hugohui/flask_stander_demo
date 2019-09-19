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
import logging
from logging.handlers import RotatingFileHandler


# 日志服务
logging.basicConfig(level=logging.INFO, format="%(message)s")
log_handler = RotatingFileHandler("logs/rpc.log", maxBytes=1024*1024*10, backupCount=10)
logger = logging.getLogger()
logger.addHandler(log_handler)

# 实现 proto 文件中定义的 StragegyServicer
class Stragegy(stragegy_pb2_grpc.StragegyServicer):
    # 实现 proto 文件中定义的 rpc 调用
    def GetStragegy(self, request, context):
        test_id = request.test_id
        md5_id = request.md5_id

        # 获取加盐字符取模
        md5_str = TestsModel.get_str_by_id(test_id)
        md5_value = Util.id_md5(md5_id, md5_str)

        # 获取策略ID
        s_id = StragegyModel.get_stragegy_id(test_id, md5_value)

        # 日志
        logger_data = {
            "method": "GetStragegy",
            "test_id": test_id,
            "md5_id": md5_id,
            "md5_str": md5_str,
            "md5_value": md5_value,
            "s_id": s_id
        }
        logger.info(json.dumps(logger_data))

        return stragegy_pb2.GetReply(stragegy_id = s_id)

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