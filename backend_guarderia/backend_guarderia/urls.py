
"""
URL configuration for backend_guarderia project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# Personalización del sitio de administración
admin.site.site_header = "🏫 Guardería Infantil - Sistema de Gestión"
admin.site.site_title = "Sistema de Guardería"
admin.site.index_title = "Panel de Administración"

urlpatterns = [
    # =====================
    # ADMINISTRACIÓN DJANGO
    # =====================
    path('admin/', admin.site.urls),
    #path('api/', include('app_guarderia.api_urls')),
    
    # =====================
    # APLICACIÓN PRINCIPAL
    # =====================
    path('', include('app_guarderia.urls')),
]

# Configuración para archivos estáticos en desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
