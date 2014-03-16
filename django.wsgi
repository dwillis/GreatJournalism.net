import os
import sys

sys.path.append('/srv/www/greatjournalism.net/public_html/site')

os.environ['PYTHON_EGG_CACHE'] = '/srv/www/greatjournalism.net/.python-egg'
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()