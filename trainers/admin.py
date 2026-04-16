from django.contrib import admin
from .models import Trainer, TrainerAssignment, TrainerFeedback

class TrainerAssignmentInline(admin.TabularInline):
    model = TrainerAssignment
    extra = 0
    fields = ('school', 'program', 'start_date', 'status')

@admin.register(Trainer)
class TrainerAdmin(admin.ModelAdmin):
    list_display = ('employee_id', 'experience_years', 'status')
    list_filter = ('status', 'experience_years', 'skills_expertise')
    search_fields = ('user__username', 'user__email', 'employee_id')
    readonly_fields = ('created_at', 'updated_at', 'joining_date')
    inlines = [TrainerAssignmentInline]
    fieldsets = (
        ('User Account', {
            'fields': ('user',)
        }),
        ('Personal Information', {
            'fields': ('employee_id', 'experience_years', 'bio', 'qualifications')
        }),
        ('Expertise', {
            'fields': ('skills_expertise',)
        }),
        ('Status', {
            'fields': ('status', 'joining_date')
        }),
    )
    filter_horizontal = ('skills_expertise',)


@admin.register(TrainerAssignment)
class TrainerAssignmentAdmin(admin.ModelAdmin):
    list_display = ('trainer', 'school', 'program', 'start_date', 'status')
    list_filter = ('status', 'school', 'trainer')
    search_fields = ('trainer__user__username', 'school__name')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Assignment', {
            'fields': ('trainer', 'school', 'program')
        }),
        ('Period', {
            'fields': ('start_date', 'end_date')
        }),
        ('Details', {
            'fields': ('visit_frequency', 'status', 'notes')
        }),
    )


@admin.register(TrainerFeedback)
class TrainerFeedbackAdmin(admin.ModelAdmin):
    list_display = ('trainer', 'school', 'visit_date', 'rating')
    list_filter = ('visit_date', 'rating', 'school')
    search_fields = ('trainer__user__username', 'school__name', 'observations')
    readonly_fields = ('created_at',)
    fieldsets = (
        ('Feedback', {
            'fields': ('trainer', 'school', 'program', 'visit_date')
        }),
        ('Content', {
            'fields': ('observations', 'rating', 'recommendations')
        }),
    )
