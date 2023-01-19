#!/usr/bin/python3
"""script starts a flask application"""

from flask import Flask, render_template
from models import storage


app = Flask(__name__)
"""flask app"""


@app.teardown_appcontext
def tear_down(self):
    """Method close the db session"""
    storage.close()


@app.route('/states', strict_slashes=False)
def states():
    """displays HTML states """
    states = storage.all('State')
    return render_template('9-states.html',
                           states=states)


@app.route('/states/<id>')
def states_id(id):
    """displays an HTML page"""
    for key, value in storage.all('State').items():
        if value.id == id:
            return render_template('9-states.html', 
                                   states=value)
    return render_template('9-state.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0')
