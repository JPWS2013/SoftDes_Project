"""

Module that defines the sensor classes including sensor characteristics as instance variables

"""

import trace_playback as tp

class SensorLabel(object):
  def __init__(self, label=None, location=None):
    self.label=label
    self.location=location

  def __str__(self):
    return 'Sensor Label: %s, Sensor Location: %s' % (self.label, self.location)

class Sensor(object):

  #def __init__(self):
    

  def get_reading(self, playback=None):
    reading=playback.read_data(self.__class__.__name__)
    return (reading,self)

  def query_id(self, model):

    idnum=str(len(model.sensedict.keys()))
    return self.__class__.__name__ + idnum


  
class Potentiometer(Sensor):
  def __init__(self, model, resistance, maxangle, label, location, inputconn=0, outputconn=0, currentpos=0):
    
    #self.senseid=self.query_id()
    self.model=model

    
    self.senseid=self.query_id(model)


    self.label=SensorLabel(label, location)

    self.resistance=resistance
    self.maxangle=maxangle
    #self.resdens=resistance/maxangle
    self.pin1=inputconn
    self.pin3=outputconn
    
    self.currentpos=currentpos
    
  #def 

  def pot_position(self, reading):
    ratio=reading/(self.pin1-self.pin3)

    self.curentpos=ratio

    return ratio

  def print_id(self):
    print self.senseid

class Accelerometer(Sensor):

  def __init__(self, model, label, location, sensx=0, xearth=0, sensy=0, yearth=0, sensz=0, zearth=0):
    self.model=model

    
    self.senseid=self.query_id(model)


    self.label=SensorLabel(label, location)

    self.sensx=sensx
    self.xearth=xearth
    self.sensy=sensy
    self.yearth=yearth
    self.sensz=sensz
    self.zearth=zearth

  def acceleration(self, xvolt=0, yvolt=0, zvolt=0):
    xaccel=(xvolt-self.xmin)/self.gradx
    yaccel=(yvolt-self.ymin)/self.grady
    zaccel=(zvolt-self.zmin)/self.gradz

    return [xaccel, yaccel, zaccel]

# class SensorCluster(Object):
#   def __init__(self, sensor_dict):

#     self.clustser=


if __name__ == '__main__':
  playback=tp.Trace()

  #print type(playback)

  pot=Potentiometer(10000, 270)

  # # print pot.senseID

  accel=Accelerometer(0.3, 2.88, 0.2, 3.12, 0.1, 2.13)


  print accel.get_reading(playback)
  print pot.get_reading(playback)