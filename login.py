#!/usr/bin/python
class Signin(object):
	def __init__(self, details):
  		self.details={}
  	def register(self):
  		firstname=raw_input('Enter your firstname')
  		lastname=raw_input('Enter your lastname')
  		username=raw_input('Enter your username')
  		password=raw_input('Enter your password')
  		email=raw_input('Enter your email')
  		self.details.update({username:password})
  		def login(self):
  			username=raw_input('Enter your username')
  			password=raw_input('Enter your password')
  			if password==self.details[username]:
  				print ('ACCESS GRANTED')
  			else:					
  				print('INVALID DETAILS')
  			