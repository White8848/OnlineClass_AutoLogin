#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author 弈云

import autolog as au
import tkinter as tk
import tkinter.messagebox
import os
import datetime

user_data = []
subject = []
log_sub = []
window = tk.Tk()


def read_user_data():
    # data文件检查
    if os.path.exists(os.getcwd()+'\\data.txt'):
        size = os.path.getsize(os.getcwd() + '\\data.txt')
        if size < 1:
            f = open(os.getcwd() + '\\data.txt', "w")
            f.write("Subject\nClass ID\nYour Account\nYour Password\n")
            f.close()
    else:
        f = open(os.getcwd() + '\\data.txt', "w")
        f.write("Subject\nClass ID\nYour Account\nYour Password\n")
        f.close()

    f = open(os.getcwd()+"\\data.txt", 'r', encoding='gbk')

    for data in f.readlines():
        if len(data) != 0:
            user_data.append(data.strip('\n'))
    f.close()
    if len(user_data) % 4 == 0:
        subject_number = len(user_data)
        for i in range(int(subject_number/4)):
            subject.append(au.Subject(user_data[i*4], user_data[i*4+1], user_data[i*4+2], user_data[i*4+3]))
    else:
        tkinter.messagebox.showerror(title='警告', message='数据损坏\n请删除data.txt并重启！')


def add_subject(list1):
    list1.insert('end', "Subject")
    subject.append(au.Subject("Subject", "Class ID", "Your Account", "Your Password"))
    f = open(os.getcwd() + '\\data.txt', "a")
    f.write("Subject\nClass ID\nYour Account\nYour Password\n")
    f.close()


def delete(list1):
    number = list(list1.curselection())
    num = number[0]
    list1.delete(num)
    del subject[num]
    f = open(os.getcwd() + '\\data.txt', "w")
    for i in subject:
        f.write("%s\n%s\n%s\n%s\n" % (i.class_name, i.class_id, i.account, i.password))
    f.close()


def main():

    # 第2步，给窗口的可视化起名字
    window.title('自动登陆器v1.2')

    # 第3步，设定窗口的大小(长 * 宽)
    window.geometry('410x165+450+250')  # 这里的乘是小x

    # 输入信息
    tk.Label(window, text='Class Name:', font=('Times', 13)).place(x=5, y=5)
    tk.Label(window, text='Class ID:', font=('Times', 13)).place(x=5, y=42)
    tk.Label(window, text='Account:', font=('Times', 13)).place(x=5, y=79)
    tk.Label(window, text='Password:', font=('Times', 13)).place(x=5, y=116)

    tk.Label(window, text='Author:弈云', font=('Times', 10)).place(x=333, y=145)
    # 课程列表
    lb = tk.Listbox(window, listvariable=None, width=5, height=7, font=('Times', 12))
    lb.place(x=272, y=5)
    # lb.selection_set(0)

    for sub in subject:
        lb.insert('end', sub.class_name)
    # 课程名称
    var_class_name = tk.StringVar()
    var_class_name.set(user_data[0])
    entry_class_name = tk.Entry(window, textvariable=var_class_name, font=('Times', 12))
    entry_class_name.place(x=100, y=5)
    # 课程ID
    var_class_id = tk.StringVar()
    var_class_id.set(user_data[1])
    entry_class_id = tk.Entry(window, textvariable=var_class_id, font=('Times', 12))
    entry_class_id.place(x=100, y=42)
    # 用户名
    var_account = tk.StringVar()
    var_account.set(user_data[2])
    entry_account = tk.Entry(window, textvariable=var_account, font=('Times', 12))
    entry_account.place(x=100, y=79)
    # 用户密码
    var_password = tk.StringVar()
    var_password.set(user_data[3])
    entry_password = tk.Entry(window, textvariable=var_password, font=('Times', 12))
    entry_password.place(x=100, y=116)

    # 按钮：登录
    log_sub.append(au.Subject(entry_class_name.get(), entry_class_id.get(), entry_account.get(), entry_password.get()))
    log = tk.Button(window, text='Login', font=('Times', 12), width=8, height=2, command=lambda: log_sub[0].login())
    log.place(x=322, y=4)
    # 按钮：添加课程
    add = tk.Button(window, text='Add', font=('Times', 12), width=8, height=1,command=lambda: add_subject(lb))
    add.place(x=322, y=65)
    # 按钮：删除课程
    delt = tk.Button(window, text='Delete', font=('Times', 12), width=8, height=1, command=lambda: delete(lb))
    delt.place(x=322, y=106)
    change = True
    num = 0

    def change_subject():
        number = list(lb.curselection())
        nonlocal change
        nonlocal num
        if len(number) != 0:
            if num == number[0]:
                subject[number[0]].class_name = entry_class_name.get()
                subject[number[0]].class_id = entry_class_id.get()
                subject[number[0]].account = entry_account.get()
                subject[number[0]].password = entry_password.get()
                log_sub[0] = au.Subject(subject[number[0]].class_name, subject[number[0]].class_id
                                        , subject[number[0]].account, subject[number[0]].password)
                f = open(os.getcwd() + '\\data.txt', "w")
                for i in subject:
                    f.write("%s\n%s\n%s\n%s\n" % (i.class_name, i.class_id, i.account, i.password))
                f.close()
            else:
                num = number[0]
                var_class_name.set(subject[number[0]].class_name)
                var_class_id.set(subject[number[0]].class_id)
                var_account.set(subject[number[0]].account)
                var_password.set(subject[number[0]].password)

        window.after(100, change_subject)
    window.after(100, change_subject)

    # 时钟插件
    def uptime():
        time_label["text"] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        window.after(100, uptime)
    time_label = tkinter.Label(text=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    time_label.place(x=5, y=145)
    window.after(100, uptime)

    # 主窗口循环显示
    window.mainloop()


if __name__ == "__main__":
    read_user_data()
    main()

