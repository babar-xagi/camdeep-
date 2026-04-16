from django.contrib import admin
from .models import Page, BlogPost, Testimonial, ContactMessage

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('title', 'slug', 'content')
    readonly_fields = ('created_at', 'updated_at')
    prepopulated_fields = {'slug': ('title',)}
    fieldsets = (
        ('Page Information', {
            'fields': ('title', 'slug', 'featured_image')
        }),
        ('Content', {
            'fields': ('content',)
        }),
        ('SEO', {
            'fields': ('description', 'keywords'),
            'classes': ('collapse',)
        }),
        ('Publishing', {
            'fields': ('status', 'author')
        }),
    )


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'status', 'published_date', 'view_count')
    list_filter = ('status', 'category', 'published_date')
    search_fields = ('title', 'content', 'author__username')
    readonly_fields = ('created_at', 'updated_at', 'view_count')
    prepopulated_fields = {'slug': ('title',)}
    fieldsets = (
        ('Post Information', {
            'fields': ('title', 'slug', 'featured_image')
        }),
        ('Content', {
            'fields': ('excerpt', 'content')
        }),
        ('Metadata', {
            'fields': ('category', 'tags', 'read_time_minutes')
        }),
        ('Publishing', {
            'fields': ('status', 'published_date', 'author')
        }),
        ('Statistics', {
            'fields': ('view_count',)
        }),
    )


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('author_name', 'rating', 'status', 'featured')
    list_filter = ('status', 'featured', 'rating', 'related_skill')
    search_fields = ('author_name', 'content')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Testimonial Information', {
            'fields': ('author_name', 'author_title', 'author_image')
        }),
        ('Content', {
            'fields': ('content', 'rating')
        }),
        ('Relations', {
            'fields': ('related_skill', 'related_program')
        }),
        ('Status', {
            'fields': ('status', 'featured')
        }),
    )


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'status', 'created_at')
    list_filter = ('status', 'message_type', 'created_at')
    search_fields = ('name', 'email', 'subject', 'message')
    readonly_fields = ('created_at', 'name', 'email', 'phone', 'subject', 'message')
    fieldsets = (
        ('Message Information', {
            'fields': ('name', 'email', 'phone', 'subject', 'message_type')
        }),
        ('Message Content', {
            'fields': ('message',)
        }),
        ('Response', {
            'fields': ('replied_message', 'replied_by', 'replied_date')
        }),
        ('Status', {
            'fields': ('status',)
        }),
    )

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

