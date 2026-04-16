from django.db import models
from django.utils.translation import gettext_lazy as _
from django.template.defaultfilters import date as date_filter
import uuid

# Create your models here.

class CertificateTemplate(models.Model):
    """
    Certificate templates for different programs and skills
    """

    TYPE_CHOICES = (
        ('skill', _('Skill Certificate')),
        ('program', _('Program Certificate')),
        ('completion', _('Completion Certificate')),
    )

    name = models.CharField(
        max_length=255,
        unique=True,
        help_text=_('Template name')
    )

    template_type = models.CharField(
        max_length=20,
        choices=TYPE_CHOICES,
        help_text=_('Type of certificate')
    )

    description = models.TextField(
        blank=True,
        null=True,
        help_text=_('Template description')
    )

    template_file = models.FileField(
        upload_to='certificate_templates/',
        help_text=_('HTML or PDF template file')
    )

    skill = models.ForeignKey(
        'skills.Skill',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='certificate_templates',
        help_text=_('Associated skill (if applicable)')
    )

    program = models.ForeignKey(
        'programs.Program',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='certificate_templates',
        help_text=_('Associated program (if applicable)')
    )

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name


class Certificate(models.Model):
    """
    Issued certificates to students
    """

    STATUS_CHOICES = (
        ('issued', _('Issued')),
        ('revoked', _('Revoked')),
    )

    certificate_id = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        editable=False,
        help_text=_('Unique certificate ID')
    )

    student = models.ForeignKey(
        'students.Student',
        on_delete=models.CASCADE,
        related_name='certificates',
        help_text=_('Student receiving certificate')
    )

    template = models.ForeignKey(
        CertificateTemplate,
        on_delete=models.PROTECT,
        related_name='issued_certificates',
        help_text=_('Certificate template used')
    )

    skill = models.ForeignKey(
        'skills.Skill',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='student_certificates',
        help_text=_('Skill for which certificate is issued')
    )

    program = models.ForeignKey(
        'programs.Program',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='student_certificates',
        help_text=_('Program for which certificate is issued')
    )

    enrollment = models.ForeignKey(
        'students.StudentProgramEnrollment',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='certificates',
        help_text=_('Associated program enrollment')
    )

    skill_level = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        help_text=_('Achieved skill level')
    )

    final_score = models.IntegerField(
        blank=True,
        null=True,
        help_text=_('Final score/percentage')
    )

    issue_date = models.DateField(
        auto_now_add=True,
        help_text=_('Date certificate was issued')
    )

    expiry_date = models.DateField(
        blank=True,
        null=True,
        help_text=_('Certificate expiry date (if applicable)')
    )

    issued_by = models.ForeignKey(
        'accounts.CustomUser',
        on_delete=models.SET_NULL,
        null=True,
        related_name='issued_certificates',
        help_text=_('Issuing authority')
    )

    pdf_file = models.FileField(
        upload_to='certificates/%Y/%m/',
        blank=True,
        null=True,
        help_text=_('Generated PDF certificate')
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='issued'
    )

    is_verified = models.BooleanField(
        default=False,
        help_text=_('Certificate verification status')
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-issue_date']
        indexes = [
            models.Index(fields=['certificate_id']),
            models.Index(fields=['student', 'skill']),
            models.Index(fields=['status']),
        ]

    def __str__(self):
        return f"Certificate - {self.student} ({self.issue_date})"

    def get_certificate_name(self):
        """Generate descriptive certificate name"""
        if self.skill:
            return f"{self.skill.get_name_display()} Certificate"
        elif self.program:
            return f"{self.program.name} Completion Certificate"
        return "Achievement Certificate"

