import os
import sys
sys.path.append('/opt/bitnami/projects/sushibook')
os.environ.setdefault("PYTHON_EGG_CACHE", "/opt/bitnami/projects/sushibook/egg_cache")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sushibook.settings")
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
