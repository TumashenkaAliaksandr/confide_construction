from django.contrib import admin
from .models import *
from .models import Advertisement

@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_main', 'image', 'description')


class DrywallPhotoInline(admin.TabularInline):
    model = Drywall.photos.through
    extra = 6  # Это позволит добавить 6 фотографий

class DrywallAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'advantages', 'material', 'price', 'discount', 'display_photos')

    def display_photos(self, obj):
        return ", ".join([str(photo.photo) for photo in obj.photos.all()])

    display_photos.short_description = 'Photos'

    inlines = [DrywallPhotoInline]

admin.site.register(Drywall, DrywallAdmin)
admin.site.register(DrywallPhoto)


class DrywallServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'photo')

admin.site.register(DrywallService, DrywallServiceAdmin)


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


class HandymanPhotoInline(admin.TabularInline):
    model = Handyman.photos.through
    extra = 6  # Это позволит добавить 6 фотографий

class HandymanAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'advantages', 'material', 'price', 'discount', 'display_photos')

    def display_photos(self, obj):
        return ", ".join([str(photo.photo) for photo in obj.photos.all()])

    display_photos.short_description = 'Photos'

    inlines = [HandymanPhotoInline]

admin.site.register(Handyman, HandymanAdmin)
admin.site.register(HandymanPhoto)

class HandymanServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'photo')

admin.site.register(HandymanService, HandymanServiceAdmin)


class WallpaperPhotoInline(admin.TabularInline):
    model = Wallpaper.photos.through
    extra = 6  # Это позволит добавить 6 фотографий

class WallpaperAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'advantages', 'material', 'price', 'discount', 'display_photos')

    def display_photos(self, obj):
        return ", ".join([str(photo.photo) for photo in obj.photos.all()])

    display_photos.short_description = 'Photos'

    inlines = [WallpaperPhotoInline]

admin.site.register(Wallpaper, WallpaperAdmin)
admin.site.register(WallpaperPhoto)

class WallpaperServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'photo')

admin.site.register(WallpaperService, WallpaperServiceAdmin)



class DisposalPhotoInline(admin.TabularInline):
    model = Disposal.photos.through
    extra = 6  # Это позволит добавить 6 фотографий

class DisposalAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'advantages', 'material', 'price', 'discount', 'display_photos')

    def display_photos(self, obj):
        return ", ".join([str(photo.photo) for photo in obj.photos.all()])

    display_photos.short_description = 'Photos'

    inlines = [DisposalPhotoInline]

admin.site.register(Disposal, DisposalAdmin)
admin.site.register(DisposalPhoto)

class DisposalServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'photo')

admin.site.register(DisposalService, DisposalServiceAdmin)



class PaintingPhotoInline(admin.TabularInline):
    model = Painting.photos.through
    extra = 6  # Это позволит добавить 6 фотографий

class PaintingAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'advantages', 'material', 'price', 'discount', 'display_photos')

    def display_photos(self, obj):
        return ", ".join([str(photo.photo) for photo in obj.photos.all()])

    display_photos.short_description = 'Photos'

    inlines = [PaintingPhotoInline]

admin.site.register(Painting, PaintingAdmin)
admin.site.register(PaintingPhoto)

class PaintingServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'photo')

admin.site.register(PaintingService, PaintingServiceAdmin)


class FurniturePhotoInline(admin.TabularInline):
    model = Furniture.photos.through
    extra = 6  # Это позволит добавить 6 фотографий

class FurnitureAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'advantages', 'material', 'price', 'discount', 'display_photos')

    def display_photos(self, obj):
        return ", ".join([str(photo.photo) for photo in obj.photos.all()])

    display_photos.short_description = 'Photos'

    inlines = [FurniturePhotoInline]

admin.site.register(Furniture, FurnitureAdmin)
admin.site.register(FurniturePhoto)

class FurnitureServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'photo')

admin.site.register(FurnitureService, FurnitureServiceAdmin)



class SoundproofingPhotoInline(admin.TabularInline):
    model = Soundproofing.photos.through
    extra = 6  # Это позволит добавить 6 фотографий

class SoundproofingAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'advantages', 'material', 'price', 'discount', 'display_photos')

    def display_photos(self, obj):
        return ", ".join([str(photo.photo) for photo in obj.photos.all()])

    display_photos.short_description = 'Photos'

    inlines = [SoundproofingPhotoInline]

admin.site.register(Soundproofing, SoundproofingAdmin)
admin.site.register(SoundproofingPhoto)

class SoundproofingServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'photo')

admin.site.register(SoundproofingService, SoundproofingServiceAdmin)



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
