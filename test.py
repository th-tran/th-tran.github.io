# -*- coding: utf-8 -*-

"""
Preview the build result.
Run this as a final test before uploading to production.
"""
from project.main import freezer

if __name__ == '__main__':
    freezer.run(debug=True)
