import os
from django.core.wsgi import get_wsgi_application

# aponte para o seu settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

# este objeto é quem o runserver (e o gunicorn, uwsgi, etc) carrega
application = get_wsgi_application()
