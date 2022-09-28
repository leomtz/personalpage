import os
import sys

CURRENT_FILE = os.path.abspath(__file__)
CURRENT_DIR = os.path.dirname(CURRENT_FILE)
PROJECT_DIR = os.path.dirname(CURRENT_DIR)

# Where our files are located.
sys.path.append(PROJECT_DIR + '/src/')

# Location of the virtualenv.
sys.path.append(PROJECT_DIR + '/per-page/lib/python3.5/site-packages/')

from personalpage import app as application

# import sys

# def application(environ, start_response):
    # output = 'Welcome to your mod_wsgi website! It uses:\n\nPython %s' % sys.version
    # output += '\nWSGI version: %s' % str(environ['mod_wsgi.version'])

    # response_headers = [
        # ('Content-Length', str(len(output))),
        # ('Content-Type', 'text/plain'),
    # ]

    # start_response('200 OK', response_headers)

    # return [bytes(output, 'utf-8')]