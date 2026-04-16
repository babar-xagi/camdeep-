from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class School(models.Model):
    """
    Partner schools collaborating with CAMDEEP
    """

    STATUS_CHOICES = (
        ('pending', _('Pending')),
        ('active', _('Active')),
        ('inactive', _('Inactive')),
        ('archived', _('Archived')),
    )

    name = models.CharField(
        max_length=255,
        unique=True,
        help_text=_('Official school name')
    )

    slug = models.SlugField(unique=True)

    description = models.TextField(
        blank=True,
        null=True,
        help_text=_('School description')
    )

    # Contact Information
    principal_name = models.CharField(
        max_length=255,
        help_text=_('Principal or head of school name')
    )
    principal_email = models.EmailField()
    principal_phone = models.CharField(max_length=20)

    # Administrative Contact
    admin_contact_name = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text=_('CAMDEEP administrator contact name')
    )
    admin_email = models.EmailField(
        blank=True,
        null=True,
        help_text=_('School administrator email')
    )
    admin_phone = models.CharField(
        max_length=20,
        blank=True,
        null=True
    )

    # Address
    street_address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state_province = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100)

    # School Information
    logo = models.ImageField(upload_to='schools/', blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    established_year = models.IntegerField(blank=True, null=True)

    total_students = models.IntegerField(
        default=0,
        help_text=_('Total number of students in school')
    )

    target_grades = models.CharField(
        max_length=255,
        default='6,7,8,9,10',
        help_text=_('Target grades (comma-separated)')
    )

    # Partnership Status
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'
    )

    mou_signed = models.BooleanField(
        default=False,
        help_text=_('MOU signed and completed')
    )
    mou_date = models.DateField(
        blank=True,
        null=True,
        help_text=_('Date MOU was signed')
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['slug']),
            models.Index(fields=['status']),
        ]

    def __str__(self):
        return self.name

    def get_target_grades(self):
        """Parse target grades as a list"""
        return [g.strip() for g in self.target_grades.split(',')]


class SchoolProgram(models.Model):
    """
    Programs implemented in a school
    """

    STATUS_CHOICES = (
        ('pending', _('Pending')),
        ('active', _('Active')),
        ('completed', _('Completed')),
        ('paused', _('Paused')),
    )

    school = models.ForeignKey(
        School,
        on_delete=models.CASCADE,
        related_name='school_programs',
        help_text=_('Partner school')
    )

    program = models.ForeignKey(
        'programs.Program',
        on_delete=models.CASCADE,
        related_name='school_implementations',
        help_text=_('CAMDEEP program')
    )

    grade_level = models.CharField(
        max_length=2,
        help_text=_('Grade level implementing this program')
    )

    start_date = models.DateField(
        help_text=_('Program start date in school')
    )

    end_date = models.DateField(
        blank=True,
        null=True,
        help_text=_('Program end date')
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'
    )

    number_of_students = models.IntegerField(
        default=0,
        help_text=_('Number of students enrolled')
    )

    notes = models.TextField(
        blank=True,
        null=True,
        help_text=_('Implementation notes and observations')
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('school', 'program', 'grade_level')
        ordering = ['-start_date']

    def __str__(self):
        return f"{self.school.name} - {self.program.name} (Grade {self.grade_level})"

