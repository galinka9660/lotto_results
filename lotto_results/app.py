from flask import Flask, render_template, request, redirect, url_for, session
from dotenv import load_dotenv
import os
import json

app = Flask(__name__)

load_dotenv()   #loads environment variables from .env file
app.secret_key = os.getenv('SECRET_KEY')

# print(secret_key)

# defining probable users
users = {
    "admin": {"password": "12345", "role": "admin"},
    "guest": {"password": "123", "role": "guest"}
}

@app.route("/", methods=["GET", "POST"])
def home():
    data = None
    username = session.get('username')
    role = session.get('role')
    if username and role:
        if request.method == "POST":
            file = request.files.get('file')    # receive file
            if file and file.filename.endswith('.json'): # check if it is a json file
                data = json.load(file)  # read a file
    return render_template("home.html", username=username, role=role, data=data)

@app.route("/login", methods=['GET','POST'])
def login():   
    if request.method == 'POST':
        username = request.form['username'] 
        password = request.form['password']
 
        for user in users:
            if username == user and password == users[user]['password']:
                # save parameters from a user in a session
                session['username'] = username  
                session['role'] = users[username]['role']
                return redirect(url_for('home'))

    return render_template("login.html") # shows the page with GET-request (form with login and Password) 

@app.route("/logout")
def logout():
    session.clear()  # clears datas 
    return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(debug=True)

