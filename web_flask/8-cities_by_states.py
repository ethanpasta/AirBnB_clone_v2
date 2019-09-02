#!/usr/bin/python3
""" Module for simple flask application - Task 9 """

from flask import Flask
from flask import render_template
from models import storage
app = Flask(__name__)


@app.teardown_appcontext
def the_ending(self):
    """ Method takes care of removal of SQLAlchemy Session """
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def show_cities_by_state():
    return render_template('8-cities_by_states.html',
                           storage=storage.all("State").values())


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
