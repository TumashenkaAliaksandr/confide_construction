# Generated by Django 4.2.4 on 2025-03-13 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0118_orderconsultations_uploaded_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=30, verbose_name='Фамилия')),
                ('zip_code', models.CharField(max_length=10, verbose_name='Почтовый индекс')),
                ('job_description', models.TextField(verbose_name='Описание работы')),
                ('hours_needed', models.IntegerField(verbose_name='Количество часов')),
                ('appointment_date', models.DateField(verbose_name='Дата визита')),
                ('appointment_time', models.TimeField(verbose_name='Время визита')),
                ('email', models.EmailField(max_length=254, verbose_name='Электронная почта')),
                ('phone_number', models.CharField(max_length=15, verbose_name='Телефон')),
                ('photo', models.ImageField(upload_to='photos/', verbose_name='Фото')),
            ],
        ),
    ]
