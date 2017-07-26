#!/usr/bin/env python

import time, threading

import GimbalControl as gimbal


frecuence=10
update_rate =1/frecuence  # 100 hertz update rate
rcCMD = [1500,1500,1500,1000,1000,1000,1000,1000]
gimbal.move_angle(0,0)
time.sleep(3)
def sendCommands():

    try:
        while True:
            if gimbal.active:
                current = time.time()
                elapsed = 0
                # Part for applying commands to the vehicle.
                # Channel order in mavlink:   roll, pitch, throttle, yaw
                # Channel order in optitrack: roll, pitch, yaw, throttle
                # Remember to check min/max for rc channels on APM Planner
                yaw     = gimbal.message[0]
                pitch    = gimbal.message[1]
                zoom = gimbal.message[2]
                roll      = gimbal.message[3]
                if(yaw<100 and yaw>-100):
                    yaw=0
                if(pitch<100 and pitch>-100):
                    pitch=0

                gimbal.speed(-pitch/100,yaw/100)
                gimbal.ReadPos()
                #print cadena
                while elapsed < update_rate:
                    elapsed = time.time() - current

    except Exception,error:
        print "Error on sendCommands thread: "+str(error)
        sendCommands(self,message,())

""" Section that starts the threads """
try:
    JoystickThread = threading.Thread(target=sendCommands)
    JoystickThread.daemon=True
    JoystickThread.start()
    gimbal.startTwisted()



except Exception as error:
    print "Error on main script thread: "+str(error)


