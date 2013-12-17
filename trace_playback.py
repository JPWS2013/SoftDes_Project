import time 
import math
import numpy


class Trace(object):

    """
    Trace is a class that inherits from object and provides methods for simulating data from sensors. 

    For the purposes of the project for the class Software Design, Fall 2013, this module only simulates the data from a hall effect sensor

    """

    def halleffect(self):

        """
        Takes a Trace object and returns a rate of rotation in revolutions per minute

        This function is supposed to mimic the data which would be read from a hall effect sensor. For convenience, the data this function returns is revolutions per minute instead of a voltage because data processing for a hall effect sensor was not known at the time of writing.

        """

        current_time=time.time()%60                  #This current_time is used in a sine function to generate hall effect sensor data
        z=3800*(math.sin(current_time*math.pi/30))   #Assumes maximum number of revolutions per minute is 3800rpm
        return abs(z)

if __name__ == '__main__':

    trace=Trace()

    print trace.halleffect('accelerometer')