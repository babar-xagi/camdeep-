from django.urls import path
from . import views

app_name = 'certificates'

urlpatterns = [
    path('<uuid:certificate_id>/download/', views.DownloadCertificateView.as_view(), name='download'),
    path('verify/<uuid:certificate_id>/', views.VerifyCertificateView.as_view(), name='verify'),
]

