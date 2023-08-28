from django.db import models


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

    image = models.ImageField(upload_to='recommended', verbose_name='photo')
    is_main = models.BooleanField(default=False)
    link = models.URLField()  # Поле для хранения ссылки

    class Meta:
        verbose_name = "recommended"
        verbose_name_plural = "recommended"
