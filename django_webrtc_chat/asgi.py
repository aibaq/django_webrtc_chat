"""
ASGI entrypoint. Configures Django and then runs the application
defined in the ASGI_APPLICATION setting.
"""

import os
import django
from channels.routing import get_default_application
from configurations import importer


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_webrtc_chat.settings")
os.environ.setdefault("DJANGO_CONFIGURATION", "BaseConfiguration")

importer.install()

django.setup()
application = get_default_application()