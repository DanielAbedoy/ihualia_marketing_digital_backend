# Generated by Django 3.0.6 on 2020-10-17 03:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0017_imagenprincipal'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imagenprincipal',
            name='cliente',
        ),
        migrations.RemoveField(
            model_name='imagenprincipal',
            name='cuenta',
        ),
    ]
