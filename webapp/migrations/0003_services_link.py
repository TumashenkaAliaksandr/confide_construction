# Generated by Django 4.2.4 on 2023-08-28 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_remove_services_color_remove_services_likes_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='services',
            name='link',
            field=models.URLField(default=2),
            preserve_default=False,
        ),
    ]
