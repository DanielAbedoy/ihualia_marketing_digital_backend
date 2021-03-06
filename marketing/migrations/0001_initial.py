# Generated by Django 3.0.6 on 2020-06-13 20:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('correo', models.EmailField(max_length=100, primary_key=True, serialize=False)),
                ('usuario', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=20)),
                ('nombre', models.CharField(max_length=100)),
                ('razon_social', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=250)),
                ('telefono', models.CharField(max_length=30)),
                ('dominio', models.URLField(max_length=100)),
                ('giro', models.CharField(max_length=150)),
                ('imagen', models.CharField(max_length=100)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('editado', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cuenta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('tipo', models.CharField(max_length=200)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usuario_de_cuenta', to='marketing.Usuario')),
            ],
            options={
                'ordering': ['usuario'],
            },
        ),
    ]
