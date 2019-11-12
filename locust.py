# coding: utf-8

"""locust压力测试
:author: huiwenhua
:data: 20191108
"""

from locust import HttpLocust, TaskSet, task

import grpc
import stragegy_pb2
import stragegy_pb2_grpc
import random

def run(l):
    # 连接 rpc 服务器
    # channel = grpc.insecure_channel('localhost:50051')
    channel = grpc.insecure_channel('112.126.118.70:50050')
    # 调用 rpc 服务
    stub = stragegy_pb2_grpc.StragegyStub(channel)
    response = stub.GetStragegy(stragegy_pb2.GetRequest(md5_id=str(random.randint(0,10000)), test_id="70c46782-01d5-11ea-ab13-c63dfbc32fe9"))
    print("Greeter client received result: " + response.result)

class UserTasks(TaskSet):
    # 列出需要测试的任务形式一
    tasks = [run]
    # 列出需要测试的任务形式二 
    # @task
    # def page(self):
    #     self.client.post("/get_build_apk_status",{"bz": "Lightningbox"})

    


    
class WebsiteUser(HttpLocust):
    # 要测试的地址
    # host = "http://version.admin.liquidnetwork.com"
    host = "http://127.0.0.1:8089"
    min_wait = 2000
    max_wait = 5000
    task_set = UserTasks