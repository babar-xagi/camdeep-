from django.contrib import admin
from .models import School, SchoolProgram

class SchoolProgramInline(admin.TabularInline):
    model = SchoolProgram
    extra = 0
    fields = ('program', 'grade_level', 'start_date', 'status', 'number_of_students')

@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'status', 'mou_signed')
    list_filter = ('status', 'mou_signed', 'city')
    search_fields = ('name', 'principal_email', 'admin_email')
    readonly_fields = ('created_at', 'updated_at')
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
        ('Partnership', {
            'fields': ('status', 'mou_signed', 'mou_date')
        }),
    )


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
