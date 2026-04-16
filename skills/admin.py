from django.contrib import admin
from .models import Skill, SkillLevel, SkillArea

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('get_name_display', 'order', 'is_active')
    list_filter = ('is_active', 'name')
    search_fields = ('name', 'description')
    readonly_fields = ('created_at', 'updated_at', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'slug', 'short_description', 'description')
        }),
        ('Content', {
            'fields': ('icon', 'image', 'learning_outcomes')
        }),
        ('Organization', {
            'fields': ('order', 'is_active')
        }),
    )


@admin.register(SkillLevel)
class SkillLevelAdmin(admin.ModelAdmin):
    list_display = ('skill', 'get_level_display', 'min_score', 'max_score')
    list_filter = ('skill', 'level')
    search_fields = ('skill__name', 'description')
    readonly_fields = ('created_at', 'updated_at')


@admin.register(SkillArea)
class SkillAreaAdmin(admin.ModelAdmin):
    list_display = ('skill', 'name', 'order')
    list_filter = ('skill',)
    search_fields = ('skill__name', 'name')
    readonly_fields = ('created_at', 'updated_at')
