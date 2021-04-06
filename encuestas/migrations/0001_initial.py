# Generated by Django 3.0.6 on 2020-12-03 21:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('marketing', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Encuesta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=35)),
                ('presentacion', models.CharField(max_length=1000)),
                ('instrucciones', models.CharField(max_length=1000)),
                ('imagen', models.CharField(blank=True, max_length=10)),
                ('anonima', models.BooleanField(null=True)),
                ('ponderacion', models.BooleanField(null=True)),
                ('paginacion', models.CharField(blank=True, max_length=10)),
                ('preguntas_json', models.TextField(blank=True)),
                ('despedida', models.CharField(blank=True, max_length=1000)),
                ('estatus', models.CharField(max_length=20)),
                ('url', models.CharField(blank=True, max_length=100)),
                ('cuenta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='encuestas', to='marketing.Cuenta')),
            ],
        ),
        migrations.CreateModel(
            name='Imagen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('encuesta', models.CharField(max_length=10)),
                ('nombre', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Encuestado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=100)),
                ('correo', models.CharField(blank=True, max_length=100)),
                ('respuestas_json', models.TextField()),
                ('creado', models.DateField(auto_now_add=True)),
                ('encuesta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='encuestados', to='encuestas.Encuesta')),
            ],
        ),
    ]
