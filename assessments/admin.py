from django.contrib import admin
from .models import Assessment, StudentAssessmentResult

class StudentAssessmentResultInline(admin.TabularInline):
    model = StudentAssessmentResult
    extra = 0
    fields = ('student', 'status', 'marks_obtained', 'is_passed')

@admin.register(Assessment)
class AssessmentAdmin(admin.ModelAdmin):
    list_display = ('title', 'program_project', 'assessment_type', 'total_marks', 'status')
    list_filter = ('assessment_type', 'status', 'program_project')
    search_fields = ('title', 'description')
    readonly_fields = ('created_at', 'updated_at')
    prepopulated_fields = {'slug': ('title',)}
    fieldsets = (
        ('Basic Information', {
            'fields': ('program_project', 'title', 'slug', 'assessment_type')
        }),
        ('Content', {
            'fields': ('description', 'content', 'file')
        }),
        ('Grading', {
            'fields': ('total_marks', 'passing_percentage')
        }),
        ('Details', {
            'fields': ('estimated_duration_minutes', 'order', 'status', 'created_by')
        }),
    )
    inlines = [StudentAssessmentResultInline]


@admin.register(StudentAssessmentResult)
class StudentAssessmentResultAdmin(admin.ModelAdmin):
    list_display = ('student', 'assessment', 'status', 'marks_obtained', 'is_passed')
    list_filter = ('assessment', 'status', 'is_passed', 'submission_date')
    search_fields = ('student__user__username', 'assessment__title')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Reference', {
            'fields': ('student', 'assessment')
        }),
        ('Submission', {
            'fields': ('status', 'submission_date')
        }),
        ('Grading', {
            'fields': ('marks_obtained', 'percentage_score', 'is_passed', 'graded_by', 'grading_date')
        }),
        ('Feedback', {
            'fields': ('feedback',)
        }),
    )
