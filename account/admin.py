from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Account

# Register your models here.

# Description: Setting User Account Model At Admin Panel
# Precondition: None
# Postcondition: Ordering is based on name
class AccountAdmin(BaseUserAdmin):
    list_display = ('email', 'name', 'phone', 'is_staff',  'is_superuser')
    list_filter = ('is_superuser',)

    fieldsets = (
        (None,
            {'fields': ('email', 'is_staff', 'is_superuser', 'password')}
         ),
        ('Personal info',
            {'fields': ('name', 'phone', 'profile_image')}
         ),
        ('Groups',
            {'fields': ('groups',)}
         ),
        ('Permissions',
            {'fields': ('user_permissions',)}
         ),
    )
    add_fieldsets = (
        (None, 
            {'fields': ('email', 'is_staff','is_superuser', 'password1', 'password2')}
        ),
        ('Personal info', 
            {'fields': ('name', 'phone', 'profile_image')}
        ),
        ('Groups', 
            {'fields': ('groups',)}
        ),
        ('Permissions',
            {'fields': ('user_permissions',)}
        ),
    )

    search_fields = ('email', 'name', 'phone')
    ordering = ('name',)
    filter_horizontal = ()


admin.site.register(Account, AccountAdmin)
