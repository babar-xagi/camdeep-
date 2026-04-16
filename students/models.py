from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Student(models.Model):
    """
    Student enrollment and profile in CAMDEEP
    """

    STATUS_CHOICES = (
        ('active', _('Active')),
        ('inactive', _('Inactive')),
        ('graduated', _('Graduated')),
        ('dropped', _('Dropped')),
    )

    user = models.OneToOneField(
        'accounts.CustomUser',
        on_delete=models.CASCADE,
        related_name='student_profile',
        help_text=_('Associated user account')
    )

    roll_number = models.CharField(
        max_length=50,
        unique=True,
        help_text=_('Unique roll number')
    )

    school = models.ForeignKey(
        'schools.School',
        on_delete=models.CASCADE,
        related_name='students',
        help_text=_('Enrolled school')
    )

    grade = models.CharField(
        max_length=2,
        choices=[(str(i), f'Grade {i}') for i in range(6, 11)],
        help_text=_('Current grade level')
    )

    date_of_birth = models.DateField(
        blank=True,
        null=True,
        help_text=_('Student date of birth')
    )

    guardian_name = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text=_('Parent/Guardian full name')
    )

    guardian_email = models.EmailField(
        blank=True,
        null=True,
        help_text=_('Parent/Guardian email')
    )

    guardian_phone = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        help_text=_('Parent/Guardian phone')
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='active'
    )

    enrollment_date = models.DateField(
        auto_now_add=True,
        help_text=_('Enrollment date in CAMDEEP')
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-enrollment_date']
        indexes = [
            models.Index(fields=['roll_number']),
            models.Index(fields=['school', 'grade']),
            models.Index(fields=['status']),
        ]

    def __str__(self):
        return f"{self.user.get_full_name()} ({self.roll_number})"

    def get_enrolled_programs(self):
        """Get all programs this student is enrolled in"""
        return self.program_enrollments.filter(status='active')


class StudentProgramEnrollment(models.Model):
    """
    Enrollment of students in specific programs
    """

    STATUS_CHOICES = (
        ('pending', _('Pending')),
        ('active', _('Active')),
        ('completed', _('Completed')),
        ('dropped', _('Dropped')),
    )

    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name='program_enrollments',
        help_text=_('Enrolled student')
    )

    program = models.ForeignKey(
        'programs.Program',
        on_delete=models.CASCADE,
        related_name='student_enrollments',
        help_text=_('Program enrolled in')
    )

    school_program = models.ForeignKey(
        'schools.SchoolProgram',
        on_delete=models.CASCADE,
        related_name='student_enrollments',
        help_text=_('School-specific program implementation')
    )

    enrollment_date = models.DateField(
        auto_now_add=True,
        help_text=_('Enrollment date')
    )

    completion_date = models.DateField(
        blank=True,
        null=True,
        help_text=_('Program completion date')
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'
    )

    progress_percentage = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        help_text=_('Progress percentage (0-100)')
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('student', 'program', 'school_program')
        ordering = ['-enrollment_date']
        indexes = [
            models.Index(fields=['student', 'status']),
            models.Index(fields=['program', 'status']),
        ]

    def __str__(self):
        return f"{self.student.user.get_full_name()} - {self.program.name}"


class StudentSkillProgress(models.Model):
    """
    Track student progress in individual skills
    """

    enrollment = models.ForeignKey(
        StudentProgramEnrollment,
        on_delete=models.CASCADE,
        related_name='skill_progress',
        help_text=_('Parent program enrollment')
    )

    skill = models.ForeignKey(
        'skills.Skill',
        on_delete=models.CASCADE,
        related_name='student_progress',
        help_text=_('Associated skill')
    )

    current_level = models.CharField(
        max_length=20,
        choices=[
            ('beginner', _('Beginner')),
            ('intermediate', _('Intermediate')),
            ('advanced', _('Advanced')),
            ('expert', _('Expert')),
        ],
        default='beginner',
        help_text=_('Current proficiency level')
    )

    score = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        help_text=_('Skill score (0-100)')
    )

    assessments_completed = models.IntegerField(
        default=0,
        help_text=_('Number of assessments completed')
    )

    last_assessment_date = models.DateField(
        blank=True,
        null=True,
        help_text=_('Date of last assessment')
    )

    notes = models.TextField(
        blank=True,
        null=True,
        help_text=_('Trainer observations and notes')
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('enrollment', 'skill')
        ordering = ['skill']
        indexes = [
            models.Index(fields=['enrollment', 'skill']),
        ]

    def __str__(self):
        return f"{self.enrollment.student.user.get_full_name()} - {self.skill.get_name_display()}"

