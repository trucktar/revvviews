# Generated by Django 3.0.8 on 2020-07-12 15:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='review',
            name='content',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='review',
            name='design',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='review',
            name='usability',
            field=models.PositiveSmallIntegerField(),
        ),
    ]
