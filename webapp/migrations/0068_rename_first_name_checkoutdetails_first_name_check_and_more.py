# Generated by Django 4.2.4 on 2024-03-15 14:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0067_remove_checkoutdetails_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='checkoutdetails',
            old_name='first_name',
            new_name='first_name_check',
        ),
        migrations.RenameField(
            model_name='checkoutdetails',
            old_name='last_name',
            new_name='last_name_check',
        ),
        migrations.RenameField(
            model_name='checkoutdetails',
            old_name='price',
            new_name='price_check',
        ),
    ]
