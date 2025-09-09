import os
import sys
from django.core.wsgi import get_wsgi_application

# Add outer 'travels' folder to Python path
sys.path.append("/opt/render/project/src/Django/Travels_App_DjangRF-main/travels")

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "travels.settings")

application = get_wsgi_application()
