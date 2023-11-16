# Generated by Django 4.2.4 on 2023-11-16 10:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Name')),
                ('description', models.TextField(verbose_name='Descriptions')),
                ('location', models.CharField(default='', max_length=200, verbose_name='Locations')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='news_photos/', verbose_name='Photo')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='Date')),
                ('author_photo', models.ImageField(blank=True, null=True, upload_to='author_photos/', verbose_name='Author Photo')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='news', to=settings.AUTH_USER_MODEL, verbose_name='Author')),
            ],
            options={
                'verbose_name': 'News',
                'verbose_name_plural': 'News',
            },
        ),
    ]
