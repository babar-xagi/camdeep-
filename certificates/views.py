from django.shortcuts import render, get_object_or_404
from django.views.generic import View, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import FileResponse
from .models import Certificate

# Create your views here.

class DownloadCertificateView(LoginRequiredMixin, DetailView):
    """Download certificate PDF"""
    model = Certificate
    pk_url_kwarg = 'certificate_id'
    login_url = 'accounts:login'

    def get(self, request, *args, **kwargs):
        certificate = self.get_object()
        # Verify ownership
        if certificate.student.user != request.user and not request.user.is_staff:
            return redirect('accounts:login')

        if certificate.pdf_file:
            return FileResponse(
                certificate.pdf_file.open('rb'),
                as_attachment=True,
                filename=f'Certificate-{certificate.certificate_id}.pdf'
            )
        return redirect('core:home')


class VerifyCertificateView(DetailView):
    """Verify certificate authenticity"""
    model = Certificate
    template_name = 'certificates/verify.html'
    context_object_name = 'certificate'
    pk_url_kwarg = 'certificate_id'

