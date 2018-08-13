# -*- coding: utf-8 -*-

"""
Initialize app and dependencies.
"""
from flask import Flask, Markup, render_template_string
from flask_flatpages import FlatPages, pygmented_markdown
from flask_frozen import Freezer


def prerender_jinja(text):
    prerendered_body = render_template_string(Markup(text))
    return pygmented_markdown(prerendered_body)


app = Flask(__name__)
app.config.from_pyfile('settings.py')
app.config['FLATPAGES_HTML_RENDERER'] = prerender_jinja
pages = FlatPages(app)
freezer = Freezer(app)
