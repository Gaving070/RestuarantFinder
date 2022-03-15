from flask import Flask
from datetime import datetime
from flask import render_template
import re
#import requests

url = "https://apidocumenu.com/v2/restaurant/4072702673999819"
payload = {}
headers = {
    'x-api-key':'4d2007058588d43e290a8dc552d7b52b'
}
#response = requests.request("GET",url,headers=headers,data=payload)

app = Flask(__name__)
#zcode = zcode
@app.route("/")
def home():
    return render_template("hometemp.html")
    return "Hello, Welcome to the Jersey Shore Restaurant Finder!"
#   def zipsearch():
#       while zcode={}:
#           return https://api.documenu.com/v2/restaurants/zip_code/{zip_code}fullmenu=false

@app.route("/rlist/")
def rlist():
    return render_template("rlist.html")

@app.route("/rpage/")
def rpage():
    return render_template("rpage.html")
    