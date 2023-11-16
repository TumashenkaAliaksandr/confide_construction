from django.contrib import admin
from blog.models import News


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'location', 'photo', 'pub_date')
