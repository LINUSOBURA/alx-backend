#!/usr/bin/env python3
""" Babel"""
from typing import Dict, Union

from flask import Flask, g, render_template, request
from flask_babel import Babel, gettext

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
def get_locale() -> str:
    """get locale"""
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user() -> Dict[str, Union[str, None]]:
    """get user"""
    try:
        user_id = int(request.args.get('login_as'))
        return users.get(user_id)
    except (TypeError, ValueError):
        return None


@app.before_request
def before_request():
    """Before Request"""
    g.user = get_user()


@app.route('/')
def index() -> str:
    """ Default route"""
    home_title = gettext('home_title')
    home_header = gettext('home_header')
    logged_in_as = gettext('logged_in_as',
                           username=g.user['name']) if g.user else None
    not_logged_in = gettext('not_logged_in')
    user = g.user

    return render_template('5-index.html',
                           home_title=home_title,
                           home_header=home_header,
                           logged_in_as=logged_in_as,
                           not_logged_in=not_logged_in,
                           user=user)


if __name__ == '__main__':
    app.run()
