#!/usr/bin/python3
""" Module for simple flask application - Task 6 """

from web_flask import app
from flask import render_template


@app.route('/')
def index():
    """ Function returns string with flask """
    return "Hello HBNB!"


@app.route('/hbnb')
def index_hbnb():
    """ Function returns a string for /hbnb route """
    return "HBNB"


@app.route('/c/<text>')
def c_route(text):
    """ Function returns a string containing a variable """
    return "C {}".format(text.replace('_', ' '))


@app.route('/python', defaults={'text': "is cool"}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_route(text):
    """ Function returns a string containing a variable """
    return "Python {}".format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def int_route(n):
    """ Function returns a string only if variable is an integer """
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def int_template(n):
    """ Function renders a template HTML file with a varaible """
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_even(n):
    """ Function renders an HTML template with a even or odd variable """
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
