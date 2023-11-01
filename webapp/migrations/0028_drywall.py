# Generated by Django 4.2.4 on 2023-11-01 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0027_services_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Drywall',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('description', models.TextField(verbose_name='Description')),
                ('advantages', models.TextField(verbose_name='Benefits')),
                ('material', models.CharField(max_length=100, verbose_name='Material')),
                ('photo', models.ImageField(default=0, upload_to='drywall_photos/', verbose_name='Photo')),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='Price')),
                ('discount', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='Discount')),
            ],
            options={
                'verbose_name': 'Drywall',
                'verbose_name_plural': 'Drywall',
            },
        ),
    ]
