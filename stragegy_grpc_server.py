# coding: utf-8

"""获取策略grpc服务端
:author: huiwenhua
:date: 2019-09-10
"""

from concurrent import futures
import time
import grpc
import stragegy_pb2
import stragegy_pb2_grpc

# 实现 proto 文件中定义的 StragegyServicer
class Stragegy(stragegy_pb2_grpc.StragegyServicer):
    # 实现 proto 文件中定义的 rpc 调用
    def GetStragegy(self, request, context):
        return stragegy_pb2.GetReply(stragegy_id = 'deviceID {md5_id} , testID {test_id}'.format(md5_id = request.md5_id, test_id= request.test_id))

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