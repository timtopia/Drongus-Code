import MotorController
import MyJoystick
import time

#write a for loop that prints out all the button values

mc = MotorController.
joy = MyJoystick.Joystick()

while True:
    print("\n" * 100)
    values = joy.update()

    for i in values:
        print("{}\t{}".format(i, values[i]))

    time.sleep(0.1)
            
