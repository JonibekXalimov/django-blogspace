from django.contrib import admin
from .models import Article, Comments

class ComementInline(admin.TabularInline):
    model = Comments
    extra = 0

class ArticleAdmin(admin.ModelAdmin):
    inlines = [ComementInline]

admin.site.register(Article, ArticleAdmin)
admin.site.register(Comments)