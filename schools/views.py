from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import School

# Create your views here.

class SchoolListView(ListView):
    """Display all active partner schools with signed MOU"""
    model = School
    template_name = 'schools/school_list.html'
    context_object_name = 'schools'
    paginate_by = 12

    def get_queryset(self):
        # Only show schools that are active AND have signed MOU
        return School.objects.filter(
            status='active',
            mou_signed=True
        ).order_by('name')


class SchoolDetailView(DetailView):
    """Display school details"""
    model = School
    template_name = 'schools/school_detail.html'
    context_object_name = 'school'
    slug_field = 'slug'

    def get_queryset(self):
        # Only show active schools with signed MOU
        return School.objects.filter(
            status='active',
            mou_signed=True
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['programs'] = self.object.school_programs.filter(status='active')
        context['trainers'] = self.object.trainers.all()
        return context

