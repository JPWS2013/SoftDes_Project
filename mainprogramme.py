"""

This is the main module that should be run on the beaglebone. It initializes and stores all the sensors that are connected before proceeding to fetch data from each one on a continuous basis

This module is intended to be run on a beaglebone black. It has only been tested to run on a beaglebone black

Written for Software Design, Fall 2013 by Justin Poh and Zoe Fiddler

"""

import controllerclassdefs as controller
import bb_modeldef as model
import bb_datamethods as data
import trace_playback as tp
import Adafruit_BBIO.ADC as ADC
import Adafruit_BBIO.UART as UART
import serial
import time

"""

AIN1 -- P9_40 -- Potentiometer
AIN2 -- P9_37 -- Accelerometer (X-Direction)
AIN3 -- P9_38 -- Accelerometer (Y-Direction)
AIN0 -- P9_39 -- Accelerometer (Z-Direction)

AIN4 -- P9_33 -- Potentiometer 2

"""

UART.setup("UART1")
ADC.setup()
 
ser = serial.Serial(port = "/dev/ttyGS0", baudrate=9600)
ser.close()
ser.open()

datasource=data.Trace()
trace=tp.Trace()
model=model.Model(ser)

pot=controller.Potentiometer('AIN1', model, 10000, 270, 'Potentiometer 1', 'Gas Pedal', 1.25, 0)

pot2=controller.Potentiometer('AIN4', model, 10000, 270, 'Potentiometer 2', 'Brake Pedal', 1.25, 0)

accel_sense=0.174/3*2.5
earthaccel_volt=2.5/2
accel=controller.Accelerometer("AIN2", "AIN3", "AIN0", model, 'Accelerometer 1', 'IMU', accel_sense, earthaccel_volt , accel_sense, earthaccel_volt, accel_sense, earthaccel_volt)

tach=controller.HallEffectSensor(model, 'Engine Tachometer', 'Engine Output Shaft')

while True:
	pot.get_reading(datasource)

	time.sleep(0.02)

	tach.get_reading(trace)

	time.sleep(0.02)

	pot2.get_reading(datasource)

	time.sleep(0.02)

	accel.get_reading(datasource)

	time.sleep(0.02)