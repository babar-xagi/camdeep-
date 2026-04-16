from django.db import models
from django.utils.translation import gettext_lazy as _
from taggit.managers import TaggableManager

# Create your models here.

class Skill(models.Model):
    """
    The 7 core skills of CAMDEEP educational framework
    """

    SKILL_CHOICES = (
        ('creativity', _('Creativity')),
        ('analytical', _('Analytical Thinking')),
        ('management', _('Management Skills')),
        ('digital', _('Digital Skills')),
        ('entrepreneurship', _('Entrepreneurship')),
        ('ethics', _('Ethics')),
        ('problem_solving', _('Problem Solving')),
    )

    name = models.CharField(
        max_length=255,
        unique=True,
        choices=SKILL_CHOICES,
        help_text=_('Name of the core skill')
    )

    slug = models.SlugField(unique=True)

    description = models.TextField(
        help_text=_('Detailed description of the skill')
    )

    short_description = models.CharField(
        max_length=500,
        help_text=_('Brief description for listings')
    )

    icon = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text=_('Icon class or emoji representation')
    )

    image = models.ImageField(
        upload_to='skills/',
        blank=True,
        null=True,
        help_text=_('Skill banner image')
    )

    learning_outcomes = models.TextField(
        blank=True,
        null=True,
        help_text=_('Key learning outcomes (one per line)')
    )

    order = models.IntegerField(
        default=0,
        help_text=_('Display order among skills')
    )

    is_active = models.BooleanField(default=True)

    tags = TaggableManager(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', 'name']
        indexes = [
            models.Index(fields=['slug']),
            models.Index(fields=['is_active']),
        ]

    def __str__(self):
        return self.get_name_display()

    def get_learning_outcomes(self):
        """Parse learning outcomes as a list"""
        if self.learning_outcomes:
            return [line.strip() for line in self.learning_outcomes.split('\n') if line.strip()]
        return []


class SkillLevel(models.Model):
    """
    Proficiency levels for each skill
    """
    LEVEL_CHOICES = (
        ('beginner', _('Beginner')),
        ('intermediate', _('Intermediate')),
        ('advanced', _('Advanced')),
        ('expert', _('Expert')),
    )

    skill = models.ForeignKey(
        Skill,
        on_delete=models.CASCADE,
        related_name='levels',
        help_text=_('Associated skill')
    )

    level = models.CharField(
        max_length=20,
        choices=LEVEL_CHOICES,
        help_text=_('Proficiency level')
    )

    description = models.TextField(
        help_text=_('Description of competency at this level')
    )

    min_score = models.IntegerField(
        default=0,
        help_text=_('Minimum score to achieve this level')
    )

    max_score = models.IntegerField(
        default=100,
        help_text=_('Maximum score for this level')
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('skill', 'level')
        ordering = ['skill', 'min_score']

    def __str__(self):
        return f"{self.skill.get_name_display()} - {self.get_level_display()}"


class SkillArea(models.Model):
    """
    Sub-areas or domains within each skill
    """
    skill = models.ForeignKey(
        Skill,
        on_delete=models.CASCADE,
        related_name='areas',
        help_text=_('Parent skill')
    )

    name = models.CharField(
        max_length=255,
        help_text=_('Name of the skill area/domain')
    )

    description = models.TextField(
        blank=True,
        null=True,
        help_text=_('Description of this skill area')
    )

    order = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('skill', 'name')
        ordering = ['skill', 'order']

    def __str__(self):
        return f"{self.skill.get_name_display()} - {self.name}"

