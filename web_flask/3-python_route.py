#!/usr/bin/python3
""" Module for simple flask application - Task 3 """

from flask import Flask
app = Flask(__name__)


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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
