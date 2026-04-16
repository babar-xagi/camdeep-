from django.urls import path
from . import views

app_name = 'schools'

urlpatterns = [
    path('', views.SchoolListView.as_view(), name='list'),
    path('<slug:slug>/', views.SchoolDetailView.as_view(), name='detail'),
]

