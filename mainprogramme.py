import controllerclassdefs as controller
import modelclassdef as model
import trace_playback as tp

#TODO: Add docstring here to explain what's going on with the import line below
import textviewdef as view

playback=tp.Trace()

model=model.Model()
view=view.TextView(model)
#cluster=controller.SensorCluster()

pot=controller.Potentiometer(model, 10000, 270, 'Potentiometer 1', 'Gas Pedal', 12, 0, 0.5)
#model.store_sensor(pot)
#label=controller.SensorLabel('Potentiometer 1', 'Gas Pedal')

accel=controller.Accelerometer(model, 'Accelerometer 1', 'IMU', 0.3, 1.5, 0.3, 1.5, 0.3, 1.5)
#model.store_sensor(accel)

#print pot.label
#model.print_sensors()

data=pot.get_reading(playback)
#print data
#model.store_data(data)

data=accel.get_reading(playback)
#model.store_data(data)

data=pot.get_reading(playback)
data=accel.get_reading(playback)

# model.print_data(pot)
model.print_data(accel)

#model.print_loc()