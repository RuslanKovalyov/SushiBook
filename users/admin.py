from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser, Profile, Post, PostLike, PostComment

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('email', 'is_staff', 'is_active',)
    list_filter = ('email', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)

#admin.site.register(Profile)
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'country', 'current_position', 'first_name', 'last_name', 'avatar',)
    fields = [('user', 'first_name', 'last_name', 'date_of_birth',),('country', 'city', 'phone',), 'current_position', 'credo', ('avatar', 'profile_background',), ]

@admin.register(Post)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ( 'author', 'title', 'date', 'picture',)
    fields = [('author', 'title',),'story', 'picture',]



admin.site.register(PostLike)
admin.site.register(PostComment)
