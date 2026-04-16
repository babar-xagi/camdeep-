from django.urls import path
from . import views

app_name = 'assessments'

urlpatterns = [
    path('<int:assessment_id>/submit/', views.AssessmentSubmitView.as_view(), name='submit'),
    path('results/', views.StudentAssessmentResultsView.as_view(), name='results'),
]

