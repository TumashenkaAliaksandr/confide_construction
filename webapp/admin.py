from django.contrib import admin

from .forms import BasketItemForm, BasketForm
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


class SubcategoryInline(admin.TabularInline):
    model = Subcategory
    extra = 1  # Количество пустых форм для добавления подкатегорий

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Поля, которые будут отображаться в списке
    search_fields = ('name',)  # Поля, по которым можно будет искать
    ordering = ('name',)  # Сортировка по имени
    inlines = [SubcategoryInline]  # Встраивание подкатегорий в админке

# Регистрация модели Category с настройками админки
admin.site.register(Category, CategoryAdmin)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'zip_code')



class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'client_email', 'amount', 'created_at', 'invoice_link')  # Поле ссылки добавлено
    search_fields = ('client_name', 'client_email')  # Поля для поиска
    list_filter = ('created_at',)  # Фильтрация по дате создания
    readonly_fields = ('created_at',)  # Поле даты только для чтения

# Регистрация модели Invoice с настройками админки
admin.site.register(Invoice, InvoiceAdmin)


class BasketItemInline(admin.TabularInline):
    model = BasketItem
    form = BasketItemForm
    extra = 1  # Дополнительные строки в админке, по умолчанию 1

class BasketAdmin(admin.ModelAdmin):
    form = BasketForm
    inlines = [BasketItemInline]  # Вставляем inline для BasketItem
    list_display = ['user', 'created_at']
    search_fields = ['user__username']

class BasketItemAdmin(admin.ModelAdmin):
    form = BasketItemForm
    list_display = ['product', 'basket', 'quantity']
    search_fields = ['product__name', 'basket__user__username']

admin.site.register(Basket, BasketAdmin)
admin.site.register(BasketItem, BasketItemAdmin)
