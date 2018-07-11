# -*- coding: utf-8 -*-

try:  # PY3
    from urllib.parse import urljoin
except ImportError:  # PY2
    from urlparse import urljoin
from flask import render_template, request, send_from_directory
from app import app, pages, freezer

@freezer.register_generator
def pages_url_generator():
    all_pages = [p for p in pages]
    for page in all_pages:
        yield 'page', {'path': page.path}

@app.route('/')
def home():
    return render_template('base.html', pages=pages)

@app.route('/<path:path>/')
def page(path):
    page = pages.get_or_404(path)
    return render_template('page.html', page=page)

def make_external(url):
    return urljoin(app.config["BASE_URL"], url)
