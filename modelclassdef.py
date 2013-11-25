class Model(object):
	def __init__(self):
		self.sensedict={}

	def store_sensor(self, sensor):
		self.sensedict[sensor.senseid]=[]

	def store_data(self, datatuple):
		data=datatuple[0]
		sensor=datatuple[1]
		self.sensedict[sensor.senseid].append(data)

	def print_sensors(self):
		print self.sensedict.keys()

	def print_data(self, sensor):
		print self.sensedict[sensor.senseid]
		