
import tkinter as tk
import random
import pygame
from threading import Thread

class DNAGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("DNA Generator")
        
        # 初始化pygame手柄支持
        pygame.init()
        pygame.joystick.init()
        self.joystick = None
        if pygame.joystick.get_count() > 0:
            self.joystick = pygame.joystick.Joystick(0)
            self.joystick.init()
            print(f"检测到手柄: {self.joystick.get_name()}")
        
        # 创建按钮和标签
        self.human_button = tk.Button(root, text="制作人类DNA (A键)", command=self.generate_human_dna)
        self.human_button.pack()
        
        self.dog_button = tk.Button(root, text="制作狗DNA (B键)", command=self.generate_dog_dna)
        self.dog_button.pack()
        
        self.human_label = tk.Label(root, text="")
        self.human_label.pack()
        
        self.dog_label = tk.Label(root, text="")
        self.dog_label.pack()
        
        # 启动手柄检测线程
        if self.joystick:
            Thread(target=self.check_joystick, daemon=True).start()

    def generate_human_dna(self):
        self.human_label.config(text=self.generate_dna(23), wraplength=400)

    def generate_dog_dna(self):
        self.dog_label.config(text=self.generate_dna(39), wraplength=400)

    def generate_dna(self, length):
        bases = ["A-T，", "T-A，", "C-G，", "G-C，"]
        return ''.join(random.choice(bases) for _ in range(length))

    def check_joystick(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.JOYBUTTONDOWN:
                    if event.button == 0:  # A键
                        self.root.after(0, self.generate_human_dna)
                    elif event.button == 1:  # B键
                        self.root.after(0, self.generate_dog_dna)

# 创建窗口并运行应用
root = tk.Tk()
app = DNAGeneratorApp(root)
root.mainloop()
