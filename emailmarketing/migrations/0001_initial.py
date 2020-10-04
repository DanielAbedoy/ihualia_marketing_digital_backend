# Generated by Django 3.0.6 on 2020-09-26 03:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contacto', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Boletin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asunto', models.CharField(max_length=500)),
                ('tipo_publicacion', models.CharField(max_length=20)),
                ('constenido', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ImagenBoletin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('cuenta', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='LinkBoletin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='PlantillaBoletin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contenido', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='GrupoEnvioBoletin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_boletin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='boletin_grupo', to='emailmarketing.Boletin')),
                ('id_grupo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='grupo_boletin', to='contacto.Grupo')),
            ],
        ),
        migrations.CreateModel(
            name='FechaHoraPublicacionBoletin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.CharField(max_length=20)),
                ('hora', models.CharField(max_length=10)),
                ('id_boletin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fecha_boletin', to='emailmarketing.Boletin')),
            ],
        ),
        migrations.CreateModel(
            name='ContactoLinkBoletin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estatus', models.CharField(max_length=20)),
                ('id_contacto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contacto_link', to='contacto.Contacto')),
                ('id_link', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='link_contacto', to='emailmarketing.LinkBoletin')),
            ],
        ),
    ]
