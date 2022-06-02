"""
@Target :
@Annotation :
@Author : JackyLiu
@Date   : 2022/6/2 10:02
@Reference  :
# 窗口实现相关
    https://blog.csdn.net/Jason_WangYing/article/details/108916236
    https://blog.csdn.net/weixin_40450867/article/details/81431718
    https://blog.csdn.net/weixin_46185085/article/details/106817073
# 打包相关：
    https://blog.csdn.net/qq_33521184/article/details/89391354
    https://blog.csdn.net/qq_42063091/article/details/82423221
@Source :

"""
import tkinter
import tkinter as tk
from tkinter import messagebox

# windows
import internalLogic

window = tk.Tk()
window.title("欢迎进入地铁线路规划系统")
window.geometry("960x860")
# put photo
# canvas = tk.Canvas(window, height=962, width=1098)
# image_file = tk.PhotoImage(file='Line.png')
# image = canvas.create_image(0, 0, anchor='nw', image=image_file)
# canvas.pack(side='top')

# initialization
context = internalLogic.Context()
city_num = -1
city_name = "广州"

# Label and input
model_information = tk.Label(window, text=f"您正在使用{context.get_model_name()}于{city_name}城市")
model_information.place(x=90, y=100)
tk.Label(window, text='始发站：').place(x=90, y=150)
tk.Label(window, text='终止站：').place(x=90, y=190)

# create input box
var_start_station = tk.StringVar()
entry_start_station = tk.Entry(window, textvariable=var_start_station)
entry_start_station.place(x=150, y=150)

var_end_station = tk.StringVar()
entry_end_station = tk.Entry(window, textvariable=var_end_station)
entry_end_station.place(x=150, y=190)


def count():
    # TODO 完成差错控制，因为这个getedge会报错
    tk.messagebox.showinfo(title="计算结果",
                           message=f"{context.using_strategy(var_start_station.get(), var_end_station.get())}")


def change_model():
    global context

    def change_to_shortest_path():
        nonlocal change_model_window
        context.change_model(internalLogic.ShortestPath(city_num))
        global model_information
        model_information['text'] = f"您正在使用{context.get_model_name()}于{city_name}城市"
        change_model_window.destroy()

    def change_to_minimum_sites():
        nonlocal change_model_window
        context.change_model(internalLogic.MinimumSites(city_num))
        global model_information
        model_information['text'] = f"您正在使用{context.get_model_name()}于{city_name}城市"
        change_model_window.destroy()

    def change_to_minimum_transfer():
        nonlocal change_model_window
        context.change_model(internalLogic.MinimumTransfer(city_num))
        global model_information
        model_information['text'] = f"您正在使用{context.get_model_name()}于{city_name}城市"
        change_model_window.destroy()

    change_model_window = tkinter.Toplevel()
    change_model_window.title("选择你想要使用的模式")
    window.geometry("300x400")

    bt_shortest_path = tk.Button(change_model_window, text="最短距离模式", command=change_to_shortest_path)
    bt_shortest_path.place(x=50, y=20)
    bt_minimise_sites = tk.Button(change_model_window, text="最少站点模式", command=change_to_minimum_sites)
    bt_minimise_sites.place(x=50, y=50)
    bt_minimum_transfer = tk.Button(change_model_window, text="最少换乘模式", command=change_to_minimum_transfer)
    bt_minimum_transfer.place(x=50, y=90)


def quit_programme():
    window.destroy()


bt_count = tk.Button(window, text='计算', command=count)
bt_count.place(x=120, y=230)
bt_change_model = tk.Button(window, text='改变模式', command=change_model)
bt_change_model.place(x=170, y=230)
bt_quit_programme = tk.Button(window, text='退出', command=quit_programme)
bt_quit_programme.place(x=250, y=230)

# Main_Loop
window.mainloop()
