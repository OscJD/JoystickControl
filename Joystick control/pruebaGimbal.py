import time
import serial
import numpy as np 

# Iniciando conexión serial
arduinoPort = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)

# Retardo para establecer la conexión serial
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
    #SYL=255
    #SYH=127
    SCR=(SPH+SPL+SYH+SYL+1)%256
    print(SPL)
    print(SPH)
    print(SYL)
    print(SYH)
    print(SCR)
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

    


speed(-10,-10)
time.sleep(1)
move_angle(0,30)
time.sleep(7)
 

#getSerialValue = arduinoPort.readline()
#getSerialValue = arduinoPort.read()
#getSerialValue = arduinoPort.read(6)
#print '\nValor retornado de Arduino: %s' % (getSerialValue)

# Cerrando puerto serial
arduinoPort.close()




	# Se borra cualquier data que haya quedado en el buffer
#	arduinoPort.flushInput()  
#	arduinoPort.setDTR()  
	
