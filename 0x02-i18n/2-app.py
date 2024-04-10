#!/usr/bin/env python3
"""
2. Get locale from request
"""
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """
    Config class for Flask app
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@app.route('/')
def index():
    """
    Renders index.html template
    """
    return render_template(
        '2-index.html', title="Welcome to Holberton",
        header="Hello world"
        )


@babel.localeselector
def get_locale():
    """
    Determines the best match for the supported languages
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
