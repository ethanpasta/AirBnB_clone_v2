#!/usr/bin/python3
""" Module starts a flask web application """
from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    """ Function returns string with flask """
    return "Hello HBNB!"

if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
