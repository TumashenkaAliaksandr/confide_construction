# Generated by Django 4.2.4 on 2023-11-26 18:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0051_alter_userprofile_options_remove_userprofile_email_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userprofile',
            options={'verbose_name': 'Users', 'verbose_name_plural': 'Users'},
        ),
    ]