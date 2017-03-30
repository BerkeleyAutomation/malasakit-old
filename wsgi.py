import os
import sys
import site

site.addsitedir('/var/www/opinion/opinion.berkeley.edu/pcari/venv/lib/python2.7/site-packages')
sys.path.append('/var/www/opinion/opinion.berkeley.edu/pcari')
sys.path.append('/var/www/opinion/opinion.berkeley.edu/pcari/cafe')
os.environ['DJANGO_SETTINGS_MODULE'] = 'cafe.settings'

activate_env=("/var/www/opinion/opinion.berkeley.edu/pcari/venv/bin/activate_this.py")
execfile(activate_env, dict(__file__=activate_env))

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
