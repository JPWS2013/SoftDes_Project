import controllerclassdefs as controller
import modelclassdef as model
import trace_playback as tp

playback=tp.Trace()
model=model.Model()

#cluster=controller.SensorCluster()

pot=controller.Potentiometer(model, 10000, 270, 'Potentiometer 1', 'Gas Pedal', 12, 0, 0.5)
model.store_sensor(pot)
#label=controller.SensorLabel('Potentiometer 1', 'Gas Pedal')

accel=controller.Accelerometer(model, 'Accelerometer 1', 'IMU', 0.3, 2.88, 0.2, 3.12, 0.1, 2.13)
model.store_sensor(accel)

print pot.label
model.print_sensors()

data=pot.get_reading(playback)
#print data
model.store_data(data)

data=accel.get_reading(playback)
model.store_data(data)

model.print_data(pot)
model.print_data(accel)