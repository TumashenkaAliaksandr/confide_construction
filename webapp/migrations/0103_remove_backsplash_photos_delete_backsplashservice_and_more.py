# Generated by Django 4.2.4 on 2024-12-09 12:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0102_rename_product_content_type_id_checkoutdetails_product_content_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='backsplash',
            name='photos',
        ),
        migrations.DeleteModel(
            name='BacksplashService',
        ),
        migrations.RemoveField(
            model_name='ceilingfan',
            name='photos',
        ),
        migrations.RemoveField(
            model_name='disposal',
            name='photos',
        ),
        migrations.DeleteModel(
            name='DisposalService',
        ),
        migrations.RemoveField(
            model_name='drywall',
            name='photos',
        ),
        migrations.DeleteModel(
            name='DrywallService',
        ),
        migrations.RemoveField(
            model_name='electrical',
            name='photos',
        ),
        migrations.DeleteModel(
            name='ElectricalService',
        ),
        migrations.RemoveField(
            model_name='furniture',
            name='photos',
        ),
        migrations.DeleteModel(
            name='FurnitureService',
        ),
        migrations.RemoveField(
            model_name='handyman',
            name='photos',
        ),
        migrations.DeleteModel(
            name='HandymanService',
        ),
        migrations.RemoveField(
            model_name='painting',
            name='photos',
        ),
        migrations.DeleteModel(
            name='PaintingService',
        ),
        migrations.RemoveField(
            model_name='soundproofing',
            name='photos',
        ),
        migrations.DeleteModel(
            name='SoundproofingService',
        ),
        migrations.RemoveField(
            model_name='tvmount',
            name='photos',
        ),
        migrations.RemoveField(
            model_name='wallpaper',
            name='photos',
        ),
        migrations.DeleteModel(
            name='WallpaperService',
        ),
        migrations.DeleteModel(
            name='Backsplash',
        ),
        migrations.DeleteModel(
            name='BacksplashPhoto',
        ),
        migrations.DeleteModel(
            name='CeilingFan',
        ),
        migrations.DeleteModel(
            name='CeilingFanPhoto',
        ),
        migrations.DeleteModel(
            name='Disposal',
        ),
        migrations.DeleteModel(
            name='DisposalPhoto',
        ),
        migrations.DeleteModel(
            name='Drywall',
        ),
        migrations.DeleteModel(
            name='DrywallPhoto',
        ),
        migrations.DeleteModel(
            name='Electrical',
        ),
        migrations.DeleteModel(
            name='ElectricalPhoto',
        ),
        migrations.DeleteModel(
            name='Furniture',
        ),
        migrations.DeleteModel(
            name='FurniturePhoto',
        ),
        migrations.DeleteModel(
            name='Handyman',
        ),
        migrations.DeleteModel(
            name='HandymanPhoto',
        ),
        migrations.DeleteModel(
            name='Painting',
        ),
        migrations.DeleteModel(
            name='PaintingPhoto',
        ),
        migrations.DeleteModel(
            name='Soundproofing',
        ),
        migrations.DeleteModel(
            name='SoundproofingPhoto',
        ),
        migrations.DeleteModel(
            name='TVMount',
        ),
        migrations.DeleteModel(
            name='TvMountPhoto',
        ),
        migrations.DeleteModel(
            name='Wallpaper',
        ),
        migrations.DeleteModel(
            name='WallpaperPhoto',
        ),
    ]