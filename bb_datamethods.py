"""

Module that defines the Model class that stores and manages data received by the sensors

This module is intended to be run on a beaglebone black. It has only been tested to run on a beaglebone black

Written for Software Design, Fall 2013 by Justin Poh and Zoe Fiddler

"""
import Adafruit_BBIO.ADC as ADC    #Adafruit_BBIO is a python library written by adafruit to access beaglebone GPIO pins using python

"""

AIN1 -- P9_40 -- Potentiometer
AIN2 -- P9_37 -- Accelerometer (X-Direction)
AIN3 -- P9_38 -- Accelerometer (Y-Direction)
AIN0 -- P9_39 -- Accelerometer (Z-Direction)

AIN4 -- P9_33 -- Potentiometer 2

"""

class Trace(object):

    """
    The trace class provides methods for reading different types of sensor data using the beaglebone
    """
    
    def potentiometer(self, pinstring):
        """
        Reads the voltage reading of a potentiometer connected to the beaglebone GPIO pins

        pinstring: a string that indicates which pin on the beaglebone the potentiometer is connected to

        Returns the voltage output of the potentiometer
        """

        for i in range(5):

            value=ADC.read(pinstring)
            voltage=value*1.8

        return voltage

    def accelerometer(self, pinstringx, pinstringy, pinstringz):
        """
        Reads the voltage reading of the three directions of accelereration from an accelerometer connected to the beaglebone GPIO pins

        pinstring: a string that indicates which pin on the beaglebone the potentiometer is connected to

        Returns the voltage output of the potentiometer
        """
        readingx=ADC.read(pinstringx)
        readingy=ADC.read(pinstringy)
        readingz=ADC.read(pinstringz)

        readingx=readingx*1.8
        readingy=readingy*1.8
        readingz=readingz*1.8

        return [readingx, readingy, readingz]