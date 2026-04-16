from django.contrib import admin
from django.utils.html import format_html, mark_safe
from .models import School, SchoolProgram

class SchoolProgramInline(admin.TabularInline):
    model = SchoolProgram
    extra = 0
    fields = ('program', 'grade_level', 'start_date', 'status', 'number_of_students')

@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'status', 'mou_signed', 'appears_on_frontend')
    list_filter = ('status', 'mou_signed', 'city', 'state_province')
    search_fields = ('name', 'principal_email', 'admin_email')
    readonly_fields = ('created_at', 'updated_at', 'frontend_requirements')
    prepopulated_fields = {'slug': ('name',)}
    inlines = [SchoolProgramInline]
    fieldsets = (
        ('School Information', {
            'fields': ('name', 'slug', 'description', 'logo', 'website', 'established_year')
        }),
        ('Principal Contact', {
            'fields': ('principal_name', 'principal_email', 'principal_phone')
        }),
        ('Administrator Contact', {
            'fields': ('admin_contact_name', 'admin_email', 'admin_phone')
        }),
        ('Address', {
            'fields': ('street_address', 'city', 'state_province', 'postal_code', 'country')
        }),
        ('Program Details', {
            'fields': ('total_students', 'target_grades')
        }),
        ('Partnership & Frontend Display', {
            'fields': ('status', 'mou_signed', 'mou_date', 'frontend_requirements'),
            'description': '<strong>⚠️ Important:</strong> Schools only appear on the frontend when BOTH conditions are met: Status = "Active" AND MOU Signed = Checked'
        }),
    )

    def appears_on_frontend(self, obj):
        """Display whether school appears on frontend"""
        if obj.status == 'active' and obj.mou_signed:
            return mark_safe('<span style="color: green; font-weight: bold;">✓ Yes</span>')
        return mark_safe('<span style="color: red;">✗ No</span>')
    appears_on_frontend.short_description = 'Appears on Frontend?'

    def frontend_requirements(self, obj):
        """Display requirements for frontend display"""
        status_ok = obj.status == 'active'
        mou_ok = obj.mou_signed

        html = '<div style="padding: 10px; background: #f0f0f0; border-radius: 5px;">'
        html += '<strong>Requirements for Frontend Display:</strong><br>'
        html += f'<span style="color: {"green" if status_ok else "red"};">• Status: {obj.get_status_display()} {"✓" if status_ok else "✗"}</span><br>'
        html += f'<span style="color: {"green" if mou_ok else "red"};">• MOU Signed: {"Yes ✓" if mou_ok else "No ✗"}</span><br>'
        html += '<br><strong>Frontend Status:</strong><br>'

        if status_ok and mou_ok:
            html += '<span style="color: green; font-weight: bold;">✓ School WILL appear on frontend school listing</span>'
        else:
            html += '<span style="color: red; font-weight: bold;">✗ School WILL NOT appear on frontend</span><br>'
            html += '<p style="color: red; font-size: 12px;">To appear on frontend, ensure Status is "Active" and MOU Signed is checked.</p>'

        html += '</div>'
        return mark_safe(html)
    frontend_requirements.short_description = 'Frontend Display Status'


@admin.register(SchoolProgram)
class SchoolProgramAdmin(admin.ModelAdmin):
    list_display = ('school', 'program', 'grade_level', 'status', 'number_of_students')
    list_filter = ('school', 'status', 'program')
    search_fields = ('school__name', 'program__name')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Assignment', {
            'fields': ('school', 'program', 'grade_level')
        }),
        ('Details', {
            'fields': ('start_date', 'end_date', 'number_of_students', 'status', 'notes')
        }),
    )
