from django.contrib import admin
from .models import CertificateTemplate, Certificate

@admin.register(CertificateTemplate)
class CertificateTemplateAdmin(admin.ModelAdmin):
    list_display = ('name', 'template_type', 'skill', 'program', 'is_active')
    list_filter = ('template_type', 'is_active')
    search_fields = ('name', 'description')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Template Information', {
            'fields': ('name', 'template_type', 'description')
        }),
        ('Association', {
            'fields': ('skill', 'program')
        }),
        ('File', {
            'fields': ('template_file',)
        }),
        ('Status', {
            'fields': ('is_active',)
        }),
    )


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ('certificate_id', 'student', 'skill', 'issue_date', 'status', 'is_verified')
    list_filter = ('status', 'is_verified', 'issue_date', 'skill')
    search_fields = ('certificate_id', 'student__user__username', 'student__user__email')
    readonly_fields = ('certificate_id', 'created_at', 'updated_at', 'issue_date')
    fieldsets = (
        ('Certificate Information', {
            'fields': ('certificate_id', 'student', 'template')
        }),
        ('Achievement', {
            'fields': ('skill', 'program', 'enrollment', 'skill_level', 'final_score')
        }),
        ('Issue Details', {
            'fields': ('issue_date', 'expiry_date', 'issued_by')
        }),
        ('File', {
            'fields': ('pdf_file',)
        }),
        ('Status', {
            'fields': ('status', 'is_verified')
        }),
    )
