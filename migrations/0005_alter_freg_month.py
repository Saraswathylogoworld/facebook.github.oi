# Generated by Django 4.0 on 2022-02-09 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fbloginapp', '0004_alter_freg_month'),
    ]

    operations = [
        migrations.AlterField(
            model_name='freg',
            name='month',
            field=models.IntegerField(null=True),
        ),
    ]
