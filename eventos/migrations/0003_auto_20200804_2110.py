# Generated by Django 3.0.6 on 2020-08-05 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0002_auto_20200804_1755'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='imagen',
            field=models.ImageField(upload_to=None),
        ),
    ]