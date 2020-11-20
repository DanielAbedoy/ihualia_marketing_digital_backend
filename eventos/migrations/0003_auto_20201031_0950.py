# Generated by Django 3.0.6 on 2020-10-31 15:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0002_auto_20201031_0853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asistente_evento',
            name='id_evento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='asistentes', to='eventos.Evento'),
        ),
        migrations.AlterField(
            model_name='boleto_evento',
            name='id_evento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='boletos', to='eventos.Evento'),
        ),
        migrations.AlterField(
            model_name='componente',
            name='id_evento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='componentes', to='eventos.Evento'),
        ),
        migrations.AlterField(
            model_name='detalles_oxxopay_evento',
            name='id_asistencia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='detalles_oxxo', to='eventos.Asistente_Evento'),
        ),
        migrations.AlterField(
            model_name='detalles_pagotarjeta_evento',
            name='id_asistencia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='detalles_card', to='eventos.Asistente_Evento'),
        ),
        migrations.AlterField(
            model_name='donacion_asistente_evento',
            name='id_asistencia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='donacion', to='eventos.Asistente_Evento'),
        ),
        migrations.AlterField(
            model_name='evento',
            name='fecha_hora_fin',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='evento',
            name='fecha_hora_inicio',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='evento',
            name='resumen',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='evento',
            name='tipo_ubicacion',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AlterField(
            model_name='lugar_evento',
            name='id_evento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lugar', to='eventos.Evento'),
        ),
        migrations.AlterField(
            model_name='online_evento',
            name='id_evento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sitio', to='eventos.Evento'),
        ),
        migrations.AlterField(
            model_name='tags_evento',
            name='id_evento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='etiquetas', to='eventos.Evento'),
        ),
    ]