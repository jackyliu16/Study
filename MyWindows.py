"""
Author： 刘逸珑
Time：   2021/12/28 20:22

@Reference:
    https://blog.csdn.net/Jason_WangYing/article/details/108916236
    https://blog.csdn.net/weixin_40450867/article/details/81431718

"""
import json
import tkinter as tk

# windows
import GetData
from AdjGraph import AdjMatrix

window = tk.Tk()
window.title("欢迎进入地铁线路规划系统")
window.geometry("960x960")
# put photo
canvas = tk.Canvas(window, height=962, width=1098)
image_file = tk.PhotoImage(file='Line.png')
image = canvas.create_image(0, 0, anchor='nw', image=image_file)
canvas.pack(side='top')

# Label and input
tk.Label(window, text="您现在正在使用最小距离模式").place(x=90, y=100)
tk.Label(window, text='始发站：').place(x=90, y=150)
tk.Label(window, text='终止站：').place(x=90, y=190)

# create input box
var_start_station = tk.StringVar()
entry_start_station = tk.Entry(window, textvariable=var_start_station)
entry_start_station.place(x=150, y=150)

var_end_station = tk.StringVar()
entry_end_station = tk.Entry(window, textvariable=var_end_station)
entry_end_station.place(x=150, y=190)

# initialization
model = 0

# open the data GetData.py create and read it in memory
GetData.initialization()
with open('original_data.json', 'r') as File:
    json_data = json.load(File)
graph = AdjMatrix(json_data, model)


# 计算函数
def count():
    print("count")


def change_model():
    print('changeModel')


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
