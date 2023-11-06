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


class DrywallAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'advantages', 'material', 'price', 'discount', 'photo')

    def photo(self, obj):
        return ", ".join([str(photo) for photo in obj.photos.all()])

    photo.short_description = 'Photo'

admin.site.register(Drywall, DrywallAdmin)


class SoundproofingAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'advantages', 'material', 'price', 'discount', 'photo')

    def photo(self, obj):
        return ", ".join([str(photo) for photo in obj.photos.all()])

    photo.short_description = 'Photo'

admin.site.register(Soundproofing, SoundproofingAdmin)


class BacksplashAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'advantages', 'material', 'price', 'discount', 'photo')

    def photo(self, obj):
        return ", ".join([str(photo) for photo in obj.photos.all()])

    photo.short_description = 'Photo'

admin.site.register(Backsplash, BacksplashAdmin)


class ElectricalPhotoInline(admin.TabularInline):
    model = Electrical.photos.through
    extra = 6  # Это позволит добавить 6 фотографий

class ElectricalAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'advantages', 'material', 'price', 'discount', 'display_photos')

    def display_photos(self, obj):
        return ", ".join([str(photo.photo) for photo in obj.photos.all()])

    display_photos.short_description = 'Photos'

    inlines = [ElectricalPhotoInline]

admin.site.register(Electrical, ElectricalAdmin)
admin.site.register(ElectricalPhoto)

class ElectricalServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'photo')

admin.site.register(ElectricalService, ElectricalServiceAdmin)


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


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('author', 'created_at', 'rating', 'approved')
    list_filter = ('approved',)
    search_fields = ('author', 'email', 'text')
    list_editable = ('approved',)

@admin.register(Quality)
class QualityAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'icon')
