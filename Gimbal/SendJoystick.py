#!/usr/bin/env python

"""send-joystick.py: Reads a joystick device using pygame and sends the information via UDP."""


import socket, struct, time
import pygame

# Main configuration
#UDP_IP = "127.0.0.1" # Localhost (for testing)
UDP_IP = "192.168.15.98" # Vehicle IP address
UDP_PORT = 51001 # This port match the ones using on other scripts

frecuence = 10 # 100 hz loop cycle
update_rate = 1/frecuence
# Create UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    pygame.init()
    pygame.joystick.init()
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
except Exception,error:
    print "No joystick connected on the computer, "+str(error)

while True:
    current = time.time()
    elapsed = 0
    
    # Joystick reading
    pygame.event.pump()
    yaw     = int(joystick.get_axis(0)*1000)
    pitch    = int(joystick.get_axis(1)*1000)
    zoom      = int(joystick.get_axis(2)*1000)
    roll = int(joystick.get_axis(3)*1000)
    button0= int(joystick.get_button(0))
    button2= int(joystick.get_button(2))
    button3= int(joystick.get_button(3))
    button4= int(joystick.get_button(4))
    button5= int(joystick.get_button(5))
    button6= int(joystick.get_button(6))
   

    # Be sure to always send the data as floats
    # The extra zeros on the message are there in order for the other scripts to do not complain about missing information
    message = [yaw, pitch, zoom, roll, button0, button2, button3, button4, button5, button6]
    buf = struct.pack('>' + 'd' * len(message), *message)
    sock.sendto(buf, (UDP_IP, UDP_PORT))
    
    print message
   ## data, addr = sock.recvfrom(51001)
    ##ip = addr[0]
    ##port = addr[1]
    
    # Make this loop work at update_rate
    while elapsed < update_rate:
        elapsed = time.time() - current
