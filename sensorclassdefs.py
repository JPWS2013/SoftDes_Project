"""

Module that defines the sensor classes including sensor characteristics as instance variables

"""

class Sensor(object):
  def __init__(self, rawdata):
  
    self.rawdata = rawdata
  

class Potentiometer(Sensor):
  def __init__(self, resistance, maxangle, inputconn=0, outputconn=0):
    self.resistance=resistance
    self.maxangle=maxangle
    self.resdens=resistance/maxangle
    self.pin1=inputconn
    self.pin3=outputconn
    
  def volt_div(self, sweeppos):
    ratio=sweeppos/maxangle
    uppervoltdrop=ratio*(self.pin1-self.pin3)
    return (self.pin1-uppervoltagedrop)
