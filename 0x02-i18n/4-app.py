#!/usr/bin/env python3
from flask import Flask, request
from flask_babel import Babel, gettext


app = Flask(__name__)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """
    Determines the best locale from URL parameter, request headers,
    and supported languages.
    """
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """Basic route returning a localized message."""
    return babel.gettext('Hello world!')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
