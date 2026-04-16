from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class ResourceCategory(models.Model):
    """
    Categories for organizing resources
    """
    name = models.CharField(
        max_length=255,
        unique=True,
        help_text=_('Category name')
    )

    slug = models.SlugField(unique=True)

    description = models.TextField(
        blank=True,
        null=True,
        help_text=_('Category description')
    )

    icon = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text=_('Icon class or emoji')
    )

    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name_plural = _('Resource Categories')

    def __str__(self):
        return self.name


class Resource(models.Model):
    """
    Learning resources: books, videos, downloads, etc.
    """

    TYPE_CHOICES = (
        ('book', _('Book')),
        ('video', _('Video')),
        ('pdf', _('PDF Document')),
        ('article', _('Article')),
        ('worksheet', _('Worksheet')),
        ('template', _('Template')),
        ('tool', _('Tool')),
        ('other', _('Other')),
    )

    STATUS_CHOICES = (
        ('draft', _('Draft')),
        ('published', _('Published')),
        ('archived', _('Archived')),
    )

    title = models.CharField(
        max_length=255,
        help_text=_('Resource title')
    )

    slug = models.SlugField(unique=True)

    description = models.TextField(
        help_text=_('Resource description')
    )

    category = models.ForeignKey(
        ResourceCategory,
        on_delete=models.SET_NULL,
        null=True,
        related_name='resources',
        help_text=_('Resource category')
    )

    resource_type = models.CharField(
        max_length=20,
        choices=TYPE_CHOICES,
        help_text=_('Type of resource')
    )

    related_skills = models.ManyToManyField(
        'skills.Skill',
        blank=True,
        related_name='resources',
        help_text=_('Related skills')
    )

    related_programs = models.ManyToManyField(
        'programs.Program',
        blank=True,
        related_name='resources',
        help_text=_('Related programs')
    )

    thumbnail = models.ImageField(
        upload_to='resources/thumbnails/',
        blank=True,
        null=True,
        help_text=_('Resource thumbnail image')
    )

    file = models.FileField(
        upload_to='resources/files/',
        blank=True,
        null=True,
        help_text=_('Resource file for download')
    )

    external_url = models.URLField(
        blank=True,
        null=True,
        help_text=_('External link (for videos, articles, etc.)')
    )

    author = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text=_('Resource author')
    )

    publication_date = models.DateField(
        blank=True,
        null=True,
        help_text=_('Publication date')
    )

    download_count = models.IntegerField(
        default=0,
        help_text=_('Number of downloads')
    )

    view_count = models.IntegerField(
        default=0,
        help_text=_('Number of views')
    )

    is_featured = models.BooleanField(
        default=False,
        help_text=_('Feature this resource on homepage')
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='draft'
    )

    created_by = models.ForeignKey(
        'accounts.CustomUser',
        on_delete=models.SET_NULL,
        null=True,
        related_name='created_resources'
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['slug']),
            models.Index(fields=['status']),
            models.Index(fields=['is_featured']),
        ]

    def __str__(self):
        return self.title

    def increment_views(self):
        """Increment view count"""
        self.view_count += 1
        self.save(update_fields=['view_count'])

    def increment_downloads(self):
        """Increment download count"""
        self.download_count += 1
        self.save(update_fields=['download_count'])

