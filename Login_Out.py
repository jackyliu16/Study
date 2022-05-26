"""
@Target : 
@Annotation : 
@Author : JackyLiu
@Date   : 2022/5/25 22:56
@Reference  : 
# 窗口实现相关
    https://blog.csdn.net/Jason_WangYing/article/details/108916236
    https://blog.csdn.net/weixin_40450867/article/details/81431718
@Source :
    
"""
# import json
import Login_In

import tkinter as tk
from tkinter import messagebox

# Initialization
In_model = Login_In.MemoryCell()

# === Main Screen ===

window = tk.Tk()
window.title("登录窗口")
window.geometry("600x400")

# put photo
canvas = tk.Canvas(window, height=127, width=445)
image_file = tk.PhotoImage(file='welcome.png')
image = canvas.create_image(0, 0, anchor='nw', image=image_file)
canvas.pack(side='top')

# Label and input
tk.Label(window, text='User Name:').place(x=90, y=150)
tk.Label(window, text='PassWord: ').place(x=90, y=190)

# input box
var_name = tk.StringVar()
entry_var_name = tk.Entry(window, textvariable=var_name)
entry_var_name.place(x=200, y=150)

var_pwd = tk.StringVar()
entry_pwd = tk.Entry(window, textvariable=var_pwd)
entry_pwd.place(x=200, y=190)


# === Windows Display ===
# sub_window_of_sign_in.withdraw()


def login():
    inp_name = var_name.get()
    inp_pwd = var_pwd.get()
    if inp_pwd and inp_name:
        if In_model.check_passwd(inp_name, inp_pwd) == 0:
            tk.messagebox.showinfo(title="登录成功", message=f"{inp_name}, 欢迎登录！")
        elif In_model.check_passwd(inp_name, inp_pwd) == -1:
            tk.messagebox.showerror(title="登录失败", message=f"你所输入的密码不正确！！！")
        else:
            tk.messagebox.showerror(title="登录失败", message=f"输入的用户名不存在！！！")
    else:
        tk.messagebox.showerror(title="Error", message=f"用户名和密码不能为空！！！")


def show_signin():
    def add_user():
        nonlocal var_signin_name, var_signin_pwd, var_signin_repwd
        sign_name = var_signin_name.get()
        sign_pwd = var_signin_pwd.get()
        sign_repwd = var_signin_repwd.get()
        if not sign_name or not sign_pwd or not sign_repwd:
            tk.messagebox.showerror(title="Error", message=f"输入值不能为空！！！")
        else:
            if sign_pwd != sign_repwd:
                tk.messagebox.showerror(title="Error", message=f"输入的两次密码不一致")
            else:
                ret = In_model.add_user(sign_name, sign_pwd)
                if ret:
                    tk.messagebox.showinfo(title="注册成功！", message=f"成功注册{sign_name}")
                else :
                    tk.messagebox.showerror(title="Error", message=f"存在相同名称的用户！！！")

    # sub_window_of_sign_in.deiconify()

    sub_window_of_sign_in = tk.Toplevel(window)
    sub_window_of_sign_in.title("Sign In")
    sub_window_of_sign_in.geometry("400x200")

    tk.Label(sub_window_of_sign_in, text="Enter a user name:").place(x=30, y=50)
    tk.Label(sub_window_of_sign_in, text='enter password:').place(x=30, y=80)
    tk.Label(sub_window_of_sign_in, text="Re-enter your password:").place(x=30, y=110)

    var_signin_name = tk.StringVar()
    var_signin_pwd = tk.StringVar()
    var_signin_repwd = tk.StringVar()

    entry_signin_name = tk.Entry(sub_window_of_sign_in, textvariable=var_signin_name)
    entry_signin_pwd = tk.Entry(sub_window_of_sign_in, textvariable=var_signin_pwd)
    entry_signin_repwd = tk.Entry(sub_window_of_sign_in, textvariable=var_signin_repwd)

    entry_signin_name.place(x=180, y=50)
    entry_signin_pwd.place(x=180, y=80)
    entry_signin_repwd.place(x=180, y=110)

    bt_sign = tk.Button(sub_window_of_sign_in, text="注册", command=add_user)
    bt_sign.place(x=200, y=150)


def quit_programme():
    window.destroy()


bt_login = tk.Button(window, text="Login", command=login)
bt_login.place(x=200, y=230)
bt_show_signin = tk.Button(window, text="Sign In", command=show_signin)
bt_show_signin.place(x=260, y=230)
bt_quit_programme = tk.Button(window, text='退出', command=quit_programme)
bt_quit_programme.place(x=330, y=230)

# mainloop has been conclude
window.mainloop()
