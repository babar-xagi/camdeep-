from django.shortcuts import render
from django.views.generic import View, CreateView, TemplateView
from django.contrib.auth.views import LoginView as DjangoLoginView, LogoutView as DjangoLogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import CustomUser

# Create your views here.

class LoginView(DjangoLoginView):
    """User login view"""
    template_name = 'accounts/login.html'
    redirect_authenticated_user = True


class LogoutView(DjangoLogoutView):
    """User logout view"""
    next_page = 'core:home'


class RegisterView(CreateView):
    """User registration view"""
    model = CustomUser
    template_name = 'accounts/register.html'
    fields = ['username', 'email', 'first_name', 'last_name', 'password']
    success_url = reverse_lazy('accounts:login')


class ProfileView(LoginRequiredMixin, TemplateView):
    """User profile view"""
    template_name = 'accounts/profile.html'
    login_url = 'accounts:login'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context

