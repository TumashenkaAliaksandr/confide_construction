from django.contrib import admin
from .models import *


@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_main', 'image', 'description')


@admin.register(ServicesSlider)
class ServicesSliderAdmin(admin.ModelAdmin):
    list_display = ('image',)


@admin.register(Recommended)
class RecommendedAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_main', 'image')


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_main', 'image', 'description')


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'location', 'photo', 'pub_date')
