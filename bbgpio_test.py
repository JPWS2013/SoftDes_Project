import Adafruit_BBIO.ADC as ADC
import time

ADC.setup()

"""

AIN1 -- P9_40 -- Potentiometer
AIN2 -- P9_37 -- Accelerometer (X-Direction)
AIN3 -- P9_38 -- Accelerometer (Y-Direction)
AIN0 -- P9_39 -- Accelerometer (Z-Direction)

AIN4 -- P9_33 -- Input voltage to Accelerometer

"""

while True:
	value=ADC.read("AIN1")
	voltage=value*1.8
	print "Voltage ", voltage

	res=[]
	while len(res) != 100:

		valz=ADC.read("AIN0")
		voltz=valz*1.8
		accel=(voltz-(2.5/2))/(0.174/3*2.5)

		res.append(accel)
		#print "Accel = ", accel

	aver_accel=sum(res)/len(res)
	print "Average Accel = ", aver_accel

	# time.sleep(1)
