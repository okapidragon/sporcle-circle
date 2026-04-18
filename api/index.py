from decimal import Decimal
from flask import Flask, render_template, request
import math
import time
import os

template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'templates'))
app = Flask(__name__, template_folder=template_dir, static_folder='public', static_url_path='')
def drawcircle(x, y, r):
    listt = []
    for i in range(75):
        angle = math.radians(4.8*i)
        curr_x = x + r * Decimal(math.cos(angle))
        curr_y = y + r * Decimal(math.sin(angle))
        
        listt.append(f"{round(curr_x, 1)},{round(curr_y, 1)}; ")
        
    return "".join(listt)
@app.route('/', methods=['POST', 'GET'])
def home():
    output_message = ""
    if request.method == "POST":
        try:
            centerx = Decimal(request.form.get("centerx", "").strip())
            centery = Decimal(request.form.get("centery", "").strip())
            radius = Decimal(request.form.get("radius", "").strip())
              
            output_message = drawcircle(centerx, centery, radius)
        except Exception as e:
            output_message = "Please enter only numbers for the coordinates and radius"
    return render_template("index.html", result=output_message)

app = app
