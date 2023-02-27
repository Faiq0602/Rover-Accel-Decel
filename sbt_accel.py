import serial
import time
r = 0.5
s = 192
e = 255
for i in range(s,e):
	b = i.to_bytes(1,'little')
	SerialPortObj = serial.Serial('/dev/ttyUSB0')
	SerialPortObj.write(bytes(b))
	time.sleep(r)

print('\nStatus -> ',SerialPortObj) 
 
SerialPortObj.close()    
