# Generated by Django 4.2.4 on 2025-01-30 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0108_invoice'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='invoice_link',
            field=models.URLField(blank=True, null=True),
        ),
    ]
