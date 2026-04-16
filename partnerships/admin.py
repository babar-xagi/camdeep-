from django.contrib import admin
from .models import MOU, Partnership

@admin.register(MOU)
class MOUAdmin(admin.ModelAdmin):
    list_display = ('mou_id', 'school', 'status', 'start_date', 'signed_by_school_date')
    list_filter = ('status', 'start_date')
    search_fields = ('mou_id', 'school__name')
    readonly_fields = ('mou_id', 'created_at', 'updated_at')
    fieldsets = (
        ('MOU Information', {
            'fields': ('mou_id', 'school', 'title', 'description')
        }),
        ('Period', {
            'fields': ('start_date', 'end_date', 'duration_months')
        }),
        ('Terms', {
            'fields': ('terms_and_conditions', 'document_file')
        }),
        ('School Signature', {
            'fields': ('signed_by_school_date', 'school_signatory_name', 'school_signatory_title')
        }),
        ('CAMDEEP Signature', {
            'fields': ('signed_by_camdeep_date', 'camdeep_signatory_name', 'camdeep_signatory_title')
        }),
        ('Status', {
            'fields': ('status', 'created_by')
        }),
    )
    verbose_name = 'MOU'
    verbose_name_plural = 'MOUs'


@admin.register(Partnership)
class PartnershipAdmin(admin.ModelAdmin):
    list_display = ('name', 'partnership_type', 'status', 'start_date')
    list_filter = ('partnership_type', 'status', 'start_date')
    search_fields = ('name', 'contact_email', 'description')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Organization Information', {
            'fields': ('name', 'partnership_type', 'description', 'website')
        }),
        ('Contact Information', {
            'fields': ('contact_person', 'contact_email', 'contact_phone')
        }),
        ('Period', {
            'fields': ('start_date', 'end_date')
        }),
        ('Status', {
            'fields': ('status', 'notes')
        }),
    )
