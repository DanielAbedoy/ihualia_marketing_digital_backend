# Generated by Django 3.0.6 on 2020-09-26 18:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emailmarketing', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='boletin',
            old_name='constenido',
            new_name='contenido',
        ),
    ]
