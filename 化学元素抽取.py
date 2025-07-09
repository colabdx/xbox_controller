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

# 定义项目列表
items = [
    "五大本质 氢", "本质 氦", "通用种子 锂", "斯通 铍", "硼砂 硼", "碳",
    "硝石 氮", "氧气 氧", "混合物 氟", "精神 氖", "素迪姆 钠", "镁",
    "明矾 铝", "退火 硅", "磷", "硫磺 硫", "盐 氯", "氨水 氩", "钾",
    "查了 钙", "莱姆 钪", "沙 钛", "玻璃 钒", "黏土 铬", "锈 锰", "铁",
    "钴", "镍", "铜", "锌", "烧明矾 镓", "黄铜 锗", "砷", "砷硫 硒",
    "海盐 溴", "岩盐 氪", "醋 铷", "蒸馏醋 锶", "生石灰 钇", "碱石灰 镐",
    "木材 铌", "烟雾 钼", "余烬 锝", "钢 钌", "马加西特 铑", "铜绿 钯",
    "银", "辰砂 镉", "汽油罐 铟", "锡", "锑", "硫磺酸 碲", "东方水 碘",
    "王水 氙", "油 铯", "硫酸油 钡", "硫酸 镧系", "火 镧", "水 铈",
    "星座标记与工艺 镨", "白羊座 煅烧 钕", "金牛座 凝固 钷", "双子座 固着 钐",
    "巨蟹座 解决方案 铕", "狮子座 消化 钆", "处女座 蒸馏 铽", "天秤座 升华 镝",
    "天蝎座 分离 钬", "射手座 蜡化 铒", "魔羯座 发酵 铥", "水瓶座 乘法 镱",
    "双鱼座 投影 镥", "蛋壳 铪", "小体 钽", "灯芯 钨", "牛脂 铼", "肥皂 锇",
    "肥皂 铱", "铂", "金色的 金", "水星 汞", "精神融合 铊", "草地 铅",
    "铋", "雄黄 钋", "阿卡维纳 砹", "水浴 氡", "反驳 钫", "坩埚 镭",
    "空气 锕", "地球 钍", "其他工艺 镤", "白羊宫 组成 铀", "金牛宫 腐烂 镎", "双子宫 煮 钚",
    "巨蟹宫 解决 镅", "狮子宫 合并 锔", "处女宫 拿 锫", "天秤宫 净化 锎", "天蝎宫 蒸馏 锿", "射手宫 筛选 镄",
    "摩羯宫 沉淀物 钔", "水瓶宫 升华 锘", "双鱼宫 粉碎 铹", "品脱 𬬻", "顾虑 罕", "微量",
    "盎司", "英镑", "小时"
]

# 创建主窗口
root = tk.Tk()
root.title("Random Item Selector")

# 创建一个标签用于显示所选项目
selected_item_label = tk.Label(root, text="", font=("微软雅黑", 16))
selected_item_label.pack(pady=20)

def select_item():
    selected_item = random.choice(items)
    selected_item_label.config(text=selected_item)

# 创建一个按钮用于触发选择事件
select_button = tk.Button(root, text="Select an Item", command=select_item)
select_button.pack(pady=10)

def check_controller():
    for event in pygame.event.get():
        if event.type == pygame.JOYBUTTONDOWN:
            # A按钮(0)或B按钮(1)按下时触发选择
            if event.button in [0, 1]:
                select_item()
    root.after(50, check_controller)  # 每50ms检查一次手柄输入

# 启动手柄检测
root.after(50, check_controller)

# 运行主循环
root.mainloop()
