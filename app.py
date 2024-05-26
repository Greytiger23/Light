#!/usr/bin/python3


from flask import Flask, render_template, request, redirect, url_for
from werkzeug.security import generate_password_hash

app = Flask(__name__)

# Simple in-memory user database
users = {}

@app.route('/')
def index():
        return redirect(url_for('signup'))

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
# You can add more complex validation here if needed
    if username and email and password:
        hashed_password = generate_password_hash(password)
        users[username] = {'email': email, 'password': hashed_password}
        return redirect(url_for('login'))
    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
    if username in users and users[username]['password'] == generate_password_hash(password):
        return redirect(url_for('success'))
    return render_template('login.html')

@app.route('/success')
def success():
    return 'Logged in successfully'


if __name__ == '__main__':
    app.run(debug=True)
