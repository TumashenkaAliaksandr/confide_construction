# Generated by Django 4.2.4 on 2023-12-29 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0065_backsplashphoto_backsplashservice_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CheckoutDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('company_name', models.CharField(blank=True, max_length=100, null=True)),
                ('street_address', models.CharField(max_length=255)),
                ('town_city', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('order_notes', models.TextField()),
            ],
        ),
    ]
