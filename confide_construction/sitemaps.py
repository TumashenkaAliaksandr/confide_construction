# webapp/sitemaps.py
from django.contrib.sitemaps import Sitemap
from webapp.models import Services, Product
from django.shortcuts import reverse



class ProductSitemap(Sitemap):
    changefreq = 'weekly'  # Частота изменения
    priority = 0.8         # Приоритет страницы

    def items(self):
        return Product.objects.all()  # Получаем все объекты Product

    def location(self, item):
        return f'/product/{item.slug}/'  # Используем метод get_absolute_url() на экземпляре объекта


class ServicesSitemap(Sitemap):
    changefreq = 'weekly'  # Частота изменения
    priority = 0.8         # Приоритет страницы

    def items(self):
        return Services.objects.all().order_by('description')  # Получаем все объекты Services

    def location(self, item):
        return f'/service/{item.description}/'  # Используем slug для генерации URL
