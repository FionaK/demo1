#!/usr/bin/python

class Signin(object):
	def __init__(self):
		self.details={}
		self.posts=[]
		self.authenticate={}
	def register(self):
		firstname=input('Enter your firstname')
		lastname=input('Enter your lastname')
		username=input('Enter your username')
		password=input('Enter your password')
		confirmpwd=input('Enter your password again')
		email=input('Enter your email')
		if password == confirmpwd:
			self.details.update({username:[firstname,lastname,password,email]})
			print ('Resgistration successful for', username)
		else:
			print ('Passwords don\'t match, try again')
	def login(self):
		username=input('Enter your username')
		password=input('Enter your password')
		if username in self.details:
			if password==self.details[username][2]:
				print ('ACCESS GRANTED')
				self.authenticate.update({username:password})
			else:
				print('INVALID USERNAME or PASSWORD')
		else:
			print ("Please register first")
	def comments(self):
		if input('Enter your username') in self.authenticate:
			comments=input('Post your comments here')
			self.posts.append(comments)
			print ("Updated comments: ", self.posts)
		else:
			print ('Can\'t post a comment, log in first')                               
                        
                
                             
       




			
  			
