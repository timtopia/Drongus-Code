import socketserver
from gpiozero import Motor, OutputDevice

default = 0

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

    def Yaw(value):
        
    def Pitch(value):

    def Roll(value):

    def Thrust(value):
        default += value:

    def setMotors(self):
        
    

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
        print(self.data)
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
    
