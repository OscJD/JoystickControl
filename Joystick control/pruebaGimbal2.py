import time
import serial

# Iniciando conexión serial
arduinoPort = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)

# Retardo para establecer la conexión serial
time.sleep(1.8)


#while True:

## arduinoPort.write(str(unichr(62)))
## arduinoPort.write(str(unichr(67)))
## arduinoPort.write(str(unichr(13)))
## arduinoPort.write(str(unichr(80)))
## 
## arduinoPort.write(str(unichr(2)))
## 
## arduinoPort.write(str(unichr(81)))
## arduinoPort.write(str(unichr(0)))
## arduinoPort.write(str(unichr(0)))
## arduinoPort.write(str(unichr(0)))
## 
## arduinoPort.write(str(unichr(81)))
## arduinoPort.write(str(unichr(0)))
## arduinoPort.write(str(unichr(227)))
## arduinoPort.write(str(unichr(8)))
## 
## arduinoPort.write(str(unichr(81)))
## arduinoPort.write(str(unichr(0)))
## arduinoPort.write(str(unichr(28)))
## arduinoPort.write(str(unichr(7)))
##
## arduinoPort.write(str(unichr(3)))
##
## time.sleep(5)

arduinoPort.write(b62)
arduinoPort.write('67')
arduinoPort.write('13')
arduinoPort.write('80')

arduinoPort.write('2')
 
arduinoPort.write('81')
arduinoPort.write('0')
arduinoPort.write('0')
arduinoPort.write('0')
 
arduinoPort.write('81')
arduinoPort.write('0')
arduinoPort.write('0')
arduinoPort.write('0')
 
arduinoPort.write('81')
arduinoPort.write('0')
arduinoPort.write('0')
arduinoPort.write('0')

arduinoPort.write('245')

time.sleep(5)

print("Ya") 

#getSerialValue = arduinoPort.readline()
#getSerialValue = arduinoPort.read()
#getSerialValue = arduinoPort.read(6)
#print '\nValor retornado de Arduino: %s' % (getSerialValue)

# Cerrando puerto serial
arduinoPort.close()




	# Se borra cualquier data que haya quedado en el buffer
#	arduinoPort.flushInput()  
#	arduinoPort.setDTR()  
	
