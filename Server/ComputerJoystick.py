import socket
import sys
import time
import json
import pygame


#Setting up server connection
HOST, PORT = "169.254.37.119", 9999






#truncating the floats from the axis
def truncate(n):
    return int(n * 1000) / 1000

#joystick
pygame.init()
pygame.joystick.init()

joystick_count = pygame.joystick.get_count()

done = False
while done==False:
    pygame.event.get()
    for i in range(joystick_count):
        
        joystick = pygame.joystick.Joystick(i)
        joystick.init()

        axes = joystick.get_numaxes()
        print(axes)
        vals = []
        for j in range(axes):
            axis = joystick.get_axis(j)
            print(truncate(axis))
            vals.append(truncate(axis))

        
        vals[1] = vals[1] * -1
        vals[3] = vals[3] * -1

        #vals[0] = Yaw
        #vals[1] = Thrust
        #vals[2] = Roll
        #vals[3] = Pitch

        Rotations = {
            "Yaw": vals[0],
            "Thrust": vals[1],
            "Roll": vals[2],
            "Pitch": vals[3]
        }

        print(Rotations)

    
    try:
        # Create a socket (SOCK_STREAM means a TCP socket)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Connect to server and send data
        sock.connect((HOST, PORT))
        print("Asdf")
        sock.sendall(bytearray(json.dumps(Rotations), 'utf8'))

        # Receive data from the server and shut down
        received = str(sock.recv(1024), "utf-8")
        sock.close
    finally:
        sock.close()

    print("Received: {}".format(received))
    time.sleep(.01)
