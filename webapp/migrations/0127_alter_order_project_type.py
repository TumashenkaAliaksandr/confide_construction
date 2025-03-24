# Generated by Django 4.2.4 on 2025-03-22 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0126_alter_checkoutdetails_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='project_type',
            field=models.CharField(blank=True, choices=[('single_project', 'Единичный проект'), ('variety_of_projects', 'Несколько проектов')], max_length=20, null=True, verbose_name='Тип проекта'),
        ),
    ]
