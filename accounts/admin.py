from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import CustomUser, UserRole, AuditLog

# Register your models here.

@admin.register(CustomUser)
class CustomUserAdmin(BaseUserAdmin):
    fieldsets = BaseUserAdmin.fieldsets + (
        ('CAMDEEP Profile', {
            'fields': ('phone_number', 'profile_picture', 'bio', 'role', 'is_verified')
        }),
        ('Address', {
            'fields': ('street_address', 'city', 'state_province', 'postal_code', 'country'),
            'classes': ('collapse',)
        }),
    )
    list_display = ('username', 'email', 'get_full_name', 'role', 'is_active')
    list_filter = BaseUserAdmin.list_filter + ('role', 'is_verified', 'is_active')
    search_fields = ('username', 'email', 'first_name', 'last_name')


@admin.register(UserRole)
class UserRoleAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at')
    search_fields = ('user__username', 'user__email')
    readonly_fields = ('created_at', 'updated_at')


@admin.register(AuditLog)
class AuditLogAdmin(admin.ModelAdmin):
    list_display = ('user', 'action', 'timestamp')
    list_filter = ('action', 'timestamp')
    search_fields = ('user__username', 'action', 'description')
    readonly_fields = ('timestamp', 'user', 'action', 'description', 'ip_address', 'user_agent')
    
    def has_add_permission(self, request):
        return False
    
    def has_delete_permission(self, request, obj=None):
        return False
    
    def has_change_permission(self, request, obj=None):
        return False

