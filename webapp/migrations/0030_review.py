# Generated by Django 4.2.4 on 2023-11-04 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0029_order_order_month'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('text', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('rating', models.PositiveIntegerField(default=5)),
                ('approved', models.BooleanField(default=False)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='review_photos/')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
