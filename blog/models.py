from django.contrib.auth.models import User
from django.db import models
from django.conf import settings



class BlogNews(models.Model):
    title = models.CharField(max_length=200, verbose_name='Name')
    description_small = models.TextField(max_length=400, default='', verbose_name='Description_small')
    description = models.TextField(verbose_name='Description')
    location = models.CharField(max_length=200, verbose_name='Location', default='')
    photo = models.ImageField(upload_to='news_photos/', null=True, blank=True, verbose_name='Photo')
    pub_date = models.DateTimeField(verbose_name='Publication Date')  # Added publication date field
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Author', related_name='news', null=True, blank=True)
    author_photo = models.ImageField(upload_to='author_photos/', null=True, blank=True, verbose_name='Author Photo')
    comment_author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                                       verbose_name='Comment Author', related_name='comments', null=True, blank=True)
    comment = models.TextField(verbose_name='Comment', default='Your default comment here')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'
