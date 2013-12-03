import time 
import math

import numpy


class Trace(object):


    def read_data(self, sensortype):
        if sensortype.lower()=='accelerometer':
            return self.accelerometer()
        if sensortype.lower()=='potentiometer':
            return self.potentiometer()




    def accelerometer(self):
        current_time=time.time()%60
        z=math.sin(current_time*math.pi/30)
        return [0,0,z]

    def potentiometer(self):
        current_time=time.time()%30
        pos=1/current_time
        return pos
        
        


#trace=Trace()

#print trace.read_data('accelerometer')
