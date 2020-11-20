# Generated by Django 3.0.6 on 2020-11-16 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('encuestas', '0009_encuesta_cuenta'),
    ]

    operations = [
        migrations.CreateModel(
            name='Encuestado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=100)),
                ('correo', models.CharField(blank=True, max_length=100)),
                ('respouesta_json', models.TextField()),
            ],
        ),
    ]
