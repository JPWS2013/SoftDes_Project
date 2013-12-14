import modelclassdef as model
import textviewdef as view
import serial

model=model.Model()
view=view.TextView(model)
txfull=False

ser=serial.Serial('/dev/ttyACM0', 9600) #Defines the serial port to use 

ser.close()
ser.open()

while True:

	while txfull==False:
		raw_message=ser.readline()

		if raw_message[:2]=='&&':
			break
	
	message=raw_message.strip()
	command=message[2]
	data=message[4:]
	datalist=data.split(',')

	if command=='1':
		model.store_sensor(datalist[0], datalist[1], datalist[2])
		model.print_loc()

	if command=='2':
		model.store_data_pot(datalist[0], datalist[1], datalist[2])