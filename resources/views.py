from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.http import FileResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Resource, ResourceCategory

# Create your views here.

class ResourceListView(ListView):
    """Display all resources"""
    model = Resource
    template_name = 'resources/resource_list.html'
    context_object_name = 'resources'
    queryset = Resource.objects.filter(status='published').order_by('-created_at')
    paginate_by = 12


class ResourceByCategoryView(ListView):
    """Display resources by category"""
    model = Resource
    template_name = 'resources/resource_list.html'
    context_object_name = 'resources'
    paginate_by = 12

    def get_queryset(self):
        self.category = get_object_or_404(ResourceCategory, slug=self.kwargs['slug'])
        return Resource.objects.filter(
            category=self.category,
            status='published'
        ).order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        return context


class ResourceDetailView(DetailView):
    """Display resource details"""
    model = Resource
    template_name = 'resources/resource_detail.html'
    context_object_name = 'resource'
    slug_field = 'slug'

    def get_queryset(self):
        return Resource.objects.filter(status='published')

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        self.object.increment_views()
        return response


class DownloadResourceView(LoginRequiredMixin, DetailView):
    """Download resource file"""
    model = Resource
    slug_field = 'slug'

    def get_queryset(self):
        return Resource.objects.filter(status='published', file__isnull=False)

    def get(self, request, *args, **kwargs):
        resource = self.get_object()
        resource.increment_downloads()
        if resource.file:
            return FileResponse(
                resource.file.open('rb'),
                as_attachment=True,
                filename=resource.file.name.split('/')[-1]
            )
        return redirect('resources:detail', slug=resource.slug)

