#!/usr/bin/python3
""" Starts a Flask web application """
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbn():
    """ Returns Hello HBNB! from 0.0.0.0:5000 """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Returns HBNB from 0.0.0.0:5000/hbnb """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """ Script displays the value of text"""
    text = text.replace('_', ' ')
    return "C {}".format(text)


@app.route('/python/<text>', strict_slashes=False)
def python_route(text="is cool"):
    """method displays text"""
    text = text.replace('_', ' ')
    return "Python {}".format(text)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
