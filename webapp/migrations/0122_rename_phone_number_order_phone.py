# Generated by Django 4.2.4 on 2025-03-14 13:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0121_remove_order_last_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='phone_number',
            new_name='phone',
        ),
    ]
