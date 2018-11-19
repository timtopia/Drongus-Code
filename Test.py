import MotorController
import pygame
pygame.init()
mc = MotorController.MotorController()
multiplier = 5;
pygame.joystick.init()
joystick = pygame.joystick.Joystick(0)
joystick.init()
clock = pygame.time.Clock()


while True:
    axis1 = joystick.get_axis(1)
    print(axis1)
    #mc.thrust(axis1*multiplier)
    clock.tick(20)
