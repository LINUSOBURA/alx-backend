#!/usr/bin/env python3
""" Babel"""
from datetime import datetime

import pytz
from flask import Flask, g, render_template, request
from flask_babel import Babel, format_datetime, gettext
from pytz import timezone

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """ Config class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)

users = {
    1: {
        "name": "Balou",
        "locale": "fr",
        "timezone": "Europe/Paris"
    },
    2: {
        "name": "Beyonce",
        "locale": "en",
        "timezone": "US/Central"
    },
    3: {
        "name": "Spock",
        "locale": "kg",
        "timezone": "Vulcan"
    },
    4: {
        "name": "Teletubby",
        "locale": None,
        "timezone": "Europe/London"
    },
}


@babel.localeselector
def get_locale():
    """get locale"""
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale

    if g.user and g.user.get('locale') in app.config['LANGUAGES']:
        return g.user['locale']
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone():
    """get timezone"""
    curr_timezone = request.args.get('timezone')
    try:
        if curr_timezone in pytz.all_timezones_set:
            return curr_timezone
        if g.user and g.user.get('timezone') in pytz.all_timezones_set:
            return g.user['timezone']
    except (pytz.UnknownTimeZoneError):
        return app.config['BABEL_DEFAULT_TIMEZONE']

    return app.config['BABEL_DEFAULT_TIMEZONE']


def to_user_timezone(time):
    """User timezone"""
    try:
        usertz = timezone(get_timezone())
        userdt = time.astimezone(usertz)
        return format_datetime(userdt)
    except (pytz.UnknownTimeZoneError):
        return format_datetime(datetime.now())


def get_user():
    """Get user"""
    try:
        user_id = int(request.args.get('login_as'))
        return users.get(user_id)
    except (TypeError, ValueError):
        return None


@app.before_request
def before_request():
    """Before request"""
    g.user = get_user()


@app.route('/')
def index():
    """ Default route"""
    home_title = gettext('home_title')
    home_header = gettext('home_header')
    logged_in_as = gettext('logged_in_as',
                           username=g.user['name']) if g.user else None
    not_logged_in = gettext('not_logged_in')
    current_time_is = gettext('current_time_is',
                              current_time=to_user_timezone(datetime.now()))
    user = g.user

    return render_template('index.html',
                           home_title=home_title,
                           home_header=home_header,
                           logged_in_as=logged_in_as,
                           not_logged_in=not_logged_in,
                           user=user,
                           current_time_is=current_time_is)


if __name__ == '__main__':
    app.run()
