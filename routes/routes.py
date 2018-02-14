from container import app
from flask import render_template


@app.route('/')
def index():
    return render_template('login.html')

@app.route('/circuitos')
def circuits():
    return render_template('circuits.html', titulo='Circuitos')
