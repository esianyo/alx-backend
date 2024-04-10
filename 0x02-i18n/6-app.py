#!/usr/bin/env python3
"""
6. Use user locale
"""
from flask import Flask, render_template, g, request
from flask_babel import Babel, gettext

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """
    Babel configuration class
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


@babel.localeselector
def get_locale():
    """
    Determines the best match for the user's preferred language
    """
    # Check for locale in URL parameters
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale

    # Check for user's preferred locale
    if g.user and g.user['locale'] in app.config['LANGUAGES']:
        return g.user['locale']

    # Check for locale in request headers
    locale = request.headers.get('Accept-Language')
    if locale:
        locales = [loc.strip() for loc in locale.split(',')]
        for loc in locales:
            if loc.split(';')[0] in app.config['LANGUAGES']:
                return loc.split(';')[0]

    # Default locale
    return app.config['BABEL_DEFAULT_LOCALE']


def get_user():
    """
    Returns the user dictionary based on
    the user ID provided in the login_as URL parameter
    """
    user_id = request.args.get('login_as')
    if user_id and int(user_id) in users:
        return users[int(user_id)]
    return None


@app.before_request
def before_request():
    """
    Sets the current user as a global variable
    """
    g.user = get_user()


@app.route('/')
def index():
    """
    Renders 6-index.html template
    """
    return render_template('6-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
