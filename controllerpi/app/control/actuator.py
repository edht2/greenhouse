from app.control.relay import relay
from app.tools.log import log
import asyncio
import time

class Actuator:
	def __init__(self, relay_indexes, extension_time) -> None:
		self.extension_time = extension_time
		self.relays = relay_indexes
		# first relay in sequence is the dominant ( turn it on - the actuator will extend )
		self.state = 'RETRACTED'

       # I have a seperate fire and forget decorator for the relays allowing togglable asyncronousity
	def fire_and_forget(f):
		""" Fire and forget is just asyncronously doing two things at the same time! 
		eg. extend and actuator AND not have to wait for it to fully extend"""
		def wrapped(*args, **kwargs):
			try:
				if args[1]:
					return asyncio.get_event_loop().run_in_executor(None, f, *args, *kwargs)
				return f(args[0], args[1])
			except:
				return asyncio.get_event_loop().run_in_executor(None, f, *args, *kwargs)
		return wrapped
	
	@fire_and_forget
	def extend(self, asynchronous=True) -> None:
     
		if self.state == "EXTENDED" or self.state == "EXTENDING":
			return None

		#relay.turn_on_relay_by_index(self.relays[0])
		print("Extending actuator on relay", self.relays[0])
	
		self.state = 'EXTENDING'
  
		log('ControllerPi', None, 'controll', 'actuator', 'Extending actuator on relay', arg=self.relayIndex)
  
		time.sleep(self.extension_time)
  		# takes about 22 seconds to fully extend
    
		self.state = 'EXTENDED'
  		# show that it is extended
  
		#relay.turn_off_relay_by_index(self.relays[0])
		print("Extended actuator on relay", self.relays[0])
  
		log('ControllerPi', True, 'controll', 'actuator', 'Extended actuator on relay', arg=self.relayIndex)


	@fire_and_forget
	def retract(self, asynchronous=True) -> None:
		if self.state == "RETRACTED" or self.state == "RETRACTING":
			return None

		#relay.turn_off_relay_by_index(self.relays[0])
		print("Retracting actuator on relay", self.relays[0])
	
		self.state = 'RETRACTING'
  
		log('ControllerPi', None, 'controll', 'actuator', 'Retracting actuator on relay', arg=self.relayIndex)
  
		time.sleep(self.extension_time)
    
		self.state = 'RETRACTED'
  
		#relay.turn_off_relay_by_index(self.relays[0])
		print("Retracted actuator on relay", self.relays[0])
  
		log('ControllerPi', True, 'controll', 'actuator', 'Retracted actuator on relay', arg=self.relayIndex)
  

	def toggle(self, asynchronous=True):
		if self.state == 'EXTENDED':
			self.retract(asynchronous)
		elif self.state == 'RETRACTED':
			self.extend(asynchronous)
		elif self.state == 'EXTENDING':
			self.retract()
		else:
			self.extend()

	def stop(self) -> None:
		""" turn off everything, this will stop and movment of the actuator """
		#relay.turn_off_relay_by_index(self.relays[0])
		#relay.turn_off_relay_by_index(self.relays[1])
