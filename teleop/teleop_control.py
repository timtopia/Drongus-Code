import socketserver
from gpiozero import Motor, OutputDevice
import json
from enum import Enum

class MotorController():
    class MotorIDs(Enum):
        BL = 0 
        BR = 1
        FL = 2
        FR = 3

    motor_speeds = [0,0,0,0]
    max_thrust_speed = 0.1

    def set_all_motors(value):
        for motor_id in MotorIDs:
            self.motor_speeds[motor_id] += value*max_thrust_speed


    def thrust(joy_val):
        set_all_motors(joy_val)
        print(self.motor_speeds)
        

class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        self.data = self.request.recv(1024).strip()
        joystick_values = json.loads(str(self.data,"utf-8"))
        print(joystick_values)
        thrust(joystick_values["Thrust"])
        
if __name__=="__main__":
    HOST,PORT = "0.0.0.0", 9999
    server = socketserver.TCPServer((HOST, PORT),MyTCPHandler)
    server.serve_forever()
