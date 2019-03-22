from tkinter import *
import MotorController
import MyJoystick
import time

root = Tk()
root.title("Drongus Debug")
root.geometry('500x500')
mc = MotorController.MotorController()
joy = MyJoystick.Joystick()

print("Test1")

TL = DoubleVar()
BL = DoubleVar()
TR = DoubleVar()
BR = DoubleVar()

TOP_LEFT = Label(root, textvariable=TL)
BOT_LEFT = Label(root, textvariable=BL)
TOP_RIGHT = Label(root, textvariable=TR)
BOT_RIGHT = Label(root, textvariable=BR)

TOP_LEFT.grid(column=0, row=0)
BOT_LEFT.grid(column=0, row=1)
TOP_RIGHT.grid(column=1, row=0)
BOT_RIGHT.grid(column=1, row=1)

TL.set(0.5)

while True:
    joy = MyJoystick.Joystick()
    values = joy.update()

    TL.set(values["LEFT_X"])
    BL.set(values["LEFT_Y"])
    TR.set(values["RIGHT_X"])
    BR.set(values["RIGHT_Y"])
    
    mc.reset()
    mc.roll(values["LEFT_X"])
    mc.pitch(values["LEFT_Y"])
    mc.yaw(values["RIGHT_X"])
    mc.thrust(values["RIGHT_Y"])
    print("Test2")

    time.sleep(0.1)

    root.mainloop()
