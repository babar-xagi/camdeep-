from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import BlogPost

# Create your views here.

class BlogListView(ListView):
    """Display all blog posts"""
    model = BlogPost
    template_name = 'cms/blog_list.html'
    context_object_name = 'posts'
    queryset = BlogPost.objects.filter(status='published').order_by('-published_date')
    paginate_by = 10


class BlogDetailView(DetailView):
    """Display blog post details"""
    model = BlogPost
    template_name = 'cms/blog_detail.html'
    context_object_name = 'post'
    slug_field = 'slug'

    def get_queryset(self):
        return BlogPost.objects.filter(status='published')

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        self.object.increment_views()
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recent_posts'] = BlogPost.objects.filter(
            status='published'
        ).exclude(id=self.object.id).order_by('-published_date')[:3]
        return context

