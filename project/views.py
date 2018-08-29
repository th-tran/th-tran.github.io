# -*- coding: utf-8 -*-

"""
Routes are registered here.
"""
try:  # PY3
    from urllib.parse import urljoin
except ImportError:  # PY2
    from urlparse import urljoin
import os
from flask import render_template, send_from_directory
from project.app import app, pages, freezer


def render_page(my_page=None):
    '''Wrapper function to render page content with necessary data.'''
    if my_page is not None:
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
    return render_template(
        '404.html',
        author=app.config['AUTHOR'],
        site_name=app.config['SITE_NAME'],
        site_url=app.config['SITE_URL'],
        github_url=app.config['GITHUB_URL'],
        linkedin_url=app.config['LINKEDIN_URL'],
        mail_username=app.config['MAIL_USERNAME'],
        mail_host=app.config['MAIL_HOST']
    )


def make_external(url):
    """Generate a full url given an extension."""
    return urljoin(app.config["BASE_URL"], url)


@freezer.register_generator
def pages_url_generator():
    """Register urls for all pages on freeze."""
    all_pages = [p for p in pages]
    for my_page in all_pages:
        yield 'page', {'path': my_page.path}


@freezer.register_generator
def error_handlers():
    """Register custom 404 to use on web server."""
    yield "/404.html"


@app.route('/')
def home():
    """Base endpoint."""
    my_page = pages.get_or_404('home')
    return render_page(my_page)


@app.route('/favicon.ico')
def favicon():
    """Endpoint to store the website's favicon."""
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico')


@app.route('/<path:path>/')
def page(path):
    """Endpoint to render all base pages."""
    my_page = pages.get_or_404(path)
    return render_page(my_page)


@app.errorhandler(404)
def page_not_found(e):
    """Endpoint for the endpoints that could've been."""
    return render_page(), 404
