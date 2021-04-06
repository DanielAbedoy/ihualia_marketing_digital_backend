# Generated by Django 3.0.6 on 2020-12-03 21:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('marketing', '0001_initial'),
        ('contacto', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Boletin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asunto', models.CharField(max_length=500)),
                ('publicacion', models.CharField(max_length=500)),
                ('contenido', models.TextField(blank=True)),
                ('estatus', models.CharField(blank=True, max_length=30)),
                ('fecha_creado', models.DateField(auto_now=True)),
                ('links', models.TextField(blank=True)),
                ('enviados', models.TextField(blank=True)),
                ('grupos', models.ManyToManyField(blank=True, related_name='boletines', to='contacto.Grupo')),
                ('id_cuenta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='boletin_cuenta', to='marketing.Cuenta')),
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
            name='SeenLinkBoletin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_link', models.CharField(max_length=10)),
                ('fecha_visto', models.DateTimeField(auto_now_add=True)),
                ('boletin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='links_vistos', to='emailmarketing.Boletin')),
                ('id_contacto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contactolink_seen', to='contacto.Contacto')),
            ],
        ),
        migrations.CreateModel(
            name='SeenContactoBoletin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_visto', models.DateTimeField(auto_now_add=True)),
                ('id_boletin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contactos_vistos', to='emailmarketing.Boletin')),
                ('id_contacto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contacto_seen', to='contacto.Contacto')),
            ],
        ),
    ]
