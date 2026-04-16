from django.contrib import admin
from .models import ResourceCategory, Resource

@admin.register(ResourceCategory)
class ResourceCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'order')
    list_editable = ('order',)
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ()


@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    list_display = ('title', 'resource_type', 'category', 'is_featured', 'download_count')
    list_filter = ('resource_type', 'category', 'is_featured', 'status')
    search_fields = ('title', 'description', 'author')
    readonly_fields = ('created_at', 'updated_at', 'download_count', 'view_count', 'created_by')
    prepopulated_fields = {'slug': ('title',)}
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'slug', 'category', 'resource_type')
        }),
        ('Content', {
            'fields': ('description', 'thumbnail', 'file', 'external_url')
        }),
        ('Metadata', {
            'fields': ('author', 'publication_date')
        }),
        ('Relations', {
            'fields': ('related_skills', 'related_programs'),
            'classes': ('collapse',)
        }),
        ('Statistics', {
            'fields': ('download_count', 'view_count')
        }),
        ('Publishing', {
            'fields': ('status', 'is_featured', 'created_by')
        }),
    )
    filter_horizontal = ('related_skills', 'related_programs')
