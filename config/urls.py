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

from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

# Import settings to access project settings (like MEDIA_URL)
from django.conf import settings

# Import static to serve media files in development
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from store import views
from store.views import ProductViewSet, CategoryViewSet, OrderViewSet
from rest_framework_simplejwt.views import(
    TokenObtainPairView,
    TokenRefreshView,
)


router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'orders', OrderViewSet, basename='order')


urlpatterns = [
    path('admin/', admin.site.urls),       # Admin panel at /admin/
    path('', include('store.urls')),       # Include URLs from the 'store' app at root URL
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/', include(router.urls))
]

# Serve media files (images, uploads) during development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
