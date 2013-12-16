"""

Module that defines the Model class that stores and manages data received by the sensors

"""

import datetime as dt
import sys

class Model(object):
    def __init__(self, view=None):
        self.view=view
        self.sensedict={}
        self.senseloc ={}
        self.lastpotreading=0

    def store_sensor(self, senseid, classname, location):
        self.sensedict[senseid]={}
        self.senseloc[senseid]=(classname, location)

    def store_data_pot(self, str_timestamp, reading_str, senseid):
        # print 'Im going to store data'
        # print "senseid = ", senseid
        # year=int(str_timestamp[:4])
        # month=int(str_timestamp[5:7])
        # day=int(str_timestamp[8:10])
        # hour=int(str_timestamp[11:13])
        # minute=int(str_timestamp[14:16])
        # second=int(str_timestamp[17:])

        data=float(reading_str)

        # timestamp=dt.datetime(year, month, day, hour, minute, second)
        # print type(timestamp)

        # print timestamp
        try:    
            self.sensedict[senseid][str_timestamp]=data

        except KeyError:
            print "Sensor does not exist. Please stop data collection on the beaglebone and run the dashboard programme first before you begin data collection again"
            sys.exit()
        # self.lastpotreading=data
        # print 'lastpotreading=', self.lastpotreading

        # print 'Ive stored the data'
        # print 'from model=', self.sensedict[senseid]

        # self.view.display_pot(senseid)

    def store_data_accel(self, str_timestamp, reading_str, senseid):
        
        data=[]

        # year=int(str_timestamp[:4])
        # month=int(str_timestamp[5:7])
        # day=int(str_timestamp[8:10])
        # hour=int(str_timestamp[11:13])
        # minute=int(str_timestamp[14:16])
        # second=int(str_timestamp[17:])

        splitdata=reading_str.split(';')

        for eachItem in splitdata:
            data.append(float(eachItem))
        
        # print data

        # timestamp=dt.datetime(year, month, day, hour, minute, second)
        # print type(timestamp)

        # print timestamp
        try:
            self.sensedict[senseid][str_timestamp]=data

        except KeyError:
            print "Sensor does not exist. Please stop data collection on the beaglebone and run the dashboard programme first before you begin data collection again"
            sys.exit()
        # print "i stored data!"
        # self.view.display_accel(senseid)
    def store_data_halleffect(self, str_timestamp, reading_str, senseid):
        
        data=[]

        # year=int(str_timestamp[:4])
        # month=int(str_timestamp[5:7])
        # day=int(str_timestamp[8:10])
        # hour=int(str_timestamp[11:13])
        # minute=int(str_timestamp[14:16])
        # second=int(str_timestamp[17:])

        splitdata=reading_str.split(';')

        for eachItem in splitdata:
            data.append(float(eachItem))
        
        # print data

        # timestamp=dt.datetime(year, month, day, hour, minute, second)
        # print type(timestamp)

        # print timestamp
        try:
            self.sensedict[senseid][str_timestamp]=data

        except KeyError:
            print "Sensor does not exist. Please stop data collection on the beaglebone and run the dashboard programme first before you begin data collection again"
            sys.exit()
        # print "I stored halleffect data!"

        # print data
        
        # self.view.display_accel(senseid)
    def print_sensors(self):
        print self.sensedict.keys()

    def print_data(self, sensor):
        print self.sensedict[sensor.senseid]

    def print_loc(self):
        print self.senseloc
        