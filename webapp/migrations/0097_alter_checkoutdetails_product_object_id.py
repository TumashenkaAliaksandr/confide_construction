# Generated by Django 4.2.4 on 2024-12-04 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0096_alter_product_discount_alter_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkoutdetails',
            name='product_object_id',
            field=models.PositiveIntegerField(),
        ),
    ]
