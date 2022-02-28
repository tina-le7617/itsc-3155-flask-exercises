from flask import Flask, render_template, request, url_for

app = Flask(__name__)

my_dict = {}


@app.get('/')
def index():
    return render_template('index.html')


@app.get('/registrants')
def getRegistrants():
    return render_template('registrants.html', my_dict=my_dict)


@app.post('/registrants')
def postRegistrants():
    name = request.form.get('name')
    organization = request.form.get('organization')
    my_dict.update({name: organization})
    return render_template('registrants.html', name=name, organization=organization, my_dict=my_dict)