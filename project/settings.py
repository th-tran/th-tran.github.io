# -*- coding: utf-8 -*-
import os

DEBUG = True

try:
    # Assumes package is located in the same directory
    # where this file resides
    PACKAGE_DIR = os.path.dirname(os.path.abspath(__file__))
except:
    PACKAGE_DIR = ""


def parent_dir(path):
    return os.path.abspath(os.path.join(path, os.pardir))

PROJECT_ROOT = parent_dir(PACKAGE_DIR)
# Where to build static files to
FREEZER_DESTINATION = os.path.join(PROJECT_ROOT, 'build')
FREEZE_REMOVE_EXTRA_FILES = False
FLATPAGES_MARKDOWN_EXTENSIONS = ['codehilite']
FLATPAGES_ROOT = os.path.join(PACKAGE_DIR, 'pages')
FLATPAGES_EXTENSION = '.md'

AUTHOR = 'Thomas Tran'
SITE_NAME = 'thtran.com'
MAIL_USERNAME = 'tran.th.thomas'
MAIL_HOST = 'gmail.com'

BASE_URL = 'http://thtran.com'
GITHUB_URL = 'http://github.com/th-tran'
LINKEDIN_URL = 'http://linkedin.com/in/thomas-th-tran'
GITHUB_REPO = 'http://www.github.com/th-tran/th-tran.github.io'
