import modelclassdef as model
import dash_view as view
import serial

model=model.Model()
view=view.TextView(model)

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