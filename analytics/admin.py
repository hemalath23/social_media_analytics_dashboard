from django.contrib import admin
from .models import SocialMediaPlatform, SocialMediaAccount, Post, Analytics

admin.site.register(SocialMediaPlatform)
admin.site.register(SocialMediaAccount)
admin.site.register(Post)
admin.site.register(Analytics)
