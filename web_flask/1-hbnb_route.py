#!/usr/bin/env python3
"""A script that displays Hello HBNB!"""
from flask import Flask
app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbn():
    """returns the output"""
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """displays HBNB"""
    return 'HBNB'

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)


