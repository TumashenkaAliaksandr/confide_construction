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


class ServicesSlider(models.Model):
    """Services slides model"""
    name = models.CharField(max_length=100, verbose_name='name', null=False)
    image = models.ImageField(upload_to='services_slider', verbose_name='photo')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Services-Slider"
        verbose_name_plural = "Services-Slider"


class Recommended(models.Model):
    """Recommended model"""
    name = models.CharField(max_length=100, verbose_name='name')
    image = models.ImageField(upload_to='recommended', verbose_name='photo')
    is_main = models.BooleanField(default=False)
    link = models.URLField()  # Поле для хранения ссылки

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Recommended"
        verbose_name_plural = "Recommended"


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


class Project(models.Model):
    """Model for projects"""
    title = models.CharField(max_length=100, verbose_name='name')
    description = models.TextField(verbose_name='descriptions')
    image = models.ImageField(upload_to='projects', verbose_name='photo')
    is_main = models.BooleanField(default=False)
    link_project = models.URLField(default='True')  # Поле для хранения ссылки

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Project"


class Callback(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name