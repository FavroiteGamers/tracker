from django.contrib import admin

from .models import TrackerUser, Gender
from django.contrib.auth.admin import UserAdmin

class TrackerUserAdmin(UserAdmin):
    add_fieldsets = (
        (None, {
            'fields': ('username', 'password1', 'password2')
        }),
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'email', 'gender')
        }),
        ('Permissions', {
            'fields': (
                'is_active', 'is_staff', 'is_superuser',
                'groups', 'user_permissions'
                )
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined')
        }),
        ('Biological Information', {
            'fields': ('weight', 'height', 'exercise')
        })
    )

    list_display = (
    'username', 'email', 'first_name', 'last_name', 'is_staff',
    'weight', 'height'
    )

admin.site.register(TrackerUser, TrackerUserAdmin)


@admin.register(Gender)
class GenderAdmin(admin.ModelAdmin):
    pass