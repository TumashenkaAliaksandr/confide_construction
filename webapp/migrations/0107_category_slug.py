# Generated by Django 4.2.4 on 2025-01-02 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0106_category_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(max_length=200, null=True, unique=True),
        ),
    ]
