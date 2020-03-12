#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests
import tkinter
import os
import re
import webbrowser
import tkinter.messagebox


class Subject(object):

    def __init__(self, class_name, class_id, account, password):
        self.class_name = class_name
        self.class_id = class_id
        self.account = account
        self.password = password

        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
        (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"

        self.header = {
            # "origin": "http://jhgkqrz.gensee.com",
            "Referer": "http://jhgkqrz.gensee.com/training/site/s/" + self.class_id,
            'User-Agent': user_agent,
        }
        self.postUrl = "http://jhgkqrz.gensee.com/training/site/s/" + self.class_id
        self.postData = {
            "nickname": account,
            "token": password,
        }

    def login(self):
        response_res = requests.post(self.postUrl, data=self.postData, headers=self.header)

        if len(self.class_name) != 0 and len(self.class_id) != 0 and \
                len(self.account) != 0 and len(self.password) != 0:
            """
            if tkinter.messagebox.askyesno(title='提示', message='是否保存密码？'):
                f = open(os.getcwd() + "\\data.txt", 'w', encoding='utf-8')
                f.write(self.class_id + '\n' + self.account + '\n' + self.password + '\n')
                f.close()
            """
            url = re.findall(re.compile(r'gensee://6170.*3b0a'), response_res.text)
            # print(url)
            if len(url) != 0:
                webbrowser.open(url[0], new=0, autoraise=True)
            else:
                tkinter.messagebox.showerror(title='警告', message='ID或密码错误')
        else:
            tkinter.messagebox.showerror(title='警告', message='输入不能为空')

    def log_time_init(self, time):
        self.time = time
