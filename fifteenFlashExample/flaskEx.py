from flask import Flask, redirect,url_for,flash,render_template,request

app = Flask(__name__)
app.secret_key='rtqwgfsywer3245125dfasda#@$1efasd'

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/login',methods=['GET','POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username']!= 'admin' or request.form['password'] != 'admin':
            error = 'Invalid username or password. Please try again!'
        else:
            flash('You were successfully logged in')
            flash('log out before login again')
            return redirect(url_for('index'))
    return render_template('log_in.html',error=error)

if __name__=='__main__':
    app.run(debug=True)
