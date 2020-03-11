#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author 弈云

import autolog as au
import tkinter as tk
import tkinter.messagebox
import os

user_data = []
subject = []
log_sub = []


def read_user_data():
    # data文件检查
    if os.path.exists(os.getcwd()+'\\data.txt') == False:
        f = open(os.getcwd() + '\\data.txt', "w")
        f.write("abc\n"+"123456\n"+"zhangsan\n"+"123459\n")
        f.close()
    else:
        size = os.path.getsize(os.getcwd() + '\\data.txt')
        if size < 1:
            f = open(os.getcwd() + '\\data.txt', "w")
            f.write("abc\n" + "123456\n" + "zhangsan\n" + "123459\n")
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


def add_subject(class_name, class_id, account, password, list1):
    subject.append(au.Subject(class_name, class_id, account, password))
    list1.insert('end', class_name)
    f = open(os.getcwd() + '\\data.txt', "a")
    f.write(class_name+"\n" + class_id+"\n" + account+"\n" + password+"\n")
    f.close()


def refresh(tx1, tx2, tx3, tx4, list1):
    tx1.delete(0, 'end')
    tx2.delete(0, 'end')
    tx3.delete(0, 'end')
    tx4.delete(0, 'end')

    number = list(list1.curselection())

    tx1.insert('end', subject[number[0]].class_name)
    tx2.insert('end', subject[number[0]].class_id)
    tx3.insert('end', subject[number[0]].account)
    tx4.insert('end', subject[number[0]].password)

    log_sub[0] = au.Subject(subject[number[0]].class_name, subject[number[0]].class_id,
                         subject[number[0]].account, subject[number[0]].password)


def delete(list1):
    number = list(list1.curselection())
    num = number[0]
    list1.delete(num)
    del subject[num]
    f = open(os.getcwd() + '\\data.txt', "w")
    for i in subject:
        f.write(i.class_name + "\n" + i.class_id + "\n"+ i.account + "\n" + i.password + "\n")
    f.close()


def main():

    # 第1步，实例化object，建立窗口window
    window = tk.Tk()

    # 第2步，给窗口的可视化起名字
    window.title('自动登陆器')

    # 第3步，设定窗口的大小(长 * 宽)
    window.geometry('410x160')  # 这里的乘是小x

    # 输入信息
    tk.Label(window, text='Class Name:', font=('Arial', 12)).place(x=40, y=5)
    tk.Label(window, text='Class ID:', font=('Arial', 12)).place(x=40, y=42)
    tk.Label(window, text='Account:', font=('Arial', 12)).place(x=40, y=79)
    tk.Label(window, text='Password:', font=('Arial', 12)).place(x=40, y=116)

    tk.Label(window, text='Author:Yirule', font=('Arial', 10)).place(x=325, y=140)
    # 课程列表
    lb = tk.Listbox(window, listvariable=None, width=4, height=7)
    lb.place(x=5, y=5)
    # lb.selection_set(0)

    for sub in subject:
        lb.insert('end', sub.class_name)
    # 课程名称
    var_class_name = tk.StringVar()
    var_class_name.set(user_data[0])
    entry_class_name = tk.Entry(window, textvariable=var_class_name, font=('Arial', 12))
    entry_class_name.place(x=135, y=5)
    # 课程ID
    var_class_id = tk.StringVar()
    var_class_id.set(user_data[1])
    entry_class_id = tk.Entry(window, textvariable=var_class_id, font=('Arial', 12))
    entry_class_id.place(x=135, y=42)
    # 用户名
    var_account = tk.StringVar()
    var_account.set(user_data[2])
    entry_account = tk.Entry(window, textvariable=var_account, font=('Arial', 12))
    entry_account.place(x=135, y=79)
    # 用户密码
    var_password = tk.StringVar()
    var_password.set(user_data[3])
    entry_password = tk.Entry(window, textvariable=var_password, font=('Arial', 12))
    entry_password.place(x=135, y=116)
    # 按钮：登录
    log_sub.append(au.Subject(entry_class_name.get(), entry_class_id.get(), entry_account.get(), entry_password.get()))
    log = tk.Button(window, text='Login', font=('Arial', 12), width=8, height=1,command=lambda: log_sub[0].login())
    log.place(x=325, y=4)
    # 按钮：更新信息
    ref = tk.Button(window, text='Refresh', font=('Arial', 12), width=8, height=1, command=lambda: refresh(
        entry_class_name, entry_class_id, entry_account, entry_password, lb))
    ref.place(x=325, y=38)
    # 按钮：添加课程
    add = tk.Button(window, text='Add', font=('Arial', 12), width=8, height=1,
                    command=lambda: add_subject(entry_class_name.get(), entry_class_id.get(), entry_account.get(),
                                               entry_password.get(), lb))
    add.place(x=325, y=72)
    # 按钮：删除课程
    delt = tk.Button(window, text='Delete', font=('Arial', 12), width=8, height=1, command=lambda: delete(lb))
    delt.place(x=325, y=106)

    # 主窗口循环显示
    window.mainloop()


if __name__ == "__main__":
    read_user_data()
    main()

