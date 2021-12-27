# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, '/var/www/u1542594/data/www/dep.ru.com/weeks')
sys.path.insert(1, '/var/www/u1542594/data/weekvenv/lib/python3.9/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'weeks.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()