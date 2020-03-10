#!/usr/bin/env python
# -*- coding:utf-8 -*-

import requests
import re
import webbrowser


class User(object):

    def __init__(self, class_id, account, password):
        self.class_id = class_id
        self.account = account
        self.password = password

        userAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
        (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"

        self.header = {
            # "origin": "http://jhgkqrz.gensee.com",
            "Referer": "http://jhgkqrz.gensee.com/training/site/s/" + self.class_id,
            'User-Agent': userAgent,
        }
        self.postUrl = "http://jhgkqrz.gensee.com/training/site/s/" + self.class_id
        self.postData = {
            "nickname": account,
            "token": password,
        }
