# coding: utf-8

"""获取策略grpc客户端
:author: huiwenhua
:date: 2019-09-10
"""

import grpc, random
import stragegy_pb2
import stragegy_pb2_grpc

def run():
    # 连接 rpc 服务器
    channel = grpc.insecure_channel('localhost:50051')
    # channel = grpc.insecure_channel('112.126.118.70:50050')
    # 调用 rpc 服务
    stub = stragegy_pb2_grpc.StragegyStub(channel)
    response = stub.GetStragegy(stragegy_pb2.GetRequest(md5_id=str(random.randint(0,10000)), test_id="70c46782-01d5-11ea-ab13-c63dfbc32fe9"))
    print("Greeter client received result: " + response.result)

if __name__ == '__main__':
    run()