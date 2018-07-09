from flask import *
import datetime
from functools import wraps
import jwt
import pymysql
from models import connection, cur

app=Flask(__name__)



app.config['SECRET_KEY']='fifi'

connection = pymysql.connect(
			host='localhost',
			user='root',
			password='',
			db='details',

	)



@app.route('/', methods= ['POST','GET'])
def test():
	return jsonify({'message': 'welcome!'})

@app.route('/register', methods=['GET','POST'])
def register():
	firstname=request.get_json()['firstname']
	lastname=request.get_json()['lastname']
	username=request.get_json()['username']
	password=request.get_json()['password']
	email=request.get_json()['email']
	#timestamp= datetime.today().strftime('%Y%m%d%H%s')
	
	try:
		with connection.cursor() as cusor:
			sql = "INSERT INTO `user` (`firstname`, `lastname`, `username`, `password`, `email`) VALUES (%s, %s, %s, %s, %s)"
			try:
				cusor.execute(sql, (firstname, lastname, username, password, email))
			except:
				return jsonify({'message': 'Registration faied. Try again'})

		connection.commit()
				
	finally:
		connection.close()
		return jsonify({'message':'successful registration'})


def token_required(k):
	@wraps(k)
	def decorated(*args, **kwargs):
		token = request.args.get('token')
		if not token:
			return jsonify({'message' : 'Token is missing'})
		try:
			data = jwt.decode(token, app.config['SECRET_KEY'])
		except:
			return jsonify({'message' : 'Token is invalid'})
		return k(*args, **kwargs)

	return decorated


@app.route('/login', methods= ['GET', 'POST'])
def login():
	username=request.get_json()['username']
	password=request.get_json()['password']
	auth= request.authorization

	cur.execute("SELECT COUNT(1) FROM user WHERE username = %s;", username)
	if cur.fetchone()[0]:
		cur.execute("SELECT password FROM user WHERE username = %s;", username)
		for row in cur.fetchall():
			if password == row[0]:
				token= jwt.encode ({'user':auth.username, 'exp':datetime.datetime.utcnow + datetime.timedelta(minutes=15)}, app.config['SECRET_KEY'])
				return jsonify({"message": "Login successful", 'access-token' : token.decode('UTF-8')})
			else:
				return jsonify({'message': "invalid password or username"})
	else:
		return jsonify({'message' : 'Invalid password or username'})
	cur.close()				

@app.route('/comments', methods=['GET', 'POST'])
@token_required
def comments():
	comment=request.get_json()["comment"]
	username=request.get_json()["username"]
	try:
		with connection.cursor() as cusor:
			sql = "INSERT INTO `comments` (`username`, `comment`) VALUES (%s, %s)"
			try:
				cusor.execute(sql, (username, comment))
			except:
				return jsonify({'message': 'Unable to comment. Try again'})
		connection.commit()			
	finally:
		connection.close()
		return jsonify({'message':'successfully commented'})

	
@app.route('/display_comments', methods=['GET'])
@token_required
def display_comments():
	cur.execute("SELECT * FROM comments")
	rows=cur.fetchall()
	return jsonify(rows)
	
		
@app.route('/delete_comment/<int:commentid>', methods=['DELETE', 'POST'])
@token_required	
def delete_comment(commentid):
	username=request.get_json()["username"]
	try:
		with connection.cursor() as cursor:
			sql="DELETE FROM `comments` WHERE `comments`.`commentID`="+str(commentID)+" and `comments`.`username`= '"+username+"'"
			try:
				cursor.execute(sql)
			except:
				return jsonify({'message' : 'please register first'})
		connection.commit()
	except:
			connection.close()		
	return jsonify ({"message": "your comment has been deleted"})

@app.route('/get_info', methods=['GET'])
@token_required
def get_info():
	cur.execute("SELECT * FROM users")
	rows=cur.fetchall()
	return jsonify (rows)
	


if __name__ == '__main__':
	app.run( debug=True)
