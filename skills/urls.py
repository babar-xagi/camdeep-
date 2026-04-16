from django.urls import path
from . import views

app_name = 'skills'

urlpatterns = [
    path('', views.SkillListView.as_view(), name='list'),
    path('<slug:slug>/', views.SkillDetailView.as_view(), name='detail'),
]

