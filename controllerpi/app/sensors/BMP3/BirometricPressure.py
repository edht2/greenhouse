# -*- coding: utf-8 -*-
from DFRobot_BMP3XX import *

class BirometricPressure:
	def __init__(self):
		self.sensor = DFRobot_BMP3XX_I2C(i2c_addr = 0x77,bus = 1)
		self.sensor.begin()
		self.sensor.set_common_sampling_mode(ULTRA_PRECISION)
		self.sensor.calibrated_absolute_difference(50.0)

	def read(self):
		return self.sensor.get_temperature, self.sensor.get_pressure, self.sensor.get_altitude
