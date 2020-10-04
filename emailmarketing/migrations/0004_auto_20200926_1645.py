# Generated by Django 3.0.6 on 2020-09-26 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emailmarketing', '0003_boletin_categoria'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='boletin',
            name='categoria',
        ),
        migrations.AddField(
            model_name='plantillaboletin',
            name='categoria',
            field=models.CharField(default='turismo', max_length=100),
            preserve_default=False,
        ),
    ]