"""Module for admin configuration for the users application."""

from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model
from users.forms import UserChangeForm, UserCreationForm
from users.models import Entity

User = get_user_model()


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    """Custom user admin class."""

    form = UserChangeForm
    add_form = UserCreationForm

    list_display = [
        'email', 'first_name', 'last_name', 'institution_name',
        'membership_category', 'is_paid_up', 'membership_expiry',
        'is_approved', 'is_superuser'
    ]
    list_filter = ['is_approved', 'is_paid_up', 'membership_category', 'is_superuser']
    search_fields = ['email', 'first_name', 'last_name', 'institution_name']
    ordering = ['email']

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name')}),
        ('Institution info', {'fields': ('institution_name', 'institution_address')}),
        ('Membership', {'fields': ('membership_category', 'is_paid_up', 'membership_expiry')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'is_approved', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email', 'password1', 'password2',
                'first_name', 'last_name',
                'institution_name', 'institution_address',
                'membership_category', 'is_paid_up', 'membership_expiry',
                'is_approved', 'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions',
            ),
        }),
    )

admin.site.register(Entity)
