# Generated by Django 4.2.4 on 2025-03-24 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0128_alter_order_project_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='subcategories',
        ),
        migrations.AddField(
            model_name='order',
            name='subcategories',
            field=models.ManyToManyField(blank=True, to='webapp.subcategory', verbose_name='Выбранные подкатегории'),
        ),
    ]
