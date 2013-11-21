"""

Module that defines the sensor classes including sensor characteristics as instance variables

"""

import trace_playback as tp

class Sensor(object):

  def get_reading(self, playback=None):
    reading=playback.read_data(self.__class__.__name__)
    return reading

  
class Potentiometer(Sensor):
  def __init__(self, resistance, maxangle, inputconn=0, outputconn=0, currentpos=0):
    
    #self.senseid=self.query_id()

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

class Accelerometer(Sensor):

  def __init__(self, gradx=0, xmin=0, grady=0, ymin=0, gradz=0, zmin=0):
    self.gradx=gradx
    self.xmin=xmin
    self.grady=grady
    self.ymin=ymin
    self.gradz=gradz
    self.zmin=zmin

  def acceleration(self, xvolt=0, yvolt=0, zvolt=0):
    xaccel=(xvolt-self.xmin)/self.gradx
    yaccel=(yvolt-self.ymin)/self.grady
    zaccel=(zvolt-self.zmin)/self.gradz

    return (xaccel, yaccel, zaccel)



if __name__ == '__main__':
  playback=tp.Trace()

  #print type(playback)

  pot=Potentiometer(10000, 270)

  # # print pot.senseID

  accel=Accelerometer(0.3, 2.88, 0.2, 3.12, 0.1, 2.13)


  print accel.get_reading(playback)
  print pot.get_reading(playback)