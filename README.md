### AB实验平台后端


#### 目录
```
|-- python
      |-- .gitignore
      |-- README.md
      |-- run.py
      |-- settings.py
      |-- settings.pyc
      |-- .vscode
      |   |-- settings.json
      |-- models
      |-- static
      |-- templates
      |-- views
      |-- utils
      |   |-- __init__.py
      |   |-- json_response.py
      |   |-- request.py
      |   |-- util.py
```


#### gRPC
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
