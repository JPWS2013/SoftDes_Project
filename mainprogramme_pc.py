# import modelclassdef as model
# import Dash as view
# import serial
# import threading
# from Tkinter import *
import time

def Database():
	ser=serial.Serial('/dev/ttyACM0', 9600) #Defines the serial port to use 

	ser.close()
	ser.open()

	if ser.isOpen():
		print "Database ready to receive data"

		while True:

			while True:
				raw_message=ser.readline()

				if raw_message[:2]=='&&':
					break
			
			message=raw_message.strip()
			command=message[2]
			data=message[4:]
			datalist=data.split(',')

			if command=='1':
				model.store_sensor(datalist[0], datalist[1], datalist[2])
				# model.print_loc()

			if command=='2':
				model.store_data_pot(datalist[0], datalist[1], datalist[2])


			if command=='3':
				model.store_data_accel(datalist[0], datalist[1], datalist[2])

if __name__=='__main__':
	th1=threading.Thread(target=Database)
	th1.setDaemon(True)
	model=model.Model()
	th1.start()

	root=Tk()
	dash=view.View(root, model)

	th2=threading.Thread(target=dash.updating)
	th2.start()
	root.mainloop()

	# th.stop()
	