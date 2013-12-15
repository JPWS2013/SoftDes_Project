"""

Module that defines the Model class that stores and manages data received by the sensors

"""

import serial

class Model(object):
    def __init__(self, ser, view=None):
        self.view=view
        self.ser=ser
        self.sensedict={}
        self.senseloc ={}

    def store_sensor(self, sensor):

        transmission='&&'+'1'+','+sensor.senseid+','+sensor.__class__.__name__+','+sensor.location+'\n'
        self.ser.write(transmission)
        # self.sensedict[sensor.senseid]={}
        # self.senseloc[sensor.senseid]=(sensor.__class__.__name__, sensor.location)

    def store_data_pot(self, datatuple):
        timestamp=str(datatuple[0])[:-7]
        data=str(datatuple[1])
        sensorid=str(datatuple[2].senseid)

        transmission='&&'+'2'+','+timestamp+','+data+','+sensorid+'\n'
        # print transmission
        self.ser.write(transmission)

    def store_data_accel(self, datatuple):
        timestamp=str(datatuple[0])[:-7]
        data=datatuple[1]
        sensorid=str(datatuple[2].senseid)

        data_str=str(data[0])+';'+str(data[1])+';'+str(data[2])

        transmission='&&'+'3'+','+timestamp+','+data_str+','+sensorid+'\n'
        # print transmission
        self.ser.write(transmission)

    def print_sensors(self):
        print self.sensedict.keys()

    def print_data(self, sensor):
        print self.sensedict[sensor.senseid]

    def print_loc(self):
        print self.senseloc
        