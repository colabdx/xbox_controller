import tkinter as tk
import random
import pygame
from pygame import joystick

# 初始化pygame和手柄
pygame.init()
joystick.init()
if joystick.get_count() > 0:
    controller = joystick.Joystick(0)
    controller.init()
    
# 氨基酸列表
amino_acids = [
    "甘氨酸", "丙氨酸", "缬氨酸", "亮氨酸", "异亮氨酸", "甲硫氨酸", "脯氨酸",
    "色氨酸", "丝氨酸", "酪氨酸", "半胱氨酸", "苯丙氨酸", "天冬酰胺", "谷氨酰胺",
    "苏氨酸", "天门冬氨酸", "谷氨酸", "赖氨酸", "精氨酸", "组氨酸"
]

# 随机选择氨基酸并更新标签的函数
def choose_amino_acid():
    selected_acid = random.choice(amino_acids)
    result_label.config(text=selected_acid)

# 创建窗口
root = tk.Tk()
root.title("随机抽取氨基酸")

# 创建按钮和标签
choose_button = tk.Button(root, text="抽取氨基酸", font=('微软雅黑', 32) , command=choose_amino_acid)
choose_button.pack()

result_label = tk.Label(root, font=('微软雅黑', 32) , text="")
result_label.pack()

def check_controller():
    for event in pygame.event.get():
        if event.type == pygame.JOYBUTTONDOWN:
            # A按钮(0)或B按钮(1)按下时触发选择
            if event.button in [0, 1]:
                choose_amino_acid()
    root.after(50, check_controller)  # 每50ms检查一次手柄输入

# 启动手柄检测
root.after(50, check_controller)

# 运行窗口的主循环
root.mainloop()
