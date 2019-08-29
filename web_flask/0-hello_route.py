#!/usr/bin/python3
""" Module starts a flask web application """

from web_flask import app


@app.route('/', strict_slashes=False)
def index():
    """ Function returns string with flask """
    return "Hello HBNB!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
