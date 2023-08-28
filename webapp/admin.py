from django.contrib import admin
from .models import *

@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_main', 'image', 'description')  # Определите поля, которые вы хотите отображать в списке объектов в админке


@admin.register(Recommended)
class RecommendedAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_main', 'image')  # Определите поля, которые вы хотите отображать в списке объектов в админке

