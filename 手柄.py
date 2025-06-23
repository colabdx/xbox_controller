import pygame

pygame.init()
pygame.joystick.init()
joystick = pygame.joystick.Joystick(0)
joystick.init()

while True:
    for event in pygame.event.get():
        if event.type == pygame.JOYBUTTONDOWN:
            print(f"按钮 {event.button} 按下")
        elif event.type == pygame.JOYAXISMOTION:
            print(f"轴 {event.axis} 值: {event.value:.2f}")
        elif event.type == pygame.JOYHATMOTION:
            print(f"方向键状态: {event.value}")
