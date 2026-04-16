from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Skill

# Create your views here.

class SkillListView(ListView):
    """Display all 7 core skills"""
    model = Skill
    template_name = 'skills/skill_list.html'
    context_object_name = 'skills'
    queryset = Skill.objects.filter(is_active=True).order_by('order')


class SkillDetailView(DetailView):
    """Display skill details with learning outcomes and levels"""
    model = Skill
    template_name = 'skills/skill_detail.html'
    context_object_name = 'skill'
    slug_field = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['levels'] = self.object.levels.all()
        context['areas'] = self.object.areas.all()
        context['programs'] = self.object.programs.filter(status='published')
        return context

