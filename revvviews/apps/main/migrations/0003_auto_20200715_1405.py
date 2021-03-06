# Generated by Django 3.0.8 on 2020-07-15 11:05

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20200712_1821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='avatar'),
        ),
        migrations.AlterField(
            model_name='project',
            name='screenshot',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='screenshot'),
        ),
    ]
