# Generated by Django 4.2.4 on 2023-09-29 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0015_alter_servicesslider_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicesslider',
            name='name',
            field=models.CharField(default=2, max_length=100, verbose_name='name'),
            preserve_default=False,
        ),
    ]