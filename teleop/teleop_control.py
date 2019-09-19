import socketserver
from gpiozero import Motor, OutputDevice
import json
from enum import Enum

class MotorController:
    class MotorIDs(Enum):
        BL = 0 
        BR = 1
        FL = 2
        FR = 3

    motor_speeds = [0,0,0,0]
    max_thrust_speed = 0.1

    def set_all_motors(self, speed):
        for motor_id in MotorIDs:
            self.motor_speeds[motor_id] += speed

class PID:
    def __init__(self, k_p, k_i, k_d):
        self.k_p = k_p 
        self.k_i = k_i
        self.k_d = k_d
        self.integral = 0

    def update(self,target,current):
        error = target - current 
        derivative = self.previous_error - error
        output = self.k_p*error + self.k_i*self.integral + self.k_d*derivative

        self.previous_error = error
        self.integral += error

        return output
        
class Drone:
    motors = MotorController()
    max_target_accel = 1
    thrust_pid = PID(1,0,0)

    def thrust(self, joy_val):
        target_acceleration = 9.8 #graviational constant
        target_acceleration += joy_val * max_target_accel

        error = target_acceleration - acceleration_global_z
        output = thrust_pid.update(error)
        motor.set_all_motors(output)

    def run_teleop(self,joystick_values):
        self.thrust(joystick_values["Thrust"])
        

class MyTCPHandler(socketserver.BaseRequestHandler):
    drone = Drone()
    def handle(self):
        self.data = self.request.recv(1024).strip()
        joystick_values = json.loads(str(self.data,"utf-8"))
        self.drone.run_teleop(joystick_values)
        
if __name__=="__main__":
    HOST,PORT = "0.0.0.0", 9999
    server = socketserver.TCPServer((HOST, PORT),MyTCPHandler)
    server.serve_forever()
