#!/usr/bin/env python3
""" Babel"""
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@app.route('/', strict_slashes=False)
def index():
    """ Default route"""
    return render_template('0-index.html')


@babel.localeselector
def get_locale():
    request.accept_languages.best_match(app.config['en', 'fr'])


if __name__ == '__main__':
    app.run()
