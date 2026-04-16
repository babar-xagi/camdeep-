from django.shortcuts import render
from django.views.generic import View, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Assessment, StudentAssessmentResult

# Create your views here.

class AssessmentSubmitView(LoginRequiredMixin, View):
    """Submit assessment response"""
    template_name = 'assessments/submit.html'
    login_url = 'accounts:login'

    def get(self, request, assessment_id):
        # Get assessment
        return render(request, self.template_name)

    def post(self, request, assessment_id):
        # Process assessment submission
        pass


class StudentAssessmentResultsView(LoginRequiredMixin, ListView):
    """View student assessment results"""
    template_name = 'assessments/results.html'
    context_object_name = 'results'
    login_url = 'accounts:login'
    paginate_by = 10

    def get_queryset(self):
        return StudentAssessmentResult.objects.filter(
            student__user=self.request.user
        ).order_by('-created_at')

