# Generated by Django 4.2.4 on 2023-11-05 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0031_remove_review_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
    ]
