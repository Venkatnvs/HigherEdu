from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, UserType

class UserTypeAdmin(admin.ModelAdmin):
    list_display = ['name']
    filter_horizontal = ['permissions']

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['email', 'full_name', 'usn', 'mobile_no', 'user_type', 'is_active', 'is_staff',"is_completed"]
    search_fields = ['email', 'full_name', 'usn', 'mobile_no']
    list_filter = ['user_type', 'is_active', 'is_staff',"is_completed"]

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('full_name', 'mobile_no')}),
        ('Study Details', {'fields': ('usn', 'country', 'course', 'graduation_year', 'abroad_year', 'abroad_season')}),
        ('Permissions', {'fields': ('user_type', 'is_active', 'is_staff', 'is_superuser',"is_completed")}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'user_type'),
        }),
    )

    ordering = ['email']

admin.site.register(UserType, UserTypeAdmin)
admin.site.register(CustomUser, CustomUserAdmin)
