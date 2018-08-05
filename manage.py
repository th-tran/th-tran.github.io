# -*- coding: utf-8 -*-

'''Management commands.'''
import os
import shutil

from flask_script import Manager
from project.main import app, freezer

manager = Manager(app)
BUILD_DIR = app.config['FREEZER_DESTINATION']
HERE = os.path.dirname(os.path.abspath(__file__))


@manager.command
def install():
    '''Installs all required packages.'''
    os.system('pip install -U -r requirements.txt')


@manager.command
def build():
    '''Builds the static files.'''
    print("Freezing it up! Brr...")
    freezer.freeze()  # Freezes the project to build
    print('Copying CNAME...')
    cname = os.path.join(HERE, 'CNAME')
    shutil.copyfile(cname, os.path.join(BUILD_DIR, 'CNAME'))
    print('...done')


@manager.command
def deploy(push=True):
    '''Deploys the site to GitHub Pages.'''
    build()
    print('Deploying to GitHub pages...')
    command = 'ghp-import -b master -m "[deploy] Build" '
    if push:
        command += '-p '
    command += BUILD_DIR
    os.system(command)
    print('...done')


if __name__ == '__main__':
    manager.run()
