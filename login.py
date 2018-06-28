#!/usr/bin/python
 class Signin(object):
	def __init__(self):
		self.details={}
	def register(self):
		firstname=input('Enter your firstname')
		lastname=input('Enter your lastname')
		username=input('Enter your username')
		password=input('Enter your password')
		email=input('Enter your email')
		self.details.update({username:password})
		print ('Resgistration successful')
	def login(self):
		username=input('Enter your username')
		password=input('Enter your password')
		if username in self.details:
			if password==self.details[username]:
				print ('ACCESS GRANTED')
			else:
				print('INVALID DETAILS')
		else:
			print ("Please register first")
  			
