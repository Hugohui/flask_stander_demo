# -*- coding: utf-8 -*-
""" 通过临时code以及webid换取是否有当前权限访问 """
import requests, time, json
import settings

def code_permission(tmp_auth_code=None, website_id=None):
    """ 
    判断code是否有权限 
    :return: 
    """
    url = '{}/white/unionid_if_permission?code={}&website_id={}'.format(settings.IF_PERMISSION_URL,tmp_auth_code, website_id)
    response = requests.get(url=url)

    res_dict = json.loads(response.text)
    return res_dict