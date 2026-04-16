from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.utils.translation import gettext_lazy as _

# Create your models here.

class CustomUser(AbstractUser):
    """
    Extended User model with additional profile fields for CAMDEEP.
    Supports multiple user roles: Admin, Trainer, School Admin, Student, Parent
    """

    ROLE_CHOICES = (
        ('admin', _('Administrator')),
        ('trainer', _('Trainer')),
        ('school_admin', _('School Administrator')),
        ('student', _('Student')),
        ('parent', _('Parent/Guardian')),
    )

    # Profile fields
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    profile_picture = models.ImageField(
        upload_to='profile_pictures/',
        blank=True,
        null=True,
        help_text=_('User profile picture')
    )
    bio = models.TextField(blank=True, null=True, help_text=_('Short biography'))
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='student')

    # Address fields
    street_address = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state_province = models.CharField(max_length=100, blank=True, null=True)
    postal_code = models.CharField(max_length=20, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)

    # Timestamps
    date_joined = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    is_verified = models.BooleanField(default=False, help_text=_('Email verified'))
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-date_joined']
        indexes = [
            models.Index(fields=['role']),
            models.Index(fields=['is_active']),
            models.Index(fields=['email']),
        ]

    def __str__(self):
        return f"{self.get_full_name()} ({self.get_role_display()})"

    def get_role_display(self):
        """Get human-readable role"""
        return dict(self.ROLE_CHOICES).get(self.role, self.role)

    def is_admin(self):
        return self.role == 'admin' or self.is_staff

    def is_trainer(self):
        return self.role == 'trainer'

    def is_school_admin(self):
        return self.role == 'school_admin'

    def is_student(self):
        return self.role == 'student'

    def is_parent(self):
        return self.role == 'parent'


class UserRole(models.Model):
    """
    Manages user roles and permissions
    """
    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='role_profile'
    )
    groups = models.ManyToManyField(
        Group,
        blank=True,
        help_text=_('Groups this user belongs to')
    )
    permissions = models.ManyToManyField(
        Permission,
        blank=True,
        help_text=_('Specific permissions for this user')
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('User Role')
        verbose_name_plural = _('User Roles')

    def __str__(self):
        return f"{self.user.username} - Roles Management"


class AuditLog(models.Model):
    """
    Track user activities for audit purposes
    """
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.SET_NULL,
        null=True,
        related_name='audit_logs'
    )
    action = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    ip_address = models.GenericIPAddressField(blank=True, null=True)
    user_agent = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']
        indexes = [
            models.Index(fields=['user', 'timestamp']),
            models.Index(fields=['action']),
        ]

    def __str__(self):
        return f"{self.user} - {self.action} ({self.timestamp})"

