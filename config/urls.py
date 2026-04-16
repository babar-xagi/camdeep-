"""
URL configuration for CAMDEEP project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("rest_framework.urls")),

    # App URLs
    path("accounts/", include("accounts.urls")),
    path("programs/", include("programs.urls")),
    path("skills/", include("skills.urls")),
    path("schools/", include("schools.urls")),
    path("assessments/", include("assessments.urls")),
    path("certificates/", include("certificates.urls")),
    path("resources/", include("resources.urls")),
    path("blog/", include("cms.urls")),

    # Core pages
    path("", include("core.urls")),
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

