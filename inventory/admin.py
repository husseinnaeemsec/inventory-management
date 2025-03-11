from django.contrib import admin
from django.contrib.auth.models import Permission
from .models import UserRole,Inventory,Role
# Register your models here.

class PermissionAdmin(admin.ModelAdmin):
    list_display = ('codename', 'name', 'content_type')
    search_fields = ('codename', 'name')
    ordering = ('content_type', 'codename')
admin.site.register(Permission,PermissionAdmin)


class UserRoleAdmin(admin.ModelAdmin):
    list_display = ('user', 'role')
    search_fields = ('user__username', 'role__name')
    ordering = ('user', 'role')


class InventoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    search_fields = ('name', 'location')
    ordering = ('name', 'location')


class RoleAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)
    filter_horizontal = ('permissions',)

admin.site.register(UserRole, UserRoleAdmin)
admin.site.register(Inventory, InventoryAdmin)
admin.site.register(Role, RoleAdmin)