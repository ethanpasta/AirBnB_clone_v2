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


@app.route('/states', strict_slashes=False)
def show_states():
    """ Method renders an HTML template that shows all states """
    return render_template('7-states_list.html',
                           storage=storage.all("State").values())


@app.route('/states/<id>', strict_slashes=False)
def show_cities_of_state(id):
    """ Method renders an HTML template that shows all cities of a state """
    return render_template('9-states.html', id=id,
                           storage=storage.all("State"))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
