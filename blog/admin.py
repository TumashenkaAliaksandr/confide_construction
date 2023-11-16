from django.contrib import admin
from blog.models import BlogNews


@admin.register(BlogNews)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'description_small', 'location', 'photo', 'pub_date', 'author', 'comment_author')

    def author(self, obj):
        return obj.author.username if obj.author else '-'

    author.short_description = 'Author'
