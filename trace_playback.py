import time 
import math

import numpy


class Trace(object):


	def read_data(self, sensortype):
		current_time=time.time()
		self.update(current_time)
		if sensortype.lower()=='accelerometer':
			return 'i see your accelerometer'
		if sensortype.lower()=='potentiometer':
			return 'i see your potentiometer'




	def accelerometer():
	"""creates a dictionary with times as keys
 	and [a_x,a_y,a_z] as values"""
 		res=dict()
 		for i in numpy.range(0,59):
 		res[i]=math.sin(i*math.pi/30)

 		return res


