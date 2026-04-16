from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Assessment(models.Model):
    """
    Assessments, worksheets, and activities for programs
    """

    TYPE_CHOICES = (
        ('worksheet', _('Worksheet')),
        ('quiz', _('Quiz')),
        ('project', _('Project')),
        ('activity', _('Activity')),
        ('assignment', _('Assignment')),
    )

    STATUS_CHOICES = (
        ('draft', _('Draft')),
        ('published', _('Published')),
        ('archived', _('Archived')),
    )

    program_project = models.ForeignKey(
        'programs.ProgramProject',
        on_delete=models.CASCADE,
        related_name='assessments',
        help_text=_('Associated program project')
    )

    title = models.CharField(
        max_length=255,
        help_text=_('Assessment title')
    )

    slug = models.SlugField()

    description = models.TextField(
        help_text=_('Assessment description and instructions')
    )

    assessment_type = models.CharField(
        max_length=20,
        choices=TYPE_CHOICES,
        default='worksheet'
    )

    content = models.TextField(
        help_text=_('Assessment content')
    )

    file = models.FileField(
        upload_to='assessments/',
        blank=True,
        null=True,
        help_text=_('PDF or document file')
    )

    total_marks = models.IntegerField(
        default=100,
        validators=[MinValueValidator(0)],
        help_text=_('Total marks/points for this assessment')
    )

    passing_percentage = models.IntegerField(
        default=50,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        help_text=_('Passing percentage (0-100)')
    )

    estimated_duration_minutes = models.IntegerField(
        default=60,
        help_text=_('Estimated time to complete (in minutes)')
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='draft'
    )

    order = models.IntegerField(default=0)

    created_by = models.ForeignKey(
        'accounts.CustomUser',
        on_delete=models.SET_NULL,
        null=True,
        related_name='created_assessments'
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('program_project', 'title')
        ordering = ['order']
        indexes = [
            models.Index(fields=['program_project', 'status']),
        ]

    def __str__(self):
        return f"{self.program_project.title} - {self.title}"


class StudentAssessmentResult(models.Model):
    """
    Student results for assessments
    """

    STATUS_CHOICES = (
        ('not_attempted', _('Not Attempted')),
        ('in_progress', _('In Progress')),
        ('submitted', _('Submitted')),
        ('graded', _('Graded')),
    )

    student = models.ForeignKey(
        'students.Student',
        on_delete=models.CASCADE,
        related_name='assessment_results',
        help_text=_('Student')
    )

    assessment = models.ForeignKey(
        Assessment,
        on_delete=models.CASCADE,
        related_name='student_results',
        help_text=_('Assessment')
    )

    submission_date = models.DateTimeField(
        blank=True,
        null=True,
        help_text=_('Date assessment was submitted')
    )

    grading_date = models.DateTimeField(
        blank=True,
        null=True,
        help_text=_('Date assessment was graded')
    )

    marks_obtained = models.IntegerField(
        blank=True,
        null=True,
        validators=[MinValueValidator(0)],
        help_text=_('Marks obtained')
    )

    percentage_score = models.IntegerField(
        blank=True,
        null=True,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        help_text=_('Score percentage')
    )

    is_passed = models.BooleanField(
        default=False,
        help_text=_('Whether student passed the assessment')
    )

    feedback = models.TextField(
        blank=True,
        null=True,
        help_text=_('Feedback from grader')
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='not_attempted'
    )

    graded_by = models.ForeignKey(
        'accounts.CustomUser',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='graded_assessments'
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('student', 'assessment')
        ordering = ['-submission_date']
        indexes = [
            models.Index(fields=['student', 'status']),
            models.Index(fields=['assessment', 'is_passed']),
        ]

    def __str__(self):
        return f"{self.student} - {self.assessment.title}"

