from django.utils.html import strip_tags

from webapp.forms import CheckoutForm
from webapp.models import CheckoutDetails, Product
from django.contrib import admin


@admin.register(CheckoutDetails)
class TicksAdmin(admin.ModelAdmin):
    form = CheckoutForm

    # Кастомное поле для отображения очищенного текста
    def clean_last_name(self, obj):
        return strip_tags(obj.last_name_check)

    clean_last_name.short_description = 'Last Name'

    def clean_price_check(self, obj):
        return strip_tags(obj.price_check)

    clean_price_check.short_description = 'Product Price'


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'discount')  # Поля, отображаемые в списке
    prepopulated_fields = {'slug': ('name',)}  # Автоматическое заполнение slug на основе имени
    search_fields = ('name', 'description')  # Поля для поиска
    ordering = ('name',)  # Порядок сортировки
    list_filter = ('discount',)  # Фильтры для боковой панели

    def save_model(self, request, obj, form, change):
        """Метод для обработки сохранения модели"""
        super().save_model(request, obj, form, change)


# Регистрация модели Product с настройками ProductAdmin
admin.site.register(Product, ProductAdmin)
