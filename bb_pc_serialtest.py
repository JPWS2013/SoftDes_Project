import serial
import time

ser=serial.Serial('/dev/ttyACM0', 9600) #Defines the serial port to use 

ser.close()
ser.open()

if ser.isOpen():
	print "It's open"

# time.sleep(3)

# ser.write("Hello World! \n")
rxfull = False

while rxfull==False:

	message=ser.readline()

	if message[:5]=="BEGIN":
		break

print message