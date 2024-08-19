from django.utils.html import strip_tags

from webapp.forms import CheckoutForm
from webapp.models import CheckoutDetails
from django.contrib import admin


@admin.register(CheckoutDetails)
class TicksAdmin(admin.ModelAdmin):
    form = CheckoutForm

    # Кастомное поле для отображения очищенного текста
    def clean_first_name(self, obj):
        return strip_tags(obj.first_name_check)

    clean_first_name.short_description = 'First Name'
