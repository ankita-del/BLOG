from django.contrib import admin
from .models import UserProfile

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('username', 'gender', 'email', 'location', 'profile_image_tag')
    readonly_fields = ('profile_image_tag',)

    def profile_image_tag(self, obj):
        return f'<img src="{obj.profile_image.url}" style="max-width:200px;max-height:200px;" />'

    profile_image_tag.allow_tags = True
    profile_image_tag.short_description = 'Profile Image'
