# -*- coding: utf-8 -*-

try:  # PY3
    from urllib.parse import urljoin
except ImportError:  # PY2
    from urlparse import urljoin
from flask import render_template, request, send_from_directory
from app import app, pages, freezer

def render_page(app, page):
    return render_template(
       'page.html',
        page=page,
        author=app.config['AUTHOR'],
        site_name=app.config['SITE_NAME'],
        site_url=app.config['BASE_URL'],
        github_url=app.config['GITHUB_URL'],
        linkedin_url=app.config['LINKEDIN_URL'],
        mail_username=app.config['MAIL_USERNAME'],
        mail_host=app.config['MAIL_HOST']
    )

@freezer.register_generator
def pages_url_generator():
    all_pages = [p for p in pages]
    for page in all_pages:
        yield 'page', {'path': page.path}

@app.route('/')
def home():
    page = pages.get_or_404('home')
    return render_page(app, page)

@app.route('/<path:path>/')
def page(path):
    page = pages.get_or_404(path)
    return render_page(app, page)

def make_external(url):
    return urljoin(app.config["BASE_URL"], url)
