from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__, static_folder='static', template_folder='templates')
def init_db():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT
    )
    """)

    conn.commit()
    conn.close()

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
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()

        try:
            cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
            conn.commit()
            conn.close()
            return "User Registered Successfully! Now go to Login."
        except:
            conn.close()
            return "Username already exists!"

    return render_template('signup.html')
# FORGOT PASSWORD PAGE
@app.route('/forgot', methods=['GET','POST'])
def forgot():
    if request.method == 'POST':
        email = request.form['email']
        return "Password reset link sent"

    return render_template('forgot.html')

import os

if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5000)