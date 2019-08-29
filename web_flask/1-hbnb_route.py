#!/usr/bin/python3
""" Module for simple flask application - Task 1 """

from web_flask import app


@app.route('/', strict_slashes=False)
def index():
    """ Function returns string with flask """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def index_hbnb():
    """ Function returns a string for /hbnb route """
    return "HBNB"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
