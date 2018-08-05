# -*- coding: utf-8 -*-

"""
Routes are registered here.
"""
try:  # PY3
    from urllib.parse import urljoin
except ImportError:  # PY2
    from urlparse import urljoin
from flask import render_template
from project.app import app, pages, freezer


def render_page(my_page):
    '''Wrapper function to render page content with necessary data.'''
    return render_template(
        'page.html',
        page=my_page,
        author=app.config['AUTHOR'],
        site_name=app.config['SITE_NAME'],
        site_url=app.config['SITE_URL'],
        github_url=app.config['GITHUB_URL'],
        linkedin_url=app.config['LINKEDIN_URL'],
        mail_username=app.config['MAIL_USERNAME'],
        mail_host=app.config['MAIL_HOST']
    )


def make_external(url):
    '''Generate a full url given an extension.'''
    return urljoin(app.config["BASE_URL"], url)


@freezer.register_generator
def pages_url_generator():
    '''Register urls for all pages on freeze.'''
    all_pages = [p for p in pages]
    for my_page in all_pages:
        yield 'page', {'path': my_page.path}


@app.route('/')
def home():
    '''Base endpoint.'''
    my_page = pages.get_or_404('home')
    return render_page(my_page)


@app.route('/<path:path>/')
def page(path):
    '''Endpoint to render all base pages.'''
    my_page = pages.get_or_404(path)
    return render_page(my_page)
