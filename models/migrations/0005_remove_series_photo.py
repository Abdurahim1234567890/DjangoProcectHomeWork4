# Generated by Django 4.1.1 on 2022-09-27 12:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0004_series_engine_series_hp_series_nm_series_photo_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='series',
            name='photo',
        ),
    ]
