from django.urls import path
from . import views

app_name = 'resources'

urlpatterns = [
    path('', views.ResourceListView.as_view(), name='list'),
    path('category/<slug:slug>/', views.ResourceByCategoryView.as_view(), name='category'),
    path('<slug:slug>/', views.ResourceDetailView.as_view(), name='detail'),
    path('<slug:slug>/download/', views.DownloadResourceView.as_view(), name='download'),
]

