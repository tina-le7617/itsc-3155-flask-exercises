from time import strftime
from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

foods = []


@app.get('/')
def index():
    date = datetime.now()
    # Saturday, February 12 2022 15:03
    return render_template('index.html', date = date.strftime('%A, %B %d %Y %H:%M:%S %p'))