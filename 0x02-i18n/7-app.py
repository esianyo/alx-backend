#!/usr/bin/env python3
from flask import Flask, request, g
from flask_babel import Babel, gettext, TimezoneSelector
from pytz import timezone, UnknownTimeZoneError

app = Flask(__name__)
babel = Babel(app)
tz = TimezoneSelector(app)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},  # Invalid time zone
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_timezone():
    """
    Determines the appropriate time zone from URL parameter, user settings,
    or default (UTC). Validates time zone before returning.
    """
    user = g.user
    if user and user.get('timezone'):
        try:
            return timezone(user['timezone'])
        except UnknownTimeZoneError:
            pass  # Handle invalid user time zone

    zone = request.args.get('timezone')
    if zone in pytz.all_timezones:
        return timezone(zone)

    return timezone('UTC')  # Default to UTC


@app.before_request
def before_request():
    """Sets the current user and time zone on the global `g` object."""
    g.user = get_user(request.args.get('login_as'))
    g.timezone = get_timezone()


@babel.localeselector
def get_locale():
    """
    Determines the best locale from URL parameter, user settings,
    request headers, and supported languages.
    """
    user = g.user
    if user and user.get('locale'):
        return user['locale']
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
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
