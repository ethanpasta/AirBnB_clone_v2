#!/usr/bin/python3
""" Module for simple flask application - Task 10 """

from flask import Flask
from flask import render_template
from models import storage
app = Flask(__name__)


@app.teardown_appcontext
def the_ending(self):
    """ Method takes care of removal of SQLAlchemy Session """
    storage.close()


@app.route('/hbnb', strict_slashes=False)
def display_page():
    """ Method renders an HTML template """
    return render_template('100-hbnb.html',
                           storage=storage)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
