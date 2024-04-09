#!/usr/bin/env python3
from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    """Basic route returning a simple message."""
    return "<h1>Hello world!</h1>"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
