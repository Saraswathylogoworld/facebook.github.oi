# Generated by Django 4.0 on 2022-02-08 05:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fbloginapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='freg',
            old_name='day',
            new_name='date',
        ),
    ]
