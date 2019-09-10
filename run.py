# coding:utf-8

"""
项目入口
:author: huiwenhua
:date: 2019-08-27
"""
import settings
from flask import Flask, request, make_response, jsonify, redirect
from utils.permission import code_permission
from utils.sign_md5 import sign_md5

# 导入视图
from views.platform import platform_view
from views.user import user_view
from views.test import test_view
from views.stragegy import stragegy_view
from views.log import log_view

app = Flask(__name__)

# 注册蓝图
app.register_blueprint(platform_view)
app.register_blueprint(user_view)
app.register_blueprint(test_view)
app.register_blueprint(stragegy_view)
app.register_blueprint(log_view)


@app.before_request
def before_request():
    referrer = request.referrer
    
    # 环境判断（测试/正式），测试环境不做扫码验证
    if  not settings.IS_DEBUG:
        cookies_tmp_code = request.cookies.get('tmp_code')
        cookies_website_id = request.cookies.get('website_id')

        request_tmp_code = request.args.get("tmp_code", '')
        request_sign = request.args.get("sign", '')
        request_website_id = request.args.get("website_id", '')

        print("cookies_tmp_code===",cookies_tmp_code)
        print("cookies_website_id===",cookies_website_id)

        print("request_tmp_code===",request_tmp_code)
        print("request_sign===",request_sign)
        print("request_website_id===",request_website_id)


        # 优先判断request_code、cookies_code
        if request_tmp_code:
            if request_sign == sign_md5(code=request_tmp_code):
                print 'auth success!'
            else:
                resData = {
                    "code": 401,
                    "msg": 'no permission'
                }
                res = make_response(jsonify(resData))
                return res
        elif cookies_tmp_code:
            res_dict = code_permission(
                tmp_auth_code=cookies_tmp_code, website_id=cookies_website_id)
            if res_dict.get('code') == 0:
                print 'auth success!'
            else:
                res = redirect(referrer)
                return res
        else:
            resData = {
                "code": 401,
                "msg": 'no permission'
            }
            res = make_response(jsonify(resData))
            return res


@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.debug = settings.IS_DEBUG
    app.run(host="0.0.0.0", port=settings.PORT)