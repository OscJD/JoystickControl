#!/usr/bin/env python

import struct, time, socket
from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor
from twisted.internet import task
import serial
import numpy as np

UDPport = 51001
message = [1500,1500,1500,1000,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
active = False

getSerialValue=np.zeros((1,100))
arduinoPort = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)


time.sleep(1.8)


def move_angle(pitch,yaw):
    angleP=int(pitch*45.5111)
    angleY=int(yaw*45.5111)
    PL=np.uint8(abs(angleP))
    if angleP<0:
        PH=127-(np.int8(abs(angleP)>>8))+128
    else:
        PH=np.int8(abs(angleP)>>8)
    YL=np.uint8(abs(angleY))
    if angleY<0:
        YH=127-(np.int8(abs(angleY)>>8))+128
    else:
        YH=np.int8(abs(angleY)>>8)
    SCR=(243+PH+PL+YH+YL+2)%256
    arduinoPort.write((unichr(62)))
    arduinoPort.write((unichr(67)))
    arduinoPort.write((unichr(13)))
    arduinoPort.write((unichr(80)))
    arduinoPort.write((unichr(2)))
    arduinoPort.write((chr(81)))
    arduinoPort.write((chr(0)))
    arduinoPort.write((chr(0)))
    arduinoPort.write((chr(0)))
    arduinoPort.write((chr(81)))
    arduinoPort.write((chr(0)))
    arduinoPort.write((chr(PL)))
    arduinoPort.write((chr(PH)))
    arduinoPort.write((chr(81)))
    arduinoPort.write((chr(0)))
    arduinoPort.write((chr(YL)))
    arduinoPort.write((chr(YH)))
    arduinoPort.write((chr(SCR)))



def speed(Spitch,Syaw):
    speedP=int(Spitch*8.19175)
    speedY=int(Syaw*8.19175)

    if speedP<0:
        SPL=255-np.uint8(abs(speedP))
        SPH=63-(np.int8(abs(speedP)>>8))+64
    else:
        SPL=np.uint8(abs(speedP))
        SPH=np.int8(abs(speedP)>>8)

    if speedY<0:
        SYL=255-np.uint8(abs(speedY))
        SYH=63-(np.int8(abs(speedY)>>8))+64
    else:
        SYL=np.uint8(abs(speedY))
        SYH=np.int8(abs(speedY)>>8)

    SCR=(SPH+SPL+SYH+SYL+1)%256

    arduinoPort.write((unichr(62)))
    arduinoPort.write((unichr(67)))
    arduinoPort.write((unichr(13)))
    arduinoPort.write((unichr(80)))
    arduinoPort.write((unichr(1)))
    arduinoPort.write((chr(0)))
    arduinoPort.write((chr(0)))
    arduinoPort.write((chr(0)))
    arduinoPort.write((chr(0)))
    arduinoPort.write((chr(SPL)))
    arduinoPort.write((chr(SPH)))
    arduinoPort.write((chr(0)))
    arduinoPort.write((chr(0)))
    arduinoPort.write((chr(SYL)))
    arduinoPort.write((chr(SYH)))
    arduinoPort.write((chr(0)))
    arduinoPort.write((chr(0)))
    arduinoPort.write((chr(SCR)))

def ReadPos():
    arduinoPort.write((unichr(62)))
    arduinoPort.write((unichr(23)))
    arduinoPort.write((unichr(1)))
    arduinoPort.write((unichr(24)))
    arduinoPort.write((unichr(1)))
    arduinoPort.write((unichr(1)))

    i=0

    while(i<70):
        getSerialValue[0,i] = ord(arduinoPort.read(1))
        #print (getSerialValue[0,i])
        i=i+1

    pl=int(getSerialValue[0,56])
    ph=int(getSerialValue[0,57])
    yl=int(getSerialValue[0,58])
    yh=int(getSerialValue[0,59])


    if(ph)<127:
        ph=int(getSerialValue[0,57])*256
        p=(ph+pl)/45.511
    else:
        ph=int(getSerialValue[0,57]-128)*256

    if(yh)<127:
        yh=int(getSerialValue[0,59])*256
        y=(yh+yl)/45.511
    else:
        yh=int(getSerialValue[0,59]-128)*256
        y=((yh+yl)/45.511)-720

    #print (p,y)

    i=0
    arduinoPort.flushInput()


def closeSer():
    arduinoPort.close()

def timeout():
    global active, message
    if not active:
        # There is no UDP data, so give message "safe" commands
        message = [1500,1500,1500,1000,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    active = False

class twistedUDP(DatagramProtocol):

    def datagramReceived(self, data, (host, port)):
        global message, active
        active = True
        # In case of failure on receiving, check this:
        numOfValues = len(data) / 8
        mess=struct.unpack('>' + 'd' * numOfValues, data)
        message = [ round(element,6) for element in mess ]
        #print message
        #UDPmess.insert(0,time.time())
        #self.sendMSG(cfg.line,(cfg.UDPip, cfg.UDPportOut))
        #self.sendMSG("1",(cfg.UDPip, cfg.UDPportOut))
    #def sendMSG(self, data, (host, port)):

     #    self.transport.write(data, (host, port))

def startTwisted():
    l = task.LoopingCall(timeout)
    l.start(0.5) # Check for disconnection each 0.5 and send neutral commands
    reactor.listenUDP(UDPport, twistedUDP())
    reactor.run()






