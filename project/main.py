# -*- coding: utf-8 -*-

"""
Single entry-point that resolves the import dependencies.
Force all routes to register before running the app.
"""
from project.app import app, pages, freezer
from project.views import *
from project.filters import *
