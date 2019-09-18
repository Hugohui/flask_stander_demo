# coding: utf-8

"""获取策略grpc客户端
:author: huiwenhua
:date: 2019-09-10
"""

import grpc
import stragegy_pb2
import stragegy_pb2_grpc

def run():
    # 连接 rpc 服务器
    # channel = grpc.insecure_channel('localhost:50051')
    channel = grpc.insecure_channel('47.93.218.129:50051')
    # 调用 rpc 服务
    stub = stragegy_pb2_grpc.StragegyStub(channel)
    response = stub.GetStragegy(stragegy_pb2.GetRequest(md5_id='rC8epZTEcw7cSykzvqftiSQiEiE', test_id="4f6d2822-da0b-11e9-be1d-0242ac120002"))
    print("Greeter client received: " + response.stragegy_id)

if __name__ == '__main__':
    run()