# -*- coding: utf-8 -*-
"""
Created on Sun Aug  5 10:34:10 2018
@author: Administrator
https://blog.csdn.net/weixin_40450867/article/details/81431718
"""
import pickle
import tkinter as tk
import tkinter.messagebox

# 窗口
window = tk.Tk()
window.title('欢迎进入学习系统')
window.geometry('960x960')
# 画布放置图片
canvas = tk.Canvas(window, height=962, width=800)
imagefile = tk.PhotoImage(file='Line.png')
image = canvas.create_image(0, 0, anchor='nw', image=imagefile)
canvas.pack(side='top')
# 标签 用户名密码
tk.Label(window, text='起始站点:').place(x=100, y=150)
tk.Label(window, text='终止站点:').place(x=100, y=190)
# 起始点输入
start_station = tk.StringVar()
entry_usr_name = tk.Entry(window, textvariable=start_station)
entry_usr_name.place(x=170, y=150)
# 终止站输入
end_station = tk.StringVar()
entry_usr_pwd = tk.Entry(window, textvariable=end_station, show='*')
entry_usr_pwd.place(x=170, y=190)


# 登录函数
def usr_log_in():
    # 输入框获取用户名密码
    usr_name = start_station.get()
    usr_pwd = end_station.get()



    # #从本地字典获取用户信息，如果没有则新建本地数据库
    # try:
    #     with open('usr_info.pickle','rb') as usr_file:
    #         usrs_info=pickle.load(usr_file)
    # except FileNotFoundError:
    #     with open('usr_info.pickle','wb') as usr_file:
    #         usrs_info={'admin':'admin'}
    #         pickle.dump(usrs_info,usr_file)
    # #判断用户名和密码是否匹配
    # if usr_name in usrs_info:
    #     if usr_pwd == usrs_info[usr_name]:
    #         tk.messagebox.showinfo(title='welcome',
    #                                message='欢迎您：'+usr_name)
    #     else:
    #         tk.messagebox.showerror(message='密码错误')
    # #用户名密码不能为空
    # elif usr_name=='' or usr_pwd=='' :
    #     tk.messagebox.showerror(message='用户名或密码为空')
    # #不在数据库中弹出是否注册的框
    # else:
    #     is_signup=tk.messagebox.askyesno('欢迎','您还没有注册，是否现在注册')
    #     if is_signup:
    #         usr_sign_up()


# 注册函数
def usr_sign_up():
    # 确认注册时的相应函数
    def signtowcg():
        # 获取输入框内的内容
        nn = new_name.get()
        np = new_pwd.get()
        npf = new_pwd_confirm.get()

        # 本地加载已有用户信息,如果没有则已有用户信息为空
        try:
            with open('usr_info.pickle', 'rb') as usr_file:
                exist_usr_info = pickle.load(usr_file)
        except FileNotFoundError:
            exist_usr_info = {}

            # 检查用户名存在、密码为空、密码前后不一致
        if nn in exist_usr_info:
            tk.messagebox.showerror('错误', '用户名已存在')
        elif np == '' or nn == '':
            tk.messagebox.showerror('错误', '用户名或密码为空')
        elif np != npf:
            tk.messagebox.showerror('错误', '密码前后不一致')
        # 注册信息没有问题则将用户名密码写入数据库
        else:
            exist_usr_info[nn] = np
            with open('usr_info.pickle', 'wb') as usr_file:
                pickle.dump(exist_usr_info, usr_file)
            tk.messagebox.showinfo('欢迎', '注册成功')
            # 注册成功关闭注册框
            window_sign_up.destroy()

    # 新建注册界面
    window_sign_up = tk.Toplevel(window)
    window_sign_up.geometry('350x200')
    window_sign_up.title('注册')
    # 用户名变量及标签、输入框
    new_name = tk.StringVar()
    tk.Label(window_sign_up, text='用户名：').place(x=10, y=10)
    tk.Entry(window_sign_up, textvariable=new_name).place(x=150, y=10)
    # 密码变量及标签、输入框
    new_pwd = tk.StringVar()
    tk.Label(window_sign_up, text='请输入密码：').place(x=10, y=50)
    tk.Entry(window_sign_up, textvariable=new_pwd, show='*').place(x=150, y=50)
    # 重复密码变量及标签、输入框
    new_pwd_confirm = tk.StringVar()
    tk.Label(window_sign_up, text='请再次输入密码：').place(x=10, y=90)
    tk.Entry(window_sign_up, textvariable=new_pwd_confirm, show='*').place(x=150, y=90)
    # 确认注册按钮及位置
    bt_confirm_sign_up = tk.Button(window_sign_up, text='确认注册',
                                   command=signtowcg)
    bt_confirm_sign_up.place(x=150, y=130)


# 退出的函数
def usr_sign_quit():
    window.destroy()


# 登录 注册按钮
bt_login = tk.Button(window, text='进行计算', command=usr_log_in)
bt_login.place(x=140, y=230)
bt_logup = tk.Button(window, text='更换模式', command=usr_sign_up)
bt_logup.place(x=220, y=230)
bt_logquit = tk.Button(window, text='退出', command=usr_sign_quit)
bt_logquit.place(x=300, y=230)
# 主循环
window.mainloop()
