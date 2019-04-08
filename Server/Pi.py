import socketserver
from gpiozero import Motor, OutputDevice
import json

default = 0

def binary_to_dict(the_binary):
    d = json.loads(str(the_binary, "utf-8"))  
    return d

class MotorController():
    #Motor1 = Back Left
    motor1 = Motor(24, 27)
    motor1_enable = OutputDevice(5, initial_value=0)
    #Motor2 = Back Right
    motor2 = Motor(6, 22)
    motor2_enable = OutputDevice(17, initial_value=0)
    #Motor3 = Front Right
    motor3 = Motor(23, 16)
    motor3_enable = OutputDevice(12, initial_value=0)
    #Motor4 = Front Left
    motor4 = Motor(13, 18)
    motor4_enable = OutputDevice(25, initial_value=0)
    
    m1speed=0
    m2speed=0
    m3speed=0
    m4speed=0

    truem1speed = 0
    truem2speed = 0
    truem3speed = 0
    truem4speed = 0

    #left negative right positive
    def Yaw(self, value):
        self.m1speed -= value
        self.m2speed += value
        self.m3speed -= value
        self.m4speed += value
        
    #down positive up negative    
    def Pitch(self, value):
        self.m1speed += value
        self.m2speed += value
        self.m3speed -= value
        self.m4speed -= value

    #Left negative Right positive
    def Roll(self, value):
        self.m1speed -= value
        self.m2speed += value
        self.m3speed += value
        self.m4speed -= value
        
    def Thrust(self, value):
        global default
        default += value

    def setMotors(self):
        global default
        self.truem1speed = self.m1speed + default
        self.truem2speed = self.m2speed + default
        self.truem3speed = self.m3speed + default
        self.truem14peed = self.m4speed + default
        if(self.truem1speed > 1):
            self.truem1speed = 1
        elif(self.truem1speed < 0):
            self.truem1speed = 0
        if(self.truem2speed > 1): 
            self.truem2speed = 1
        elif(self.truem2speed < 0):
            self.truem2speed = 0
        if(self.truem3speed > 1):
            self.truem3speed = 1
        elif(self.truem3speed < 0):
            self.truem3speed = 0
        if(self.truem4speed > 1):
            self.truem4speed = 1
        elif(self.truem4speed < 0):
            self.truem4speed = 0
        self.motor1.forward(self.truem1speed)
        self.motor2.forward(self.truem2speed)
        self.motor3.forward(self.truem3speed)
        self.motor4.forward(self.truem4speed)

    def print(self):
        return (str(self.truem1speed) + ',' + str(self.truem2speed) + ',' + str(self.truem3speed) + ',' + str(self.truem4speed))

class MyTCPHandler(socketserver.BaseRequestHandler):
    mc = MotorController()
    #def __init__(self, *args, **kwargs):
    #    super(MyTCPHandler, self).__init__(*args, **kwargs)
    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        print("{} wrote:".format(self.client_address[0]))
        dictionary = binary_to_dict(self.data)
        if abs(dictionary["Yaw"])>.1:
            self.mc.Yaw(dictionary["Yaw"])
        if abs(dictionary["Pitch"])>.1:    
            self.mc.Pitch(dictionary["Pitch"])
        if abs(dictionary["Roll"])>.1:
            self.mc.Roll(dictionary["Roll"])
        if abs(dictionary["Thrust"])>.1:
            self.mc.Thrust(dictionary["Thrust"])
        self.mc.setMotors()
        print(self.mc.print())
        # just send back the same data, but upper-cased
        self.request.sendall(bytes("Recieved", "utf8"))
        

if __name__ == "__main__":
    HOST, PORT = "0.0.0.0", 9999

    # Create the server, binding to localhost on port 9999
    server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()
    
