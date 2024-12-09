from django.contrib import admin
from .models import *
from .models import Advertisement


@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_main', 'image', 'description')


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


@admin.register(Profile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'email', 'password')


@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ('title', 'image_tag', 'link', 'active', 'created_at', 'updated_at')
    list_filter = ('active',)
    search_fields = ('title', 'link')
    readonly_fields = ('image_tag', 'created_at', 'updated_at')

    def image_tag(self, obj):
        return obj.image.url if obj.image else None

    image_tag.short_description = 'Image Preview'

    fieldsets = (
        ('Advertisement Details', {
            'fields': ('title', 'image', 'image_tag', 'link', 'active')
        }),
    )


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('author', 'text', 'created_at', 'rating', 'approved')
    list_filter = ('approved', 'rating')
    search_fields = ('author', 'text')
    ordering = ('-created_at',)


admin.site.register(Review, ReviewAdmin)
