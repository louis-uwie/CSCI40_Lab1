from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Profile

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'

class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline,)

# Unregister the default User admin
admin.site.unregister(User)

# Register the custom User admin
admin.site.register(User, CustomUserAdmin)
