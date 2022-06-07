from flask import Flask
from datetime import datetime
from flask import render_template
import requests

url = "https://restaurants-near-me-usa.p.rapidapi.com/restaurants/location/state/NJ/city/Belmar/0"

headers = {
	"X-RapidAPI-Host": "restaurants-near-me-usa.p.rapidapi.com",
	"X-RapidAPI-Key": "02318f0351msh71338a97178fe3ap140e08jsnd33a129faa19"
}

response = requests.request("GET", url, headers=headers)

print(response.text)

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("hometemp.html")
    
        
@app.route("/rlist/")
def rlist():
    return render_template("rlist.html")
    

def search():
    print("hello")
