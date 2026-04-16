from django.contrib import admin
from .models import SiteSetting, HomePage, Feature, FAQ

# Register your models here.

@admin.register(SiteSetting)
class SiteSettingAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Basic Information', {
            'fields': ('site_name', 'tagline', 'description', 'logo', 'favicon')
        }),
        ('Contact Information', {
            'fields': ('email', 'phone_primary', 'phone_secondary')
        }),
        ('Address', {
            'fields': ('street_address', 'city', 'state', 'postal_code', 'country')
        }),
        ('Social Media', {
            'fields': ('facebook_url', 'twitter_url', 'linkedin_url', 'youtube_url', 'instagram_url'),
            'classes': ('collapse',)
        }),
        ('Design Settings', {
            'fields': ('primary_color', 'secondary_color', 'accent_color'),
            'classes': ('collapse',)
        }),
        ('Configuration', {
            'fields': ('maintenance_mode', 'allow_registration')
        }),
    )
    readonly_fields = ('created_at', 'updated_at')

    def has_add_permission(self, request):
        return not SiteSetting.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(HomePage)
class HomePageAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Main Content', {
            'fields': ('title', 'hero_subtitle', 'hero_image', 'hero_description')
        }),
        ('Call to Action', {
            'fields': ('cta_button_text', 'cta_button_url')
        }),
        ('Featured Section', {
            'fields': ('featured_section_title', 'featured_section_description')
        }),
        ('Status', {
            'fields': ('is_published',)
        }),
    )
    readonly_fields = ('created_at', 'updated_at')


@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ('title', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    search_fields = ('title', 'description')
    readonly_fields = ('created_at', 'updated_at')


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'category', 'order', 'is_active')
    list_filter = ('category', 'is_active')
    search_fields = ('question', 'answer')
    readonly_fields = ('created_at', 'updated_at')

