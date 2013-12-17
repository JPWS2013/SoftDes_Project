"""

Module that defines the sensor classes including sensor characteristics as instance variables

This module is intended to be run on a beaglebone black. It has only been tested to run on a beaglebone black

Written for Software Design, Fall 2013 by Justin Poh and Zoe Fiddler

"""

import trace_playback as tp
import bb_datamethods as data
import datetime as dt
import time
import math

class Sensor(object):

  """
  Sensor is a class that inherits from object and is used to subclass different sensors that will be read by the beaglebone.

  Sensor also provides methods that are necessary for all types of sensors.

  """

  def query_id(self, model):

    """
    Queries the model for a unique sensor ID 

    self: must be a Sensor object or a subclass of Sensor
    model: must be an instance of Model as defined in the module bb_modeldef.py

    Returns a string that is the unique sensor ID for the sensor
    """

    idnum=str(len(model.senseloc.keys()))
    
    return self.__class__.__name__ + idnum

 
class Potentiometer(Sensor):
  """
  This class is a subclass of Sensor that mimics a real-world potentiometer by allowing a user to store properties of the potentiometer as attributes.

  The class also provides methods for fetching data from the actual sensor, processing the reading and displaying it.
  """

  def __init__(self, pinstring, model, resistance, maxangle, label, location, inputconn=0, outputconn=0):
    
    self.model=model
    self.pin=pinstring

    self.senseid=self.query_id(model)

    self.label=label
    self.location=location

    self.resistance=resistance
    self.maxangle=maxangle

    self.pin1=inputconn
    self.pin3=outputconn

    model.store_sensor(self)

  def get_reading(self, datasource):
    """
    Fetches and processes a reading from the actual potentiometer and sends it to the model for storage

    datasource: must be a Trace object

    This function has no return value. It simply fetches and processes data and sends them to the model for storage
    """

    reading=datasource.potentiometer(self.pin)
    timestamp=dt.datetime.today()

    processed_reading=self.data_process(reading)
    datapacket=(timestamp, processed_reading, self)

    self.model.store_data_pot(datapacket)

  def data_process(self, reading):
    """
    Processes the potentiometer reading to convert voltage into a ratio to indicate how much the potentiometer has been turned

    reading: Must be a float or integer number

    Returns the ratio that describes how much the potentiometer has been turned
    """

    ratio=(reading-self.pin3)/(self.pin1-self.pin3)

    self.curentpos=ratio

    return ratio

  def print_id(self):
    """
    Function that prints the unique senseid for the potentiometer. This function has no return value. 
    """
    print self.senseid


class Accelerometer(Sensor):

  """
  This class is a subclass of Sensor that mimics a real-world accelerometer by allowing a user to store properties of the accelerometer as attributes.

  The class also provides methods for fetching data from the actual sensor, processing the reading and displaying it.
  """

  def __init__(self, pinx, piny, pinz, model, label, location, sensx=0, xearth=0, sensy=0, yearth=0, sensz=0, zearth=0):
    self.model=model

    self.pinx=pinx
    self.piny=piny
    self.pinz=pinz
    
    self.senseid=self.query_id(model)

    self.label=label
    self.location=location

    self.sensx=sensx
    self.xearth=xearth
    self.sensy=sensy
    self.yearth=yearth
    self.sensz=sensz
    self.zearth=zearth

    model.store_sensor(self)

  def get_reading(self, datasource=None):
    """
    Fetches and processes a reading from the actual accelerometer and sends it to the model for storage

    datasource: must be a Trace object

    This function has no return value. It simply fetches and processes data and sends them to the model for storage
    """

    reading=datasource.accelerometer(self.pinx, self.piny, self.pinz)
    timestamp=dt.datetime.today()

    processed_reading=self.data_process(reading)
    
    datapacket=(timestamp, processed_reading, self)

    self.model.store_data_accel(datapacket)
  
  def data_process(self, reading):
    """
    Processes the accelerometer reading to convert voltage into a measure of acceleration in g

    reading: Must be a list of float or integer numbers

    Returns a list of the x, y and z direction accelerations in that order
    """
    xvolt=reading[0]
    yvolt=reading[1]
    zvolt=reading[2]

    xaccel=(xvolt-self.xearth)/self.sensx
    yaccel=(yvolt-self.yearth)/self.sensy
    zaccel=(zvolt-self.zearth)/self.sensz

    return [xaccel, yaccel, zaccel]

  def display(self, view):

    view.display_accel(self)

class HallEffectSensor(Sensor):
  def __init__(self, model, label, location):
    self.model=model    
    self.senseid=self.query_id(model)
    self.label=label
    self.location=location

    model.store_sensor(self)

  def get_reading(self, datasource=None):
    """
    Fetches and processes a reading from the actual Hall Effect Sensor and sends it to the model for storage

    datasource: must be a Trace object

    This function has no return value. It simply fetches and processes data and sends them to the model for storage. Note that it has been implemented using a trace playback sending fake data because the hall effect sensor has not been implemented at the time of writing. Thus, fake data is used to take the place of the sensor.
    """

    timestamp=dt.datetime.today()

    processed_reading=datasource.halleffect()

    speedcalc=processed_reading/(0.8*11)*(2*math.pi*0.000142)*60

    datapacket=(timestamp, [processed_reading, speedcalc], self)
    self.model.store_data_halleffect(datapacket)

if __name__ == '__main__':
  data=tp.Trace()

  #print type(data)

  # pot=Potentiometer(10000, 270)

  # # print pot.senseID

  # accel=Accelerometer(0.3, 2.88, 0.2, 3.12, 0.1, 2.13)
  tach=HallEffectSensor('model', 'Engine Tachometer', 'Engine Output Shaft')

  print tach.get_reading(data)

  # print accel.get_reading(data)
  # print pot.get_reading(data)