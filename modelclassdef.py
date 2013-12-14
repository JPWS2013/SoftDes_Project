"""

Module that defines the Model class that stores and manages data received by the sensors

"""

import datetime as dt

class Model(object):
    def __init__(self, view=None):
        self.view=view
        self.sensedict={}
        self.senseloc ={}

    def store_sensor(self, senseid, classname, location):
        self.sensedict[senseid]={}
        self.senseloc[senseid]=(classname, location)

    def store_data_pot(self, str_timestamp, reading_str, senseid):
        year=int(str_timestamp[:4])
        month=int(str_timestamp[5:7])
        day=int(str_timestamp[8:10])
        hour=int(str_timestamp[11:13])
        minute=int(str_timestamp[14:16])
        second=int(str_timestamp[17:])

        data=float(reading_str)

        timestamp=dt.datetime(year, month, day, hour, minute, second)
        # print type(timestamp)

        # print timestamp
        
        self.sensedict[senseid][timestamp]=data

        self.view.display_pot(senseid)

    # def store_data_accel(self, str_timestamp, reading_str, senseid):
    #     year=int(str_timestamp[:4])
    #     month=int(str_timestamp[5:7])
    #     day=int(str_timestamp[8:10])
    #     hour=int(str_timestamp[11:13])
    #     minute=int(str_timestamp[14:16])
    #     second=int(str_timestamp[17:])

    #     data=float(reading_str)

    #     timestamp=dt.datetime(year, month, day, hour, minute, second)
    #     # print type(timestamp)

    #     # print timestamp
        
    #     self.sensedict[senseid][timestamp]=data

    #     self.view.display_pot(senseid)

    def print_sensors(self):
        print self.sensedict.keys()

    def print_data(self, sensor):
        print self.sensedict[sensor.senseid]

    def print_loc(self):
        print self.senseloc
        