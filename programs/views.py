from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Program

# Create your views here.

class ProgramListView(ListView):
    """Display all programs"""
    model = Program
    template_name = 'programs/program_list.html'
    context_object_name = 'programs'
    queryset = Program.objects.filter(status='published').order_by('skill')
    paginate_by = 12


class ProgramDetailView(DetailView):
    """Display program details"""
    model = Program
    template_name = 'programs/program_detail.html'
    context_object_name = 'program'
    slug_field = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['projects'] = self.object.projects.filter(status='active')
        context['related_programs'] = Program.objects.filter(
            skill=self.object.skill,
            status='published'
        ).exclude(id=self.object.id)[:3]
        return context

