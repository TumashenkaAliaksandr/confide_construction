# Generated by Django 4.2.4 on 2024-11-17 07:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('webapp', '0081_alter_checkoutdetails_product_content_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkoutdetails',
            name='product_content_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype'),
        ),
        migrations.AlterField(
            model_name='checkoutdetails',
            name='product_object_id',
            field=models.PositiveIntegerField(),
        ),
    ]