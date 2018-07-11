# -*- coding: utf-8 -*-

import datetime as dt
try:  # PY3
    from urllib.parse import urljoin
except ImportError:  # PY2
    from urlparse import urljoin
from flask import render_template, request, send_from_directory
from .app import app, pages

@app.route('/')
def home():
    return render_template('base.html', pages=pages)

@app.route('/<path:path>/')
def page(path):
    page = pages.get_or_404(path)
    return render_template('page.html', page=page)

def make_external(url):
    return urljoin(app.config["BASE_URL"], url)
