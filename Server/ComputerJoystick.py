import socket
import sys

import pygame

#Setting up server connection
HOST, PORT = "10.0.41.243", 9999


# Create a socket (SOCK_STREAM means a TCP socket)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)



#joystick
pygame.init()
pygame.joystick.init()

print(pygame.joystick.get_count())

try:
    # Connect to server and send data
    sock.connect((HOST, PORT))
    sock.sendall(bytes(data + "\n", "utf-8"))

    # Receive data from the server and shut down
    received = str(sock.recv(1024), "utf-8")
finally:
    sock.close()

print("Sent:     {}".format(data))
print("Received: {}".format(received))
