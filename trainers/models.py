from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Trainer(models.Model):
    """
    CAMDEEP Trainers managing programs at schools
    """

    STATUS_CHOICES = (
        ('active', _('Active')),
        ('inactive', _('Inactive')),
        ('on_leave', _('On Leave')),
        ('archived', _('Archived')),
    )

    user = models.OneToOneField(
        'accounts.CustomUser',
        on_delete=models.CASCADE,
        related_name='trainer_profile',
        help_text=_('Associated user account')
    )

    employee_id = models.CharField(
        max_length=50,
        unique=True,
        help_text=_('Unique employee ID')
    )

    qualifications = models.TextField(
        blank=True,
        null=True,
        help_text=_('Qualifications and certifications (one per line)')
    )

    experience_years = models.IntegerField(
        default=0,
        help_text=_('Years of experience in education')
    )

    bio = models.TextField(
        blank=True,
        null=True,
        help_text=_('Professional biography')
    )

    skills_expertise = models.ManyToManyField(
        'skills.Skill',
        blank=True,
        related_name='expert_trainers',
        help_text=_('Skills this trainer specializes in')
    )

    assigned_schools = models.ManyToManyField(
        'schools.School',
        blank=True,
        related_name='trainers',
        through='TrainerAssignment',
        help_text=_('Schools this trainer is assigned to')
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='active'
    )

    joining_date = models.DateField(
        auto_now_add=True,
        help_text=_('Date trainer joined CAMDEEP')
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['employee_id']),
            models.Index(fields=['status']),
        ]

    def __str__(self):
        return f"{self.user.get_full_name()} ({self.employee_id})"

    def get_qualifications(self):
        """Parse qualifications as a list"""
        if self.qualifications:
            return [q.strip() for q in self.qualifications.split('\n') if q.strip()]
        return []


class TrainerAssignment(models.Model):
    """
    Assignment of trainers to schools and programs
    """

    STATUS_CHOICES = (
        ('assigned', _('Assigned')),
        ('active', _('Active')),
        ('completed', _('Completed')),
        ('removed', _('Removed')),
    )

    trainer = models.ForeignKey(
        Trainer,
        on_delete=models.CASCADE,
        related_name='assignments',
        help_text=_('Assigned trainer')
    )

    school = models.ForeignKey(
        'schools.School',
        on_delete=models.CASCADE,
        related_name='trainer_assignments',
        help_text=_('School assignment')
    )

    program = models.ForeignKey(
        'programs.Program',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='trainer_assignments',
        help_text=_('Program (optional, if school-wide leave blank)')
    )

    start_date = models.DateField(
        help_text=_('Assignment start date')
    )

    end_date = models.DateField(
        blank=True,
        null=True,
        help_text=_('Assignment end date')
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='assigned'
    )

    visit_frequency = models.CharField(
        max_length=50,
        default='Twice per month',
        help_text=_('Frequency of trainer visits')
    )

    notes = models.TextField(
        blank=True,
        null=True,
        help_text=_('Assignment notes')
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('trainer', 'school', 'program')
        ordering = ['-start_date']
        indexes = [
            models.Index(fields=['trainer', 'status']),
            models.Index(fields=['school', 'status']),
        ]

    def __str__(self):
        return f"{self.trainer.user.get_full_name()} @ {self.school.name}"


class TrainerFeedback(models.Model):
    """
    Feedback and observations from trainers
    """

    trainer = models.ForeignKey(
        Trainer,
        on_delete=models.CASCADE,
        related_name='feedbacks',
        help_text=_('Feedback provider')
    )

    school = models.ForeignKey(
        'schools.School',
        on_delete=models.CASCADE,
        related_name='trainer_feedbacks',
        help_text=_('School subject of feedback')
    )

    program = models.ForeignKey(
        'programs.Program',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='trainer_feedbacks',
        help_text=_('Program feedback is about')
    )

    visit_date = models.DateField(
        help_text=_('Date of trainer visit')
    )

    observations = models.TextField(
        help_text=_('Observations and feedback')
    )

    rating = models.IntegerField(
        choices=[(i, i) for i in range(1, 6)],
        blank=True,
        null=True,
        help_text=_('Overall rating (1-5)')
    )

    recommendations = models.TextField(
        blank=True,
        null=True,
        help_text=_('Recommendations for improvement')
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-visit_date']
        indexes = [
            models.Index(fields=['trainer', 'visit_date']),
            models.Index(fields=['school', 'visit_date']),
        ]

    def __str__(self):
        return f"Feedback: {self.school.name} - {self.visit_date}"

