# Generated by Django 3.0.6 on 2020-10-31 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0005_auto_20201031_1000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lugar_evento',
            name='direccion2',
            field=models.CharField(blank=True, default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='lugar_evento',
            name='latitud',
            field=models.CharField(blank=True, default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='lugar_evento',
            name='longitud',
            field=models.CharField(blank=True, default='', max_length=30),
            preserve_default=False,
        ),
    ]
