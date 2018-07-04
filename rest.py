from flask import Flask, jsonify, request
app=Flask(__name__)
details = {}
posts=[]
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
	details.update({username:{"first_name":firstname,"last_name":lastname,"email":email,"pass_wd":password}})
	return jsonify({'message':'successful registration'})

@app.route('/login', methods= ['GET', 'POST'])
def login():
	username=request.get_json()['username']
	password=request.get_json()['password']
	if username in details:
		if password==details[username]["password"]:
			return jsonify({"message": "Login successful"})
		else:
			return jsonify({'message': "invalid password or username"})

@app.route('/comments', methods=['GET', 'POST'])
def comments():
	comment=request.get_json()["comment"]
	posts.append(comment)
	return jsonify({"message": "comment uploaded"})

	
@app.route('/display', methods=['GET'])
def display_comments():
	output={}
	for each in posts:
		output.update({posts.index(each):each})
		return jsonify(output)

@app.route('/delete_comment/<int:commentid>', methods=['DELETE'])	
def delete_comment(commentid):
	del posts[commentid]
	return jsonify ({"message": "your comment has been deleted"})


if __name__ == '__main__':
	app.run(debug=True, port=5080)