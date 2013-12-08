"""

Module that defines the Model class that stores and manages data received by the sensors

"""

class Model(object):
    def __init__(self, view=None):
        self.view=view
        self.sensedict={}
        self.senseloc ={}

    def store_sensor(self, sensor):
        self.sensedict[sensor.senseid]={}
        self.senseloc[sensor.senseid]=(sensor.__class__.__name__, sensor.location)

    def store_data(self, datatuple):
        timestamp=datatuple[0]
        data=datatuple[1]
        sensor=datatuple[2]
        
        self.sensedict[sensor.senseid][timestamp]=data

        sensor.display(self.view)


    def print_sensors(self):
        print self.sensedict.keys()

    def print_data(self, sensor):
        print self.sensedict[sensor.senseid]

    def print_loc(self):
        print self.senseloc
        