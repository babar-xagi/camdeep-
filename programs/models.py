from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator, MaxValueValidator
from skills.models import Skill

# Create your models here.

class Program(models.Model):
    """
    CAMDEEP Educational Programs
    Each program spans 1 month and consists of 2 projects per skill
    """

    GRADE_CHOICES = (
        ('6', _('Grade 6')),
        ('7', _('Grade 7')),
        ('8', _('Grade 8')),
        ('9', _('Grade 9')),
        ('10', _('Grade 10')),
    )

    STATUS_CHOICES = (
        ('draft', _('Draft')),
        ('published', _('Published')),
        ('archived', _('Archived')),
    )

    name = models.CharField(
        max_length=255,
        help_text=_('Program name')
    )

    slug = models.SlugField(unique=True)

    description = models.TextField(
        help_text=_('Detailed program description')
    )

    skill = models.ForeignKey(
        Skill,
        on_delete=models.CASCADE,
        related_name='programs',
        help_text=_('Associated core skill')
    )

    target_grade = models.CharField(
        max_length=2,
        choices=GRADE_CHOICES,
        help_text=_('Target grade level')
    )

    duration_days = models.IntegerField(
        default=30,
        validators=[MinValueValidator(1), MaxValueValidator(365)],
        help_text=_('Program duration in days')
    )

    learning_outcomes = models.TextField(
        blank=True,
        null=True,
        help_text=_('Key learning outcomes (one per line)')
    )

    thumbnail = models.ImageField(
        upload_to='programs/',
        blank=True,
        null=True
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
        related_name='created_programs'
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['slug']),
            models.Index(fields=['status']),
            models.Index(fields=['skill']),
        ]

    def __str__(self):
        return f"{self.name} (Grade {self.target_grade})"

    def get_learning_outcomes(self):
        """Parse learning outcomes as a list"""
        if self.learning_outcomes:
            return [line.strip() for line in self.learning_outcomes.split('\n') if line.strip()]
        return []


class ProgramProject(models.Model):
    """
    Projects within a program
    Each skill program has 2 projects of 15 days each
    """

    STATUS_CHOICES = (
        ('draft', _('Draft')),
        ('active', _('Active')),
        ('archived', _('Archived')),
    )

    program = models.ForeignKey(
        Program,
        on_delete=models.CASCADE,
        related_name='projects',
        help_text=_('Parent program')
    )

    title = models.CharField(
        max_length=255,
        help_text=_('Project title')
    )

    slug = models.SlugField()

    description = models.TextField(
        help_text=_('Detailed project description')
    )

    project_number = models.IntegerField(
        help_text=_('Project number (1 or 2) within the program'),
        validators=[MinValueValidator(1), MaxValueValidator(2)]
    )

    duration_days = models.IntegerField(
        default=15,
        help_text=_('Project duration in days')
    )

    objectives = models.TextField(
        blank=True,
        null=True,
        help_text=_('Project objectives (one per line)')
    )

    deliverables = models.TextField(
        blank=True,
        null=True,
        help_text=_('Expected deliverables (one per line)')
    )

    resources = models.TextField(
        blank=True,
        null=True,
        help_text=_('Required resources and materials')
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='draft'
    )

    order = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('program', 'project_number')
        ordering = ['program', 'order']
        indexes = [
            models.Index(fields=['program', 'status']),
        ]

    def __str__(self):
        return f"{self.program.name} - Project {self.project_number}: {self.title}"

    def get_objectives(self):
        """Parse objectives as a list"""
        if self.objectives:
            return [line.strip() for line in self.objectives.split('\n') if line.strip()]
        return []

    def get_deliverables(self):
        """Parse deliverables as a list"""
        if self.deliverables:
            return [line.strip() for line in self.deliverables.split('\n') if line.strip()]
        return []


class ProgramModule(models.Model):
    """
    Modules or lessons within a project
    """
    project = models.ForeignKey(
        ProgramProject,
        on_delete=models.CASCADE,
        related_name='modules',
        help_text=_('Parent project')
    )

    title = models.CharField(
        max_length=255,
        help_text=_('Module title')
    )

    content = models.TextField(
        help_text=_('Module content')
    )

    order = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['project', 'order']

    def __str__(self):
        return f"{self.project.title} - Module {self.order}: {self.title}"

