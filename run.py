# coding:utf-8

"""
项目入口
:author: huiwenhua
:date: 2019-08-27
"""
import settings
from flask import Flask

# 导入视图
from views.platform import platform_view
from views.user import user_view

app = Flask(__name__)

# 注册蓝图
app.register_blueprint(platform_view)
app.register_blueprint(user_view)


@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.debug = settings.IS_DUBUG
    app.run(host="0.0.0.0", port=settings.PORT)