# coding:utf-8

"""
项目入口
:author: huiwenhua
:date: 2019-08-27
"""
import settings
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.debug = settings.IS_DUBUG
    app.run(host="0.0.0.0", port=settings.PORT)