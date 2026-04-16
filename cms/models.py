from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify

# Create your models here.

class Page(models.Model):
    """
    Dynamic CMS pages
    """

    STATUS_CHOICES = (
        ('draft', _('Draft')),
        ('published', _('Published')),
        ('archived', _('Archived')),
    )

    title = models.CharField(
        max_length=255,
        unique=True,
        help_text=_('Page title')
    )

    slug = models.SlugField(
        unique=True,
        help_text=_('URL slug')
    )

    content = models.TextField(
        help_text=_('Page content (supports HTML)')
    )

    description = models.CharField(
        max_length=500,
        blank=True,
        null=True,
        help_text=_('SEO meta description')
    )

    keywords = models.CharField(
        max_length=500,
        blank=True,
        null=True,
        help_text=_('SEO keywords (comma-separated)')
    )

    featured_image = models.ImageField(
        upload_to='cms/pages/',
        blank=True,
        null=True,
        help_text=_('Featured image')
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='draft'
    )

    author = models.ForeignKey(
        'accounts.CustomUser',
        on_delete=models.SET_NULL,
        null=True,
        related_name='cms_pages'
    )

    published_date = models.DateTimeField(
        blank=True,
        null=True,
        help_text=_('Publication date')
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
        return self.title


class BlogPost(models.Model):
    """
    Blog posts for news, updates, and articles
    """

    STATUS_CHOICES = (
        ('draft', _('Draft')),
        ('published', _('Published')),
        ('archived', _('Archived')),
    )

    title = models.CharField(
        max_length=255,
        help_text=_('Blog post title')
    )

    slug = models.SlugField(
        unique=True,
        help_text=_('URL slug')
    )

    excerpt = models.TextField(
        max_length=500,
        help_text=_('Short excerpt for listing')
    )

    content = models.TextField(
        help_text=_('Full blog content')
    )

    featured_image = models.ImageField(
        upload_to='cms/blog/',
        help_text=_('Featured image')
    )

    category = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text=_('Blog category')
    )

    tags = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text=_('Tags (comma-separated)')
    )

    author = models.ForeignKey(
        'accounts.CustomUser',
        on_delete=models.SET_NULL,
        null=True,
        related_name='blog_posts'
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='draft'
    )

    read_time_minutes = models.IntegerField(
        default=5,
        help_text=_('Estimated read time in minutes')
    )

    view_count = models.IntegerField(
        default=0,
        help_text=_('Number of views')
    )

    published_date = models.DateTimeField(
        blank=True,
        null=True,
        help_text=_('Publication date')
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-published_date']
        indexes = [
            models.Index(fields=['slug']),
            models.Index(fields=['status']),
            models.Index(fields=['published_date']),
        ]

    def __str__(self):
        return self.title

    def increment_views(self):
        """Increment view count"""
        self.view_count += 1
        self.save(update_fields=['view_count'])


class Testimonial(models.Model):
    """
    Student and partner testimonials
    """

    STATUS_CHOICES = (
        ('pending', _('Pending Approval')),
        ('approved', _('Approved')),
        ('archived', _('Archived')),
    )

    author_name = models.CharField(
        max_length=255,
        help_text=_('Testimonial author name')
    )

    author_title = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text=_('Author title/role')
    )

    author_image = models.ImageField(
        upload_to='cms/testimonials/',
        blank=True,
        null=True,
        help_text=_('Author image/avatar')
    )

    content = models.TextField(
        help_text=_('Testimonial content')
    )

    rating = models.IntegerField(
        choices=[(i, i) for i in range(1, 6)],
        default=5,
        help_text=_('Rating (1-5 stars)')
    )

    related_skill = models.ForeignKey(
        'skills.Skill',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='testimonials',
        help_text=_('Related skill')
    )

    related_program = models.ForeignKey(
        'programs.Program',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='testimonials',
        help_text=_('Related program')
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'
    )

    featured = models.BooleanField(
        default=False,
        help_text=_('Feature on homepage')
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['status']),
            models.Index(fields=['featured']),
        ]

    def __str__(self):
        return f"Testimonial by {self.author_name}"


class ContactMessage(models.Model):
    """
    Contact form messages
    """

    STATUS_CHOICES = (
        ('new', _('New')),
        ('replied', _('Replied')),
        ('resolved', _('Resolved')),
        ('spam', _('Spam')),
    )

    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    subject = models.CharField(max_length=255)
    message = models.TextField()

    message_type = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        help_text=_('Type of inquiry')
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='new'
    )

    replied_message = models.TextField(
        blank=True,
        null=True,
        help_text=_('Reply message')
    )

    replied_by = models.ForeignKey(
        'accounts.CustomUser',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='replied_messages'
    )

    replied_date = models.DateTimeField(
        blank=True,
        null=True,
        help_text=_('Date message was replied to')
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['status']),
            models.Index(fields=['created_at']),
        ]

    def __str__(self):
        return f"Contact: {self.subject} from {self.name}"

