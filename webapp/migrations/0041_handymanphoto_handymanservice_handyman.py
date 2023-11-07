# Generated by Django 4.2.4 on 2023-11-07 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0040_electricalservice'),
    ]

    operations = [
        migrations.CreateModel(
            name='HandymanPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(default=0, upload_to='handyman_photos/', verbose_name='Photo')),
            ],
            options={
                'verbose_name': 'Photo for Handyman',
                'verbose_name_plural': 'Photos for Handyman',
            },
        ),
        migrations.CreateModel(
            name='HandymanService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('description', models.TextField(verbose_name='Description')),
                ('photo', models.ImageField(upload_to='handymanservice_photos/', verbose_name='Photo')),
            ],
            options={
                'verbose_name': 'HandymanService',
                'verbose_name_plural': 'HandymanService',
            },
        ),
        migrations.CreateModel(
            name='Handyman',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('description', models.TextField(verbose_name='Description')),
                ('advantages', models.TextField(verbose_name='Benefits')),
                ('material', models.CharField(max_length=350, verbose_name='Material')),
                ('photo', models.ImageField(default=0, upload_to='handyman_photos/', verbose_name='Photo')),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='Price')),
                ('discount', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='Discount')),
                ('photos', models.ManyToManyField(blank=True, related_name='handyman', to='webapp.handymanphoto')),
            ],
            options={
                'verbose_name': 'Handyman',
                'verbose_name_plural': 'Handyman',
            },
        ),
    ]
