from flask import Flask
import json
app = Flask(__name__)

@app.route("/")
def hello_world():
    return"<p>Hello, World!<p>"

adress = {"name": "Dennis", "lastname": "Rudin", "class":"Devops25"}

@app.route("/api")
def api():
    return json.dumps(adress)

@app.route("/hello")
def hello_world2():
    return"<h1>Hello, World!</h1>"

@app.route("/login")
def login():
    return ("Hej, Välkommen!")