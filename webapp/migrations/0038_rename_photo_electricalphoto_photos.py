# Generated by Django 4.2.4 on 2023-11-06 09:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0037_electricalphoto_alter_electrical_material_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='electricalphoto',
            old_name='photo',
            new_name='photos',
        ),
    ]