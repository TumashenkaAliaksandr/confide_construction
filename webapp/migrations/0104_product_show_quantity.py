# Generated by Django 4.2.4 on 2024-12-13 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0103_remove_backsplash_photos_delete_backsplashservice_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='show_quantity',
            field=models.BooleanField(default=False),
        ),
    ]
