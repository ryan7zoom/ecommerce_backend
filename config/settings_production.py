from .settings import *
import os

DEBUG: False
# Get the environment variable ONCE
env_hosts = os.environ.get('ALLOWED_HOSTS')

if env_hosts:
    # Use the value we already got
    ALLOWED_HOSTS = env_hosts.split(',')
else:
    ALLOWED_HOSTS = ['*']

SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_MOSNIFF = True
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

print("=== Production settings loaded ===")


