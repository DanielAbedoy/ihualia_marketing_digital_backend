# Generated by Django 3.0.6 on 2020-08-22 02:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0012_asistente_evento_boleto_asistenteevento_detalles_oxxopay_evento_detalles_pagotarjeta_evento'),
    ]

    operations = [
        migrations.CreateModel(
            name='Donacion_Asistente_Evento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monto', models.CharField(max_length=10)),
                ('id_asistencia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='donacion_asistente', to='eventos.Asistente_Evento')),
            ],
        ),
    ]