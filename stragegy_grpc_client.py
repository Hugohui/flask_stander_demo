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
    channel = grpc.insecure_channel('ab-test-grpc:50050')
    # channel = grpc.insecure_channel('112.126.118.70:50050')
    # 调用 rpc 服务
    stub = stragegy_pb2_grpc.StragegyStub(channel)
    response = stub.GetStragegy(stragegy_pb2.GetRequest(md5_id='rC8epZTEcw7cSykzvqftiS5iEiE', test_id="e293f5ae-cef8-11e9-a429-c06e964480ff"))
    print("Greeter client received result: " + response.result)

if __name__ == '__main__':
    run()