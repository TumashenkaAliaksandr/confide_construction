# Generated by Django 4.2.4 on 2024-12-03 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0092_alter_checkoutdetails_product_object_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='flag_1',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='flag_2',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='flag_3',
            field=models.BooleanField(default=False),
        ),
    ]
