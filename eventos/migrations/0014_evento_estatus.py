# Generated by Django 3.0.6 on 2020-09-10 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0013_donacion_asistente_evento'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='estatus',
            field=models.CharField(default='completo', max_length=50),
            preserve_default=False,
        ),
    ]