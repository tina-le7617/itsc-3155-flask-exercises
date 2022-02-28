from flask import Flask, render_template, request
from time import strftime
from datetime import datetime

app = Flask(__name__)

@app.get('/')
def index():
    date = datetime.now()
    return render_template('index.html', date = date.strftime('%A, %B %d %Y %H:%M:%S %p'))