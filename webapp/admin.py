from django.contrib import admin
from .models import *
from decimal import Decimal

@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_main', 'image', 'description')

class DisposalServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'advantages', 'material', 'price', 'discount', 'photo')

    def photo(self, obj):
        return ", ".join([str(photo) for photo in obj.photos.all()])

    photo.short_description = 'Photo'

admin.site.register(DisposalService, DisposalServiceAdmin)


@admin.register(ServicesSlider)
class ServicesSliderAdmin(admin.ModelAdmin):
    list_display = ('name', 'image')


@admin.register(Assessment)
class AssessmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'image')


@admin.register(Recommended)
class RecommendedAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_main', 'image')


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_main', 'image', 'description')


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'location', 'photo', 'pub_date')


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'phone', 'email', 'password')