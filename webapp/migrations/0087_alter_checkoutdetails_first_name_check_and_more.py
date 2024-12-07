# Generated by Django 4.2.4 on 2024-11-25 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0086_checkoutdetails_name_check'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkoutdetails',
            name='first_name_check',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='checkoutdetails',
            name='last_name_check',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='checkoutdetails',
            name='phone_number',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='checkoutdetails',
            name='street_address',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='checkoutdetails',
            name='town_city',
            field=models.CharField(default='', max_length=100),
        ),
    ]
