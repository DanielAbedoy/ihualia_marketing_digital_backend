# Generated by Django 3.0.6 on 2020-10-17 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0016_auto_20200912_1013'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImagenPrincipal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cliente', models.CharField(max_length=10)),
                ('cuenta', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=500)),
            ],
        ),
    ]
