from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, static_folder='static', template_folder='templates')

# LOGIN PAGE
@app.route('/')
@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username == "admin" and password == "1234":
            return "Login Successful"
        else:
            return "Invalid Username or Password"

    return render_template('login.html')


# SIGNUP PAGE
@app.route('/signup', methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        return "User Registered Successfully"

    return render_template('signup.html')


# FORGOT PASSWORD PAGE
@app.route('/forgot', methods=['GET','POST'])
def forgot():
    if request.method == 'POST':
        email = request.form['email']
        return "Password reset link sent"

    return render_template('forgot.html')

<<<<<<< HEAD
if __name__ == "__main__":
    app.run(debug=True)
=======

if __name__ == '__main__':
    app.run(debug=True)
>>>>>>> e40cf701d97f6a0fc4e3ab9652545b5c685e16b6
