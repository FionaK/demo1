from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('login.html')
@app.route('/register')
def register():
	return render_template('register.html')
@app.route('/comments')
def comments():
        return render_template('comments.html')
			
	
	 
  
      
      

if __name__ == '__main__':
   app.run(debug = True, port=5050)
