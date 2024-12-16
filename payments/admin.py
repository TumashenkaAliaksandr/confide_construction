from django.utils.html import strip_tags

from webapp.forms import CheckoutForm
from webapp.models import CheckoutDetails, Product
from django.contrib import admin


@admin.register(CheckoutDetails)
class CheckoutDetailsAdmin(admin.ModelAdmin):
    form = CheckoutForm
    list_display = ('last_name_check', 'date')  # Укажите необходимые поля для отображения в списке

    # Указываем поля, которые будут только для чтения
    readonly_fields = ('price_check', 'name_check')

    def get_readonly_fields(self, request, obj=None):
        # Вы можете добавить дополнительную логику для определения, какие поля делать только для чтения
        return super().get_readonly_fields(request, obj)

    def price_check(self, obj):
        return obj.price_check  # Возвращаем значение цены

    def name_check(self, obj):
        return obj.name_check  # Возвращаем название продукта

    price_check.short_description = 'Product Price'  # Заголовок колонки
    name_check.short_description = 'Product Name'  # Заголовок колонки


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
