# Generated by Django 3.0.6 on 2020-08-08 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0004_auto_20200804_2142'),
    ]

    operations = [
        migrations.RenameField(
            model_name='imagen_evento',
            old_name='imagen',
            new_name='directorio_imagen',
        ),
        migrations.RemoveField(
            model_name='evento',
            name='imagen',
        ),
        migrations.AddField(
            model_name='evento',
            name='diretorio_imagen',
            field=models.CharField(default=-1, max_length=2000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='evento',
            name='nombre_imagen',
            field=models.CharField(default=-1, max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='imagen_evento',
            name='nombre_imagen',
            field=models.CharField(default=-1, max_length=500),
            preserve_default=False,
        ),
    ]