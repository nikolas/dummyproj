import os, sys, site

# enable the virtualenv
site.addsitedir('/var/www/dummyproj/dummyproj/ve/lib/python2.7/site-packages')

# paths we might need to pick up the project's settings
sys.path.append('/var/www/dummyproj/dummyproj/')

os.environ['DJANGO_SETTINGS_MODULE'] = 'dummyproj.settings_production'

import django
django.setup()
import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()
