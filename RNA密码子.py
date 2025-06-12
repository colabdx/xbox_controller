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

# 定义一个函数来生成随机密码子并显示相应的氨基酸或密码子名称
def generate_codon():
    codons = ["UUU", "UUC", "UUA", "UUG", "CUU", "CUA", "CUC", "CUG", "AUU", "AUC", "AUA", "AUG", "GUU", "GUC", "GUA", "GUG",
              "UCU", "UCC", "UCA", "UCG", "CCU", "CCC", "CCA", "CCG", "ACU", "ACC", "ACA", "ACG", "GCU", "GCC", "GCA", "GCG",
              "UAU", "UAC", "UAA", "UAG", "UGA", "CAU", "CAC", "CAA", "CAG", "AAU", "AAC", "AAA", "AAG", "GAU", "GAC", "GAA", "GAG",
              "UGU", "UGC", "UGG", "CGU", "CGC", "CGA", "CGG", "AGA", "AGG", "AGU", "AGC", "GGU", "GGC", "GGA", "GGG"]
    amino_acids = {
        "UUU": "苯丙", "UUC": "苯丙", "UUA": "亮", "UUG": "亮", "CUU": "亮", "CUA": "亮", "CUC": "亮", "CUG": "亮",
        "AUU": "异亮", "AUC": "异亮", "AUA": "异亮", "AUG": "旦", "GUU": "缬", "GUC": "缬", "GUA": "缬", "GUG": "缬",
        "UCU": "丝", "UCC": "丝", "UCA": "丝", "UCG": "丝", "CCU": "脯", "CCC": "脯", "CCA": "脯", "CCG": "脯",
        "ACU": "苏", "ACC": "苏", "ACA": "苏", "ACG": "苏", "GCU": "丙", "GCC": "丙", "GCA": "丙", "GCG": "丙",
        "UAU": "酪", "UAC": "酪", "UAA": "终止密码", "UAG": "终止密码", "UGA": "终止密码", "CAU": "组", "CAC": "组",
        "CAA": "谷氨酰胺", "CAG": "谷氨酰胺", "AAU": "天门冬酰胺", "AAC": "天门冬酰胺", "AAA": "赖", "AAG": "赖",
        "GAU": "天门冬", "GAC": "天门冬", "GAA": "谷", "GAG": "谷", "UGU": "半胱", "UGC": "半胱", "UGG": "色",
        "CGU": "精", "CGC": "精", "CGA": "精", "CGG": "精", "AGA": "精", "AGG": "精", "AGU": "丝", "AGC": "丝",
        "GGU": "甘", "GGC": "甘", "GGA": "甘", "GGG": "甘"
    }
    
    # 随机生成三个核苷酸
    codon = ''.join(random.choices('ACUG', k=3))
    result = amino_acids.get(codon, "未知密码子")
    
    # 更新标签显示结果
    result_label.config(text=f"密码子: {codon}\n氨基酸/密码子名称: {result}")

# 创建主窗口
root = tk.Tk()
root.title("密码子转译器")

# 创建一个按钮，点击时调用generate_codon函数
generate_button = tk.Button(root, text="生成密码子", command=generate_codon)
generate_button.pack(pady=20)

# 创建一个标签，用于显示结果
result_label = tk.Label(root, text="点击按钮生成密码子")
result_label.pack(pady=20)

def check_controller():
    for event in pygame.event.get():
        if event.type == pygame.JOYBUTTONDOWN:
            # A按钮(0)或B按钮(1)按下时触发选择
            if event.button in [0, 1]:
                generate_codon()
    root.after(50, check_controller)  # 每50ms检查一次手柄输入

# 启动手柄检测
root.after(50, check_controller)

# 运行主循环
root.mainloop()
