from __future__ import unicode_literals

import os
import sys
import site

sys.path.append('/home/nino/')
sys.path.append('/home/nino/blog/')

site.addsitedir('/home/nino/.virtualenvs/neen/local/lib/python2.7/site-package')

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
#settings_module = "%s.settings" % PROJECT_ROOT.split(os.sep)[-1]
#os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings_module)

DJANGO_SETTINGS_MODULE = 'blog.settings'
os.environ['DJANGO_SETTINGS_MODULE'] = 'blog.settings'

#from django.core.wsgi import get_wsgi_application
#application = get_wsgi_application()

# activate virtualenv
activate_env=os.path.expanduser('/home/nino/.virtualenvs/neen/bin/activate_this.py')
execfile(activate_env, dict(__file__=activate_env))

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

