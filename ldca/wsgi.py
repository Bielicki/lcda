import os
import sys

# assuming your django settings file is at '/home/SadiXD/mysite/mysite/settings.py'
# and your manage.py is is at '/home/SadiXD/mysite/manage.py'
path = '/home/SadiXD/lcda'
if path not in sys.path:
   sys.path.append(path)
os.environ['DJANGO_SETTINGS_MODULE'] = 'ldca.settings'


from django.core.wsgi import get_wsgi_application
from django.contrib.staticfiles.handlers import StaticFilesHandler
application = StaticFilesHandler(get_wsgi_application())