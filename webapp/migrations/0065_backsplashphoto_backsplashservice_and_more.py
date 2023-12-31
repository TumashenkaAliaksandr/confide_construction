# Generated by Django 4.2.4 on 2023-12-26 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0064_rename_profile_pic_profile_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='BacksplashPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(default=0, upload_to='backsplash_photos/', verbose_name='Photo')),
            ],
            options={
                'verbose_name': 'Photo for Backsplash',
                'verbose_name_plural': 'Photos for Backsplash',
            },
        ),
        migrations.CreateModel(
            name='BacksplashService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('description', models.TextField(verbose_name='Description')),
                ('photo', models.ImageField(upload_to='backsplashservice_photos/', verbose_name='Photo')),
            ],
            options={
                'verbose_name': 'BacksplashService',
                'verbose_name_plural': 'BacksplashService',
            },
        ),
        migrations.AlterField(
            model_name='backsplash',
            name='material',
            field=models.CharField(max_length=350, verbose_name='Material'),
        ),
        migrations.AlterField(
            model_name='backsplash',
            name='photo',
            field=models.ImageField(default=0, upload_to='backsplash_photos/', verbose_name='Photo'),
        ),
        migrations.AddField(
            model_name='backsplash',
            name='photos',
            field=models.ManyToManyField(blank=True, related_name='backsplash', to='webapp.backsplashphoto'),
        ),
    ]
