"""

Module that defines the sensor classes including sensor characteristics as instance variables

"""

import trace_playback as tp
import datetime as dt

class Sensor(object):

  def get_reading(self, playback=None):
    reading=playback.read_data(self.__class__.__name__)
    timestamp=dt.datetime.today()

    processed_reading=self.data_process(reading)

    datapacket=(timestamp, processed_reading, self)
    self.model.store_data(datapacket)

    # return (reading,self)

  def query_id(self, model):

    idnum=str(len(model.sensedict.keys()))
    return self.__class__.__name__ + idnum

 
class Potentiometer(Sensor):
  def __init__(self, model, resistance, maxangle, label, location, inputconn=0, outputconn=0, currentpos=0):
    
    #self.senseid=self.query_id()
    self.model=model

    
    self.senseid=self.query_id(model)

    self.label=label
    self.location=location
    #self.label=SensorLabel(label, location)

    self.resistance=resistance
    self.maxangle=maxangle
    #self.resdens=resistance/maxangle
    self.pin1=inputconn
    self.pin3=outputconn
    
    self.currentpos=currentpos

    model.store_sensor(self)


  def data_process(self, reading):
    ratio=(reading-self.pin3)/(self.pin1-self.pin3)

    self.curentpos=ratio

    return ratio

  def display(self, view):

    view.display_pot(self)

  def print_id(self):
    print self.senseid

class Accelerometer(Sensor):

  def __init__(self, model, label, location, sensx=0, xearth=0, sensy=0, yearth=0, sensz=0, zearth=0):
    self.model=model

    
    self.senseid=self.query_id(model)


    # self.label=SensorLabel(label, location)
    self.label=label
    self.location=location

    self.sensx=sensx
    self.xearth=xearth
    self.sensy=sensy
    self.yearth=yearth
    self.sensz=sensz
    self.zearth=zearth

    model.store_sensor(self)

  def data_process(self, reading):
    xvolt=reading[0]
    yvolt=reading[1]
    zvolt=reading[2]

    xaccel=(xvolt-self.xearth)/self.sensx
    yaccel=(yvolt-self.yearth)/self.sensy
    zaccel=(zvolt-self.zearth)/self.sensz

    return [xaccel, yaccel, zaccel]

  def display(self, view):

    view.display_accel(self)


if __name__ == '__main__':
  playback=tp.Trace()

  #print type(playback)

  pot=Potentiometer(10000, 270)

  # # print pot.senseID

  accel=Accelerometer(0.3, 2.88, 0.2, 3.12, 0.1, 2.13)


  print accel.get_reading(playback)
  print pot.get_reading(playback)