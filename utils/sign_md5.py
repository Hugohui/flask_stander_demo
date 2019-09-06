#!/usr/bin/env python
# -*- coding: utf-8 -*-
import hashlib
import settings

def sign_md5(src=settings.DINGDING_SRC, key=settings.DINGDING_KEY, code=None):
    """ 加密 
    :param src: 跳转地址 
    :param code: 临时码 
    :param key: 关键词 
    :return: 
    """
    md5_key = src + key + code
    return hashlib.md5(md5_key.encode("utf-8")).hexdigest()