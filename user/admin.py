# user/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User  # Import the custom User model


# Customizing the UserAdmin to display 'role' and other fields in the admin panel
class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('username', 'email', 'role', 'is_staff', 'is_active')  # Fields to display
    list_filter = ('role', 'is_staff', 'is_active')  # Filter users by role, staff, active status
    search_fields = ('username', 'email')  # Fields that can be searched
    ordering = ('username',)  # Default ordering by username

    # Customize the fields that appear when editing a user in the admin panel
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Role', {'fields': ('role',)}),  # Display 'role' field in the admin panel
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    # Customize the fields that appear when adding a user in the admin panel
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'role', 'is_staff', 'is_active')}
         ),
    )


# Register the custom User model with the custom admin (no need to unregister the default User model)
admin.site.register(User, CustomUserAdmin)
