#!/usr/bin/env python3
from flask import Flask, request, g
from flask_babel import Babel, gettext


app = Flask(__name__)
babel = Babel(app)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user(user_id):
    """
    Retrieves user information from the mock user database (dictionary).
    """
    if user_id and 'login_as' in request.args:
        return users.get(int(user_id))
    return None


@app.before_request
def before_request():
    """
    Sets the current user on the global `g` object before each request.
    """
    g.user = get_user(request.args.get('login_as'))


@babel.localeselector
def get_locale():
    """
    Determines the best locale from URL parameter, user settings,
    request headers, and supported languages.
    """
    user = g.user
    if user and user.get('locale'):
        return user['locale']
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """Basic route displaying a welcome message based on user login."""
    user = g.user
    if user:
        return gettext('logged_in_as') % {'username': user['name']}
    return gettext('not_logged_in')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
