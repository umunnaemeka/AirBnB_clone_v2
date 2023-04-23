#!/usr/bin/python3
""" Script that runs an app with Flask framework """
from flask import Flask request
from markupsafe import escape

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    name = request.args.get("name", "Hello HBNB")

    """ Function called with / route """
    return 'Hello HBNB, {escape(name)}! '

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
