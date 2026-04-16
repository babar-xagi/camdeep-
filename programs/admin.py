from django.contrib import admin
from .models import Program, ProgramProject, ProgramModule

class ProgramProjectInline(admin.TabularInline):
    model = ProgramProject
    extra = 0
    fields = ('title', 'project_number', 'duration_days', 'status', 'order')

@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ('name', 'skill', 'target_grade', 'status')
    list_filter = ('skill', 'target_grade', 'status')
    search_fields = ('name', 'description')
    readonly_fields = ('created_at', 'updated_at')
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ProgramProjectInline]
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'slug', 'skill', 'target_grade', 'description')
        }),
        ('Content', {
            'fields': ('learning_outcomes', 'thumbnail', 'duration_days')
        }),
        ('Status', {
            'fields': ('status', 'created_by')
        }),
    )


class ProgramModuleInline(admin.TabularInline):
    model = ProgramModule
    extra = 0
    fields = ('title', 'order')

@admin.register(ProgramProject)
class ProgramProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'program', 'project_number', 'duration_days', 'status')
    list_filter = ('program', 'status')
    search_fields = ('title', 'description')
    readonly_fields = ('created_at', 'updated_at')
    inlines = [ProgramModuleInline]
    fieldsets = (
        ('Basic Information', {
            'fields': ('program', 'title', 'slug', 'project_number', 'description')
        }),
        ('Content', {
            'fields': ('objectives', 'deliverables', 'resources')
        }),
        ('Organization', {
            'fields': ('duration_days', 'order', 'status')
        }),
    )


@admin.register(ProgramModule)
class ProgramModuleAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'order')
    list_filter = ('project',)
    search_fields = ('title', 'content')
    readonly_fields = ('created_at', 'updated_at')
