#!/bin/bash

# 启动grpc服务
python stragegy_grpc_server.py &

# 启动http server
python run.py

