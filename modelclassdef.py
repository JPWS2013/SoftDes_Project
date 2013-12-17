"""

Module that defines the Model class that stores and manages data received by the sensors

This module is intended to be run on a linux PC

Written for Software Design, Fall 2013 by Justin Poh and Zoe Fiddler

"""

import datetime as dt
import sys

class Model(object):

    """
    This class defines methods for storing the data received from the serial port from the beaglebone
    """
    def __init__(self, view=None):
        self.view=view
        self.sensedict={}
        self.senseloc ={}
        self.lastpotreading=0

    def store_sensor(self, senseid, classname, location):
        """
        Stores the sensor in the Model

        senseid: string of the unique ID number of the sensor
        classname: string of the class of sensor object (type of sensor)
        location: string of the location of the sensor on the car

        This function has no return value
        """
        self.sensedict[senseid]={}
        self.senseloc[senseid]=(classname, location)

    def store_data_pot(self, str_timestamp, reading_str, senseid):
        """
        Converts the potentiometer data received into a suitable format and stores it in the Model

        str_timestap: string of the datetime object that represents when the data was fetched
        reading_str: string version of the processed potentiometer data
        senseid: string version of the unique ID number of the sensor

        This function has no return value
        """

        data=float(reading_str)

        try:    
            self.sensedict[senseid][str_timestamp]=data

        except KeyError:
            print "Sensor does not exist. Please stop data collection on the beaglebone and run the dashboard programme first before you begin data collection again"
            sys.exit()

    def store_data_accel(self, str_timestamp, reading_str, senseid):
        
        """
        Converts the accelerometer data received into a suitable format and stores it in the Model

        str_timestap: string of the datetime object that represents when the data was fetched
        reading_str: string version of the processed accelerometer data
        senseid: string version of the unique ID number of the sensor

        This function has no return value
        """

        data=[]

        splitdata=reading_str.split(';')

        for eachItem in splitdata:
            data.append(float(eachItem))
        
        try:
            self.sensedict[senseid][str_timestamp]=data

        except KeyError:
            print "Sensor does not exist. Please stop data collection on the beaglebone and run the dashboard programme first before you begin data collection again"
            sys.exit()

    def store_data_halleffect(self, str_timestamp, reading_str, senseid):
        """
        Converts the potentiometer data received into a suitable format and stores it in the Model

        str_timestap: string of the datetime object that represents when the data was fetched
        reading_str: string version of the processed accelerometer data
        senseid: string version of the unique ID number of the sensor

        This function has no return value
        """
        data=[]

        splitdata=reading_str.split(';')

        for eachItem in splitdata:
            data.append(float(eachItem))
        
        try:
            self.sensedict[senseid][str_timestamp]=data

        except KeyError:
            print "Sensor does not exist. Please stop data collection on the beaglebone and run the dashboard programme first before you begin data collection again"
            sys.exit()

    def print_sensors(self):
        """
        Prints all the sensors stored in the model. This function has no return value. It only prints a list of all the sensors stored in the model.
        """
        print self.sensedict.keys()

    def print_data(self, sensor):
        """
        Prints all the data stored in the model for the particular sensor. This function has no return value. It only prints the data
        """
        print self.sensedict[sensor.senseid]

    def print_loc(self):
        """
        Prints the dictionary of all sensors and their locations. This function has no return value. It only prints the dictionary.
        """
        print self.senseloc