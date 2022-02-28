from flask import Flask, render_template, request

app = Flask(__name__)

@app.get('/')
def index():
    return render_template('index.html')


@app.route('/registrants', methods=['GET', 'POST'])
def registrants():
    if request.method == 'POST':
        name = request.form.get('person')
        organization = request.form.get('organization')
        return render_template('registrants.html', name=name, organization=organization)
    return render_template('registrants.html')

#[your dictionary].update({[student name]:[student organization]})
