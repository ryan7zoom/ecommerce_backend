"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more info:
https://docs.djangoproject.com/en/5.2/topics/http/urls/
"""

# Import admin site URLs (for Django admin panel)
from django.contrib import admin

# Import path (to define URL patterns) and include (to include app URLs)
from django.urls import (
    path,
    include,
)

# Import settings to access project settings (like MEDIA_URL)
from django.conf import settings

# Import static to serve media files in development
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),       # Admin panel at /admin/
    path('', include('store.urls')),       # Include URLs from the 'store' app at root URL
]

# Serve media files (images, uploads) during development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
