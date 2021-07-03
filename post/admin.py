from django.contrib import admin
from .models import Category, Post, Comment, Language, PostLanguage

admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Language)
admin.site.register(PostLanguage)

admin.AdminSite.site_header = 'Blog'