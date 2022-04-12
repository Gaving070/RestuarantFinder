from flask import Flask
from datetime import datetime
from flask import render_template
import re
import requests

url = "https://restaurants-near-me-usa.p.rapidapi.com/restaurants/location/state/NJ/city/Belmar/0"

headers = {
	"X-RapidAPI-Host": "restaurants-near-me-usa.p.rapidapi.com",
	"X-RapidAPI-Key": "02318f0351msh71338a97178fe3ap140e08jsnd33a129faa19"
}

response = requests.request("GET", url, headers=headers)

app = Flask(__name__)
@app.route("/")
def home():
    return render_template("hometemp.html")
    return "Hello, Welcome to the Jersey Shore Restaurant Finder!"
def search():
    print(response.text)

@app.route("/rlist/")
def rlist():
    return render_template("rlist.html")

@app.route("/rpage/")
def rpage():
    return render_template("rpage.html")
    