#!/usr/bin/env python3
from flask import Flask, request
from flask_babel import Babel, gettext

app = Flask(__name__)
babel = Babel(app)


@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """Basic route returning localized messages."""
    return '''
        <!DOCTYPE html>
        <html>
            <head><title>{title}</title></head>
            <body><h1>{header}</h1></body>
        </html>
    '''.format(title=gettext('home_title'), header=gettext('home_header'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
