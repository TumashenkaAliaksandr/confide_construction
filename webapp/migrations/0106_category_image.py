# Generated by Django 4.2.4 on 2024-12-22 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0105_category_product_categories'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='categories/'),
        ),
    ]