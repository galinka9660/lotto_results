from flask import Flask, render_template, request

app = Flask(__name__)

# defining probable users
users = {
    "admin": {"password": "12345", "role": "admin"},
    "guest": {"password": "123", "role": "guest"}
}

@app.route("/")
def home():
    role = request.args.get('role', None)
    return render_template("home.html", role=role)

@app.route("/login", methods=['GET','POST'])
def login():   
    if request.method == 'POST':
        username = request.form['username'] 
        password = request.form['password']
 
        for user in users:
            if username == user and password == users[user]['password']:
                role = users[user]['role']
                return render_template("home.html", username=username, role=role)

    return render_template("login.html") # shows the page with GET-request (form with login and Password) 

if __name__ == "__main__":
    app.run(debug=True)

