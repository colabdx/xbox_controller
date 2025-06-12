import tkinter as tk
import random
import pygame
from pygame import joystick

# 创建主窗口
root = tk.Tk()
root.geometry("600x400")
root.title("白兔堂岛屿生活")

# 初始化pygame和手柄
pygame.init()
joystick.init()
if joystick.get_count() > 0:
    controller = joystick.Joystick(0)
    controller.init()
    
# 初始金额
balance = 1000

# 岛屿及其价格
islands_price = {
'Азорские острова C' : 10,
'Остров Инувик G,F': 20,
'Остров Кальяо D, bB': 100,
'Остров Кейп-Код A, Es': 80,
'Остров Санта-Барбара E, As': 100,
'Остров Диксон B, Des': 50,
'Остров Нарвик Fis, Ges': 30,
'Остров Ном Cis, Ces': 80,
'Остров Перт Gis, Fes': 100,
'Остров Вальпараисо Dis, Hesses': 40,
'Остров Фейрвил Ais, Eses': 50,
'Остров Монтевидео Eis, Ases': 60,
'Остров Левек His, Deses': 70,
'Остров Вангануи Fises, Geses': 100,
'Остров Оби D, Ceses': 20,
'Остров Время-Пространство A, Fesses': 70
}

# 抽取岛屿
def draw_island():
    global balance
    island = random.choice(list(islands_price.keys()))
    price = islands_price[island]
    balance += price
    balance_label.config(text=f"我的金额: ${balance}")
    island_label.config(text=f"抽取的岛屿: {island}")



# 创建金额标签
balance_label = tk.Label(root, text=f"我的金额: ${balance}", font=('Helvetica', 16))
balance_label.pack()

# 创建抽取岛屿按钮
draw_button = tk.Button(root, text="抽取岛屿", command=draw_island, font=('Helvetica', 16))
draw_button.pack()



# 创建岛屿标签
island_label = tk.Label(root, text="尚未抽取任何岛屿", font=('Helvetica', 16))
island_label.pack()

def check_controller1():
    for event in pygame.event.get():
        if event.type == pygame.JOYBUTTONDOWN:
            # A按钮(0)或B按钮(1)按下时触发选择
            if event.button in [0, 1]:
                draw_island()
    root.after(20, check_controller1)  

# 启动手柄检测
root.after(20, check_controller1)


from tkinter import ttk
import pygame
from pygame import joystick
    


# 定义一个函数，用于在次窗口中显示文本
def show_info():

    # 创建一个次窗口
    new_window = tk.Toplevel(root)
    new_window.title("岛屿信息")
    new_window.geometry("300x300")

    # 定义一个字典，用于存储岛屿和对应的数字
    islands_info = {
'Азорские острова C' : 10,
'Остров Инувик G,F': 20,
'Остров Кальяо D, bB': 100,
'Остров Кейп-Код A, Es': 80,
'Остров Санта-Барбара E, As': 100,
'Остров Диксон B, Des': 50,
'Остров Нарвик Fis, Ges': 30,
'Остров Ном Cis, Ces': 80,
'Остров Перт Gis, Fes': 100,
'Остров Вальпараисо Dis, Hesses': 40,
'Остров Фейрвил Ais, Eses': 50,
'Остров Монтевидео Eis, Ases': 60,
'Остров Левек His, Deses': 70,
'Остров Вангануи Fises, Geses': 100,
'Остров Оби D, Ceses': 20,
'Остров Время-Пространство A, Fesses': 70
    }

    # 创建一个列表框，用于显示岛屿信息
    listbox = tk.Listbox(new_window)
    listbox.pack(fill="both", expand=True)

    # 遍历字典，将岛屿信息添加到列表框中
    for island, info in islands_info.items():
        listbox.insert(tk.END, f"{island}: {info}")


# 在主窗口中添加一个按钮，用于打开次窗口
button = ttk.Button(root, text="显示岛屿信息", command=show_info)
button.pack(pady=20)

# 创建一个标签用于显示公司名称
company_label = tk.Label(root, text="©2024-2026 青岛耶胡迪梅纽因音乐学校", font=("微软雅黑", 12))
company_label.pack(side="bottom", anchor="sw")  # 将标签放置在窗口底部

def check_controller2():
    for event in pygame.event.get():
        if event.type == pygame.JOYBUTTONDOWN:
            if event.button in [2, 3]:
                show_info()
    root.after(50, check_controller2)  # 每50ms检查一次手柄输入

# 启动手柄检测
root.after(50, check_controller2)

# 运行主循环
root.mainloop()


