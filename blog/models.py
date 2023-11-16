from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class News(models.Model):
    """News Model"""
    title = models.CharField(max_length=200, verbose_name='Name')
    description = models.TextField(verbose_name='Descriptions')
    location = models.CharField(max_length=200, verbose_name='Locations', default='')
    photo = models.ImageField(upload_to='news_photos/', null=True, blank=True, verbose_name='Photo')
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name='Data')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "News"
        verbose_name_plural = "News"

    def get_absolute_url(self):
        return reverse('news-datail', kwargs={'pk': self.id})

