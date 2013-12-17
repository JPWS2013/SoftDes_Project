"""

Module that defines the Model class on the beaglebone that stores and manages data received by the sensors

This module is intended to be run on a beaglebone black. It has only been tested to run on a beaglebone black

Written for Software Design, Fall 2013 by Justin Poh and Zoe Fiddler

"""

import serial

class Model(object):
    """
    This Model class provides methods for packing the data in a suitable form for transmission over the serial port of the beaglebone to a computer
    """

    def __init__(self, ser):
        self.ser=ser
        self.sensedict={}
        self.senseloc ={}

    def store_sensor(self, sensor):
        """
        Formats the necessary properties of the sensor to transmit to the model on the laptop for storage so that the model recognizes the sensor exists

        sensor: must be an instance of a Sensor object or an instance of subclass of Sensor

        This function has no return value. It only carries out the described formatting and transmitting actions
        """

        transmission='&&'+'1'+','+sensor.senseid+','+sensor.__class__.__name__+','+sensor.location+'\n'
        self.ser.write(transmission)
        self.senseloc[sensor.senseid]=(sensor.__class__.__name__, sensor.location)

    def store_data_pot(self, datatuple):
        """
        Formats potentiometer data into a standardized format that is suitable for transmitting over the serial port for the model on the laptop to read 

        datatuple: A tuple of the necessary data that needs to be stored in the model

        This function has no return value. It only carries out the described formatting and transmitting actions
        """

        timestamp=str(datatuple[0])
        data=str(datatuple[1])
        sensorid=str(datatuple[2].senseid)

        transmission='&&'+'2'+','+timestamp+','+data+','+sensorid+'\n'
        self.ser.write(transmission)

    def store_data_accel(self, datatuple):
        """
        Formats accelerometer data into a standardized format that is suitable for transmitting over the serial port for the model on the laptop to read 

        datatuple: A tuple of the necessary data that needs to be stored in the model

        This function has no return value. It only carries out the described formatting and transmitting actions
        """

        timestamp=str(datatuple[0])
        data=datatuple[1]
        sensorid=str(datatuple[2].senseid)

        data_str=str(data[0])+';'+str(data[1])+';'+str(data[2])

        transmission='&&'+'3'+','+timestamp+','+data_str+','+sensorid+'\n'
        self.ser.write(transmission)


    def store_data_halleffect(self, datatuple):
        """
        Formats hall effect sensor data into a standardized format that is suitable for transmitting over the serial port for the model on the laptop to read 

        datatuple: A tuple of the necessary data that needs to be stored in the model

        This function has no return value. It only carries out the described formatting and transmitting actions
        """

        timestamp=str(datatuple[0])
        rpm=str(datatuple[1][0])
        speed=str(datatuple[1][1])
        sensorid=str(datatuple[2].senseid)
        
        data=rpm+';'+speed

        transmission='&&'+'4'+','+timestamp+','+data+','+sensorid+'\n'
        self.ser.write(transmission)

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