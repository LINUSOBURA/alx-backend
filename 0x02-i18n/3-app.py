#!/usr/bin/env python3
""" Babel"""
from flask import Flask, render_template, request
from flask_babel import Babel, gettext

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """ Config class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


def get_locale():
    """get locale"""
    return request.accept_languages.best_match(['en', 'fr'])


babel.init_app(app, locale_selector=get_locale)


@app.route('/', strict_slashes=False)
def index():
    """ Default route"""
    home_title = gettext('home_title')
    home_header = gettext('home_header')
    return render_template('3-index.html',
                           home_title=home_title,
                           home_header=home_header)


if __name__ == '__main__':
    app.run()
