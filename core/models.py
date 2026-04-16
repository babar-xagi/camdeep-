from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class SiteSetting(models.Model):
    """
    Global site configuration and branding settings
    """
    site_name = models.CharField(
        max_length=255,
        default='CAMDEEP',
        help_text=_('Official name of the platform')
    )
    tagline = models.CharField(
        max_length=500,
        default='A Real-World Educational Framework with Global Competencies',
        help_text=_('Official tagline')
    )
    description = models.TextField(
        help_text=_('Site description for SEO')
    )

    # Branding
    logo = models.ImageField(upload_to='branding/', blank=True, null=True)
    favicon = models.ImageField(upload_to='branding/', blank=True, null=True)

    # Contact Information
    email = models.EmailField(help_text=_('Primary contact email'))
    phone_primary = models.CharField(max_length=20, help_text=_('Primary phone'))
    phone_secondary = models.CharField(max_length=20, blank=True, null=True)

    # Address
    street_address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100)

    # Social Media
    facebook_url = models.URLField(blank=True, null=True)
    twitter_url = models.URLField(blank=True, null=True)
    linkedin_url = models.URLField(blank=True, null=True)
    youtube_url = models.URLField(blank=True, null=True)
    instagram_url = models.URLField(blank=True, null=True)

    # Color Scheme
    primary_color = models.CharField(max_length=7, default='#2563EB', help_text=_('Primary color (Blue)'))
    secondary_color = models.CharField(max_length=7, default='#FFFFFF', help_text=_('Secondary color (White)'))
    accent_color = models.CharField(max_length=7, default='#D4AF37', help_text=_('Accent color (Gold)'))

    # Settings
    maintenance_mode = models.BooleanField(default=False)
    allow_registration = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('Site Setting')
        verbose_name_plural = _('Site Settings')

    def __str__(self):
        return self.site_name

    def save(self, *args, **kwargs):
        # Ensure only one instance exists
        if self.pk is None and SiteSetting.objects.exists():
            self.pk = SiteSetting.objects.first().pk
        super().save(*args, **kwargs)


class HomePage(models.Model):
    """
    Home page content and hero section
    """
    title = models.CharField(max_length=255, default='Welcome to CAMDEEP')
    hero_subtitle = models.CharField(
        max_length=500,
        default='Empowering Minds. Transforming Futures.'
    )
    hero_image = models.ImageField(upload_to='home/', blank=True, null=True)
    hero_description = models.TextField(help_text=_('Hero section description'))

    cta_button_text = models.CharField(max_length=100, default='Get Started')
    cta_button_url = models.CharField(max_length=255, default='/programs')

    featured_section_title = models.CharField(max_length=255, default='Why Choose CAMDEEP?')
    featured_section_description = models.TextField(blank=True, null=True)

    is_published = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('Home Page')
        verbose_name_plural = _('Home Pages')

    def __str__(self):
        return self.title


class Feature(models.Model):
    """
    Featured items on homepage or marketing pages
    """
    title = models.CharField(max_length=255)
    description = models.TextField()
    icon = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text=_('Icon class or emoji')
    )
    image = models.ImageField(upload_to='features/', blank=True, null=True)
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title


class FAQ(models.Model):
    """
    Frequently Asked Questions
    """
    question = models.CharField(max_length=500)
    answer = models.TextField()
    category = models.CharField(max_length=100, blank=True, null=True)
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order']
        verbose_name = _('FAQ')
        verbose_name_plural = _('FAQs')

    def __str__(self):
        return self.question[:50]

