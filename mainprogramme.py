import controllerclassdefs as controller
import bb_modeldef as model
import bb_datamethods as data
import Adafruit_BBIO.ADC as ADC
import Adafruit_BBIO.UART as UART
import serial

#TODO: Add docstring here to explain what's going on with the import line below
# import textviewdef as view

UART.setup("UART1")
ADC.setup()
 
ser = serial.Serial(port = "/dev/ttyGS0", baudrate=9600)
ser.close()
ser.open()

datasource=data.Trace()

model=model.Model(ser)
# view=view.TextView(model)
#cluster=controller.SensorCluster()

pot=controller.Potentiometer(model, 10000, 270, 'Potentiometer 1', 'Gas Pedal', 1.25, 0)
#model.store_sensor(pot)
#label=controller.SensorLabel('Potentiometer 1', 'Gas Pedal

accel_sense=0.174/3*2.5
earthaccel_volt=2.5/2
accel=controller.Accelerometer(model, 'Accelerometer 1', 'IMU', accel_sense, earthaccel_volt , accel_sense, earthaccel_volt, accel_sense, earthaccel_volt)
#model.store_sensor(accel)

#print pot.label
#model.print_sensors()

data=pot.get_reading(datasource)
#print data
# model.store_data(data)

# data=accel.get_reading(datasource)
#model.store_data(data)

# data=pot.get_reading(datasource)
# data=accel.get_reading(datasource)

# model.print_data(pot)
# model.print_data(accel)

#model.print_loc()