import socketserver
from gpiozero import Motor, OutputDevice

default = 0

def binary_to_dict(the_binary):
    jsn = ''.join(chr(int(x, 2)) for x in the_binary.split())
    d = json.loads(jsn)  
    return d

class MotorConoller():
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

    #left negative right positive
    def Yaw(value):
        m1speed -= value
        m2speed += value
        m3speed -= value
        m4speed += value
        
    #down positive up negative    
    def Pitch(value):
        m1speed += value
        m2speed += value
        m3speed -= value
        m4speed -= value

    #Left negative Right positive
    def Roll(value):
        m1speed -= value
        m2speed += value
        m3speed += value
        m4speed -= value
        
    def Thrust(value):
        default += value

    def setMotors(self):
        m1speed += default
        m2speed += default
        m3speed += default
        m4speed += default
        if(m1speed > 1):
            m1speed = 1
        elif(m1speed < 0):
            m1speed = 0
        if(m2speed > 1):
            m2speed = 1
        elif(m2speed < 0):
            m2speed = 0
        if(m3speed > 1):
            m3speed = 1
        elif(m3speed < 0):
            m3speed = 0
        if(m4speed > 1):
            m4speed = 1
        elif(m4speed < 0):
            m4speed = 0
        motor1.forward(m1speed)
        motor2.forward(m2speed)
        motor3.forward(m3speed)
        motor4.forward(m4speed)s
    

class MyTCPHandler(socketserver.BaseRequestHandler):
    def __init__(self):
        self.mc = MotorController()
    """
    The RequestHandler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """
    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        print("{} wrote:".format(self.client_address[0]))
        print(binary_to_dict(self.data))
        # just send back the same data, but upper-cased
        self.request.sendall(bytes("Recieved", "utf8"))
while True:
    if __name__ == "__main__":
        HOST, PORT = "0.0.0.0", 9999

    # Create the server, binding to localhost on port 9999
    server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()
    
