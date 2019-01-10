import MotorController
import MyJoystick
import time

#write a for loop that prints out all the button values

mc = MotorController.MotorController()
joy = MyJoystick.Joystick()

while True:
    print("\n" * 500)
    values = joy.update()

    for i in values:
        print("{}\t{}".format(i, values[i]))

    mc.reset()
    mc.roll(values["LEFT_X"])
    mc.pitch(values["LEFT_Y"])
    mc.yaw(values["RIGHT_X"])
    mc.thrust(values["RIGHT_Y"])
    mc.display()
    
    time.sleep(0.1)
            
