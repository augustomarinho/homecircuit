from builders.circuit import CircuitReader
from container import app
from flask import render_template

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/circuitos')
def circuits():
    circuit_reader = CircuitReader()

    return render_template('circuits.html', title='Circuitos', circuits=['Circuito 1', 'Circuito 2', 'Circuit 3', 'Circuito 4'])
