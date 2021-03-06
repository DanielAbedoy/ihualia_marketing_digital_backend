# Generated by Django 3.0.6 on 2020-06-13 20:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('marketing', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CampoExtra',
            fields=[
                ('nombre', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150)),
                ('correo', models.EmailField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Grupo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150)),
                ('cuenta', models.ForeignKey(default='', on_delete=django.db.models.deletion.DO_NOTHING, related_name='cuenta_del_grupo', to='marketing.Cuenta')),
            ],
            options={
                'ordering': ['cuenta'],
            },
        ),
        migrations.CreateModel(
            name='Grupo_Contacto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contacto', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='contacto_grupo', to='contacto.Contacto')),
                ('grupo', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='grupo_contacto', to='contacto.Grupo')),
            ],
            options={
                'ordering': ['grupo'],
            },
        ),
        migrations.CreateModel(
            name='CampoExtra_Grupo',
            fields=[
                ('clave', models.AutoField(primary_key=True, serialize=False)),
                ('campo_extra', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='campo_grupo', to='contacto.CampoExtra')),
                ('grupo', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='gupo_campo', to='contacto.Grupo')),
            ],
            options={
                'ordering': ['grupo'],
            },
        ),
        migrations.CreateModel(
            name='Campo_Contacto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.CharField(max_length=70)),
                ('campo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contacto.CampoExtra')),
                ('contacto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contacto.Contacto')),
            ],
            options={
                'ordering': ['contacto'],
            },
        ),
    ]
