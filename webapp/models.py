from django.db import models
from django.urls import reverse


class Services(models.Model):
    """Services model"""
    name = models.CharField(max_length=100, verbose_name='name')
    description = models.TextField(verbose_name='description')
    image = models.ImageField(upload_to='services', verbose_name='photo')
    is_main = models.BooleanField(default=False)
    link = models.URLField()  # Поле для хранения ссылки

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Services"
        verbose_name_plural = "Services"


class Recommended(models.Model):
    """Recommended model"""
    name = models.CharField(max_length=100, verbose_name='name')
    image = models.ImageField(upload_to='recommended', verbose_name='photo')
    is_main = models.BooleanField(default=False)
    link = models.URLField()  # Поле для хранения ссылки

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "recommended"
        verbose_name_plural = "recommended"


class News(models.Model):
    """News Model"""
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')
    location = models.CharField(max_length=200, verbose_name='Место', default='')
    photo = models.ImageField(upload_to='news_photos/', null=True, blank=True, verbose_name='Фото')
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Новости"
        verbose_name_plural = "Новости"

    def get_absolute_url(self):
        return reverse('news-datail', kwargs={'pk': self.id})