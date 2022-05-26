"""
@Target :
@Annotation :
@Author : JackyLiu
@Date   : 2022/5/26 18:12
@Less reference  :
    1.  https://www.cnblogs.com/myshuzhimei/p/11764522.html
    2.  https://www.cnblogs.com/ListenWind/p/4624476.html#:~:text=%E5%88%A4%E6%96%ADPython%E8%BE%93%E5%85%A5%E6%98%AF%E5%90%A6%E4%B8%BA%E6%95%B0%E5%AD%97.%20%E5%9C%A8%E6%8E%A5%E6%94%B6raw_input%E6%96%B9%E6%B3%95%E5%90%8E%EF%BC%8C%E5%88%A4%E6%96%AD%E6%8E%A5%E6%94%B6%E5%88%B0%E7%9A%84%E5%AD%97%E7%AC%A6%E4%B8%B2%E6%98%AF%E5%90%A6%E4%B8%BA%E6%95%B0%E5%AD%97.%20%E4%BE%8B%E5%A6%82%EF%BC%9A.%20str%20%3D%20raw_input%20%28%22please%20input,%E4%B8%BATrue%E8%A1%A8%E7%A4%BA%E8%BE%93%E5%85%A5%E7%9A%84%E6%89%80%E6%9C%89%E5%AD%97%E7%AC%A6%E9%83%BD%E6%98%AF%E6%95%B0%E5%AD%97%EF%BC%8C%E5%90%A6%E5%88%99%EF%BC%8C%E4%B8%8D%E6%98%AF%E5%85%A8%E9%83%A8%E4%B8%BA%E6%95%B0%E5%AD%97.%20str%E4%B8%BA%E5%AD%97%E7%AC%A6%E4%B8%B2.%20str.isalnum%20%28%29%20%E6%89%80%E6%9C%89%E5%AD%97%E7%AC%A6%E9%83%BD%E6%98%AF%E6%95%B0%E5%AD%97%E6%88%96%E8%80%85%E5%AD%97%E6%AF%8D.%20str.isalpha%20%28%29%20%E6%89%80%E6%9C%89%E5%AD%97%E7%AC%A6%E9%83%BD%E6%98%AF%E5%AD%97%E6%AF%8D.
"""

import tkinter as tk
from tkinter import messagebox

# import json
import Guess_In

# Initialization
In = Guess_In.Guess()

# === Main Screen ===
window = tk.Tk()
window.title("Guessing number!")
window.geometry("400x180")

# Label
var_display = tk.Variable()
tk.Label(window, textvariable=var_display).place(x=180, y=10)
tk.Label(window, text="Number's you guess: ").place(x=50, y=60)

# Input Box
var_guess_num = tk.StringVar()
tk.Entry(window, textvariable=var_guess_num).place(x=200, y=60)


def guess():
    global var_display
    print(var_guess_num.get())
    if not var_guess_num.get():
        tk.messagebox.showerror(title="Error", message="请输入你所猜的数字！！！")
    else:
        # if not isinstance(var_guess_num.get(), int):
        if not var_guess_num.get().isdigit():
            tk.messagebox.showerror(title="Error", message="请勿输入非数字元素")
        elif int(var_guess_num.get()) > 1024 or int(var_guess_num.get()) < 0:
            tk.messagebox.showerror(title="Error", message="请输入0~1024范围内的数字")
        else:
            ret = In.guess(int(var_guess_num.get()))
            if ret == 0:
                var_display.set("恭喜你猜中了！！！")
                tk.messagebox.showinfo(title="恭喜！", message=f"恭喜你使用了{In.get_time()}次成功的猜出了结果\n数据显示十次以下能猜中的人都运气很好呢")
            elif ret == 1:
                var_display.set(f"你输入的数字过高，\n真实的数字比{var_guess_num.get()}高")
            elif ret == -1:
                var_display.set(f"你输入的数字过低，\n真实的数字比{var_guess_num.get()}低")


def quit_programme():
    window.destroy()


bt_guess = tk.Button(window, text="猜", command=guess)
bt_guess.place(x=200, y=100)
bt_close_window = tk.Button(window, text="关闭", command=quit_programme)
bt_close_window.place(x=230, y=100)

# mainloop has been conclude
window.mainloop()
