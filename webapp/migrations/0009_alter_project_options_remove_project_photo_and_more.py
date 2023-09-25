# Generated by Django 4.2.4 on 2023-09-25 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0008_project_alter_recommended_image_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'verbose_name': 'Project', 'verbose_name_plural': 'Project'},
        ),
        migrations.RemoveField(
            model_name='project',
            name='photo',
        ),
        migrations.AddField(
            model_name='project',
            name='image',
            field=models.ImageField(default=2, upload_to='projects', verbose_name='photo'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(verbose_name='descriptions'),
        ),
        migrations.AlterField(
            model_name='project',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='data'),
        ),
        migrations.AlterField(
            model_name='project',
            name='title',
            field=models.CharField(max_length=200, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='recommended',
            name='image',
            field=models.ImageField(upload_to='recommended', verbose_name='photo'),
        ),
        migrations.AlterField(
            model_name='recommended',
            name='name',
            field=models.CharField(max_length=100, verbose_name='name'),
        ),
    ]
