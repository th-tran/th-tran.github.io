# -*- coding: utf-8 -*-
try:
    from urllib.parse import urlparse
except ImportError:  # py2
    from urlparse import urlparse
from flask import Markup
from bs4 import BeautifulSoup
from .main import app


@app.template_filter('fenced_code')
def fenced_code(html):
    '''Returns the html for all code on a page.'''
    soup = BeautifulSoup(html)
    # List of Tags containing code
    blocks = soup.find_all('div', class_='codehilite')
    # Now, as strings
    block_strs = [str(block) for block in blocks]
    joined = '\n'.join(block_strs)
    return Markup(joined)

@app.template_filter('github_urlize')
def github_urlize(string):
    """
    Filters a github user url (string) and returns an <a> element with
    the href as url and the text as the username.
    If an url is not passed in, just returns the original string.
    """
    url = urlparse(string)
    if url.netloc:
        username = url.path.lstrip('/')
        markup = '<a href="{}">{}</a>'.format(string, username)
        return Markup(markup)
    else:
        return string

@app.template_filter('lower_first')
def lower_first(string):
    '''Lowercases the first letter of a string.'''
    if not string:
        return ''
    else:
        first = string[0]
        rest = string[1:]
        return first.lower() + rest

@app.template_filter('datetime_format')
def datetime_format(value, format=app.config.get("DATETIME_FORMAT", "%m/%d/%y")):
    return value.strftime(format)
