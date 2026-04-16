from django.contrib import admin
from .models import Student, StudentProgramEnrollment, StudentSkillProgress

class StudentSkillProgressInline(admin.TabularInline):
    model = StudentSkillProgress
    extra = 0
    fields = ('skill', 'current_level', 'score', 'assessments_completed')

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('roll_number', 'user', 'school', 'grade', 'status')
    list_filter = ('school', 'grade', 'status')
    search_fields = ('roll_number', 'user__username', 'user__email')
    readonly_fields = ('created_at', 'updated_at', 'enrollment_date')
    fieldsets = (
        ('User Account', {
            'fields': ('user', 'roll_number')
        }),
        ('School Information', {
            'fields': ('school', 'grade', 'enrollment_date')
        }),
        ('Guardian Information', {
            'fields': ('guardian_name', 'guardian_email', 'guardian_phone')
        }),
        ('Additional Info', {
            'fields': ('date_of_birth', 'status')
        }),
    )


@admin.register(StudentProgramEnrollment)
class StudentProgramEnrollmentAdmin(admin.ModelAdmin):
    list_display = ('student', 'program', 'status', 'progress_percentage', 'enrollment_date')
    list_filter = ('program', 'status', 'enrollment_date')
    search_fields = ('student__user__username', 'program__name')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Enrollment', {
            'fields': ('student', 'program', 'school_program')
        }),
        ('Status', {
            'fields': ('status', 'enrollment_date', 'completion_date')
        }),
        ('Progress', {
            'fields': ('progress_percentage',)
        }),
    )
    inlines = [StudentSkillProgressInline]


@admin.register(StudentSkillProgress)
class StudentSkillProgressAdmin(admin.ModelAdmin):
    list_display = ('enrollment', 'skill', 'current_level', 'score')
    list_filter = ('skill', 'current_level')
    search_fields = ('enrollment__student__user__username', 'skill__name')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Reference', {
            'fields': ('enrollment', 'skill')
        }),
        ('Progress', {
            'fields': ('current_level', 'score', 'assessments_completed', 'last_assessment_date')
        }),
        ('Notes', {
            'fields': ('notes',)
        }),
    )
