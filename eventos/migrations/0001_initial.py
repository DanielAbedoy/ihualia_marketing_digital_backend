# Generated by Django 3.0.6 on 2020-10-29 02:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('marketing', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asistente_Evento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('correo', models.EmailField(max_length=100)),
                ('nombre', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=20)),
                ('metodo_pago', models.CharField(max_length=20)),
                ('monto_total', models.CharField(max_length=10)),
                ('estatus_pago', models.CharField(max_length=40)),
                ('fecha_agrgado', models.DateTimeField(auto_now_add=True)),
                ('fecha_actualizado', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('tipo', models.CharField(max_length=100)),
                ('categoria', models.CharField(max_length=70)),
                ('sub_categoria', models.CharField(max_length=70)),
                ('tipo_ubicacion', models.CharField(max_length=15)),
                ('fecha_hora_inicio', models.DateTimeField()),
                ('fecha_hora_fin', models.DateTimeField()),
                ('zona_horaria', models.CharField(max_length=100)),
                ('directorio_imagen', models.CharField(max_length=10)),
                ('resumen', models.CharField(max_length=1000)),
                ('estatus', models.CharField(max_length=50)),
                ('id_cuenta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='evento_cuenta', to='marketing.Cuenta')),
            ],
        ),
        migrations.CreateModel(
            name='ImagenPrincipal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cliente', models.CharField(max_length=10)),
                ('cuenta', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Video_Evento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=260)),
                ('posicion', models.IntegerField()),
                ('id_evento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='video_evento', to='eventos.Evento')),
            ],
        ),
        migrations.CreateModel(
            name='Tags_Evento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('palabra', models.CharField(max_length=30)),
                ('id_evento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tags_evento', to='eventos.Evento')),
            ],
        ),
        migrations.CreateModel(
            name='Parrafo_Evento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parrafo', models.CharField(max_length=560)),
                ('posicion', models.IntegerField()),
                ('id_evento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parrafo_evento', to='eventos.Evento')),
            ],
        ),
        migrations.CreateModel(
            name='Online_Evento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=200)),
                ('id_evento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='online_evento', to='eventos.Evento')),
            ],
        ),
        migrations.CreateModel(
            name='Lugar_Evento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direccion1', models.CharField(max_length=200)),
                ('direccion2', models.CharField(max_length=200, null=True)),
                ('ciudad', models.CharField(max_length=60)),
                ('estado', models.CharField(max_length=60)),
                ('codigo_postal', models.CharField(max_length=20)),
                ('pais', models.CharField(max_length=100)),
                ('latitud', models.CharField(max_length=30, null=True)),
                ('longitud', models.CharField(max_length=30, null=True)),
                ('id_evento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lugar_evento', to='eventos.Evento')),
            ],
        ),
        migrations.CreateModel(
            name='Imagen_Evento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_imagen', models.CharField(max_length=500)),
                ('posicion', models.IntegerField()),
                ('id_evento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='imagen_evento', to='eventos.Evento')),
            ],
        ),
        migrations.CreateModel(
            name='Donacion_Asistente_Evento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monto', models.CharField(max_length=10)),
                ('id_asistencia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='donacion_asistente', to='eventos.Asistente_Evento')),
            ],
        ),
        migrations.CreateModel(
            name='Detalles_PagoTarjeta_Evento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_pago', models.CharField(max_length=60)),
                ('id_orden', models.CharField(max_length=30)),
                ('id_asistencia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cardDetailspay_asistente', to='eventos.Asistente_Evento')),
            ],
        ),
        migrations.CreateModel(
            name='Detalles_OxxoPay_Evento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_referencia', models.CharField(max_length=20)),
                ('id_asistencia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='oxxoDetails_asistente', to='eventos.Asistente_Evento')),
            ],
        ),
        migrations.CreateModel(
            name='Boleto_Evento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=50)),
                ('nombre', models.CharField(max_length=200)),
                ('cantida_total', models.CharField(max_length=20)),
                ('precio', models.CharField(max_length=20)),
                ('descripcion', models.CharField(max_length=250)),
                ('cantidad_minima', models.CharField(max_length=20)),
                ('cantidad_maxima', models.CharField(max_length=20)),
                ('canal_ventas', models.CharField(max_length=50)),
                ('id_evento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='boleto_evento', to='eventos.Evento')),
            ],
        ),
        migrations.CreateModel(
            name='Boleto_AsistenteEvento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.CharField(max_length=10)),
                ('id_asistencia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='boleto_asistente', to='eventos.Asistente_Evento')),
                ('id_boleto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='boleto_item', to='eventos.Boleto_Evento')),
            ],
        ),
        migrations.AddField(
            model_name='asistente_evento',
            name='id_evento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='asistente_evento', to='eventos.Evento'),
        ),
    ]
