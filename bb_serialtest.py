import Adafruit_BBIO.UART as UART
import serial
 
UART.setup("UART1")
 
ser = serial.Serial(port = "/dev/ttyGS0", baudrate=9600)
ser.close()
ser.open()

if ser.isOpen():

    print "Serial is open!"

    while True:
        
        #data=ser.readline()

        ser.write("BEGIN Hey there! I see you! Do you see me? \n")

ser.close()