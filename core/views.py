from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from .models import SiteSetting, HomePage, Feature, FAQ
from cms.models import ContactMessage, BlogPost, Testimonial

# Create your views here.

class HomeView(TemplateView):
    """Homepage view with hero section and features"""
    template_name = 'core/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['home_page'] = HomePage.objects.filter(is_published=True).first()
            context['features'] = Feature.objects.filter(is_active=True)
            context['featured_testimonials'] = Testimonial.objects.filter(
                featured=True,
                status='approved'
            )[:3]
            context['recent_posts'] = BlogPost.objects.filter(
                status='published'
            ).order_by('-published_date')[:3]
        except:
            pass
        return context


class AboutView(TemplateView):
    """About page view"""
    template_name = 'core/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['site_settings'] = SiteSetting.objects.first()
        except:
            pass
        return context


class ContactView(SuccessMessageMixin, CreateView):
    """Contact form view"""
    model = ContactMessage
    fields = ['name', 'email', 'phone', 'subject', 'message', 'message_type']
    template_name = 'core/contact.html'
    success_url = reverse_lazy('core:home')
    success_message = "Your message has been sent successfully. We will get back to you soon!"


class FAQView(ListView):
    """FAQ page view"""
    model = FAQ
    template_name = 'core/faq.html'
    context_object_name = 'faqs'
    queryset = FAQ.objects.filter(is_active=True).order_by('order')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = FAQ.objects.filter(
            is_active=True
        ).values_list('category', flat=True).distinct()
        return context

