"""

Module that defines the Model class that stores and manages data received by the sensors

"""
import Adafruit_BBIO.ADC as ADC


class Trace(object):
    
    def potentiometer(self):

        for i in range(5):

            value=ADC.read("AIN1")
            voltage=value*1.8
            # print "voltage = ", voltage

        return voltage

    def accelerometer(self):
        readingx=ADC.read("AIN2")
        readingy=ADC.read("AIN3")
        readingz=ADC.read("AIN0")

        readingx=readingx*1.8
        readingy=readingy*1.8
        readingz=readingz*1.8
        reading=[readingx, readingy, readingz]

        return reading