### AB实验平台后端

#### 项目目录
```
|-- python
    |-- .dockerignore
    |-- .gitignore
    |-- Dockerfile
    |-- README.md
    |-- requirements.txt
    |-- run.py    // 项目入口
    |-- settings.py
    |-- stragegy_grpc_client.py   // rpc客户端
    |-- stragegy_grpc_server.py   // rpc服务端
    |-- stragegy_pb2.py
    |-- stragegy_pb2_grpc.py
    |-- logs
    |   |-- ab-test.log
    |   |-- rpc.log
    |-- models
    |   |-- __init__.py
    |   |-- log.py
    |   |-- platform.py
    |   |-- stragegy.py
    |   |-- test.py
    |   |-- user.py
    |-- protos
    |   |-- stragegy.proto
    |-- static
    |-- templates
    |-- utils
    |   |-- __init__.py
    |   |-- json_response.py
    |   |-- permission.py
    |   |-- request.py
    |   |-- sign_md5.py
    |   |-- util.py
```

#### 平台API服务
##### 创建虚拟环境
```python
virtualenv python3安装路径 venv
```
##### 安装依赖
```python
venv/bin/pip install -r requirements.txt
```
##### 启动项目
```python
venv/bin/python run.py
```

##### 平台入口（部署到不同服务器需要修改接口访问IP）
```javascript
http://liquid-h5.oss-cn-beijing.aliyuncs.com/ab_test/index.html
```

#### gRPC服务
##### 生成
- install gRPC
      ```python
      python -m pip install grpcio
      ```
- install gRPC tools
      ```python
      python -m pip install grpcio-tools
      ```
- generate gRPC code
      ```python
      python -m grpc_tools.protoc -I ./protos/ --python_out=. --grpc_python_out=. ./protos/stragegy.proto
      ```
##### 启动server
```python
venv/bin/python stragegy_grpc_server.py
# 守护进程启动
nohup venv/bin/python stragegy_grpc_server.py &
```

##### client调用
```python
# 具体调用实现：stragegy_grpc_client.py
```

#### Docker
如果对docker不了解，请先学习[Docker 入门教程](http://www.ruanyifeng.com/blog/2018/02/docker-tutorial.html)
##### 打包镜像
```bash
docker image build -t [imageName] .
```

##### 将镜像push到镜像仓库
```bash
docker image push [username]/[repository]:[tag]
```

##### 拉取镜像到机器
```bash
docker image pull [username]/[repository]:[tag]
```

##### 平台服务容器
```bash
docker container run -p 5200:5200 [imageName] python run.py
# 或者守护进程
docker container run -d -p 5200:5200 [imageName] python run.py
```

#### gRPC服务容器
```bash
docker container run -p 50051:50051 [imageName] python stragegy_grpc_server.py
# 或者守护进程
docker container run -d -p 50051:50051 [imageName] python stragegy_grpc_server.py
```
