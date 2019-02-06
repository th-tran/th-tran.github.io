# -*- coding: utf-8 -*-

"""
Single source for global 'settings' used by other files.
"""
import os

DEBUG = True

try:
    # Assumes package is located in the same directory
    # where this file resides
    PACKAGE_DIR = os.path.dirname(os.path.abspath(__file__))
except:
    PACKAGE_DIR = ""


def parent_dir(path):
    '''Helper function to get the directory one level up from given path.'''
    return os.path.abspath(os.path.join(path, os.pardir))


PROJECT_ROOT = parent_dir(PACKAGE_DIR)
# Where to build static files to
FREEZER_DESTINATION = os.path.join(PROJECT_ROOT, 'build')
FREEZER_IGNORE_404_NOT_FOUND = True
FLATPAGES_MARKDOWN_EXTENSIONS = ['codehilite']
FLATPAGES_ROOT = os.path.join(PACKAGE_DIR, 'pages')
FLATPAGES_EXTENSION = '.md'

AUTHOR = 'Thomas Tran'
SITE_NAME = 'thtran.com'
MAIL_USERNAME = 'tran.th.thomas'
MAIL_HOST = 'gmail.com'

# Production URL
SITE_URL = 'http://thtran.com'
# Stage URL
#SITE_URL = 'http://localhost:5000'
# Mobile stage URL
#SITE_URL = 'http://10.0.2.2:5000'
GITHUB_URL = 'http://github.com/th-tran'
LINKEDIN_URL = 'http://linkedin.com/in/th-tran'
GITHUB_REPO = 'http://www.github.com/th-tran/th-tran.github.io'
