from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid

# Create your models here.

class MOU(models.Model):
    """
    Memorandum of Understanding with partner schools
    """

    STATUS_CHOICES = (
        ('draft', _('Draft')),
        ('pending', _('Pending Signature')),
        ('signed', _('Signed')),
        ('active', _('Active')),
        ('suspended', _('Suspended')),
        ('terminated', _('Terminated')),
    )

    mou_id = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        editable=False,
        help_text=_('Unique MOU identifier')
    )

    school = models.OneToOneField(
        'schools.School',
        on_delete=models.CASCADE,
        related_name='mou',
        help_text=_('Partner school')
    )

    title = models.CharField(
        max_length=255,
        default='Memorandum of Understanding with CAMDEEP',
        help_text=_('MOU title')
    )

    description = models.TextField(
        blank=True,
        null=True,
        help_text=_('MOU description and objectives')
    )

    start_date = models.DateField(
        help_text=_('Partnership start date')
    )

    end_date = models.DateField(
        blank=True,
        null=True,
        help_text=_('Partnership end date (optional)')
    )

    duration_months = models.IntegerField(
        default=12,
        help_text=_('MOU duration in months')
    )

    terms_and_conditions = models.TextField(
        blank=True,
        null=True,
        help_text=_('Terms and conditions of partnership')
    )

    document_file = models.FileField(
        upload_to='mou/%Y/%m/',
        blank=True,
        null=True,
        help_text=_('MOU document PDF')
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='draft'
    )

    signed_by_school_date = models.DateField(
        blank=True,
        null=True,
        help_text=_('Date signed by school')
    )

    signed_by_camdeep_date = models.DateField(
        blank=True,
        null=True,
        help_text=_('Date signed by CAMDEEP')
    )

    school_signatory_name = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text=_('Name of school signatory')
    )

    school_signatory_title = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text=_('Title of school signatory')
    )

    camdeep_signatory_name = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text=_('Name of CAMDEEP signatory')
    )

    camdeep_signatory_title = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text=_('Title of CAMDEEP signatory')
    )

    created_by = models.ForeignKey(
        'accounts.CustomUser',
        on_delete=models.SET_NULL,
        null=True,
        related_name='created_mous'
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = _('MOU')
        verbose_name_plural = _('MOUs')

    def __str__(self):
        return f"MOU - {self.school.name}"

    def is_active(self):
        """Check if MOU is currently active"""
        from django.utils import timezone
        today = timezone.now().date()
        return (self.status == 'active' and
                self.start_date <= today and
                (self.end_date is None or self.end_date >= today))


class Partnership(models.Model):
    """
    General partnership records with organizations
    """

    TYPE_CHOICES = (
        ('school', _('School')),
        ('ngo', _('NGO')),
        ('corporate', _('Corporate')),
        ('government', _('Government')),
        ('other', _('Other')),
    )

    STATUS_CHOICES = (
        ('prospective', _('Prospective')),
        ('negotiating', _('Negotiating')),
        ('active', _('Active')),
        ('concluded', _('Concluded')),
    )

    name = models.CharField(
        max_length=255,
        unique=True,
        help_text=_('Organization name')
    )

    partnership_type = models.CharField(
        max_length=20,
        choices=TYPE_CHOICES,
        help_text=_('Type of partner organization')
    )

    description = models.TextField(
        blank=True,
        null=True,
        help_text=_('Partnership description')
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='prospective'
    )

    contact_person = models.CharField(
        max_length=255,
        help_text=_('Primary contact person')
    )

    contact_email = models.EmailField()
    contact_phone = models.CharField(max_length=20)

    website = models.URLField(blank=True, null=True)

    start_date = models.DateField(
        blank=True,
        null=True,
        help_text=_('Partnership start date')
    )

    end_date = models.DateField(
        blank=True,
        null=True,
        help_text=_('Partnership end date')
    )

    notes = models.TextField(
        blank=True,
        null=True,
        help_text=_('Additional notes')
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name

