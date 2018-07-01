from flask import Flask, redirect, url_for, request, render_template, session, flash
app = Flask(__name__)

posts=[]
post_info ={}

@app.route('/')
def index():
        return "<h1> <a href = '/login'> Already signed up? Click here to log in</a> <br/> <br/></h1> <h2><a href = '/register'> Click here to signup</a> <br/> <br/></h2>"
@app.route('/login', methods =['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
    	return render_template('login.html')
        if request.form['username'] != 'fifi' or request.form['password'] != '123':
            return 'Invalid username or password'
        else:
        	session ['log_in'] = True
        	flash("You are logged in")
        	return render_template('comments,html')

@app.route('/register')
def register():
	return render_template('register.html')

@app.route('/comments', methods=['GET', 'POST'])
def comments():
    if request.method == 'POST':
        post_info['title'] = request.form.get('title')
        post_info['content'] = request.form.get('content')
        posts.append(post_info)
	return render_template('comments.html')

   
@app.route('/logout')

def logout():
   
   session.pop('login', None)
   flash('You are logged out')
   return redirect(url_for('/'))
                
                      

if __name__ == '__main__':
   app.run(debug = True, port=5050)
