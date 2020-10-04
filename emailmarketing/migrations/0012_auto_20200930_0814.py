# Generated by Django 3.0.6 on 2020-09-30 13:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('emailmarketing', '0011_boletin_id_cuenta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fechahorapublicacionboletin',
            name='ids_grupos',
            field=models.TextField(),
        ),
        migrations.CreateModel(
            name='EnvioBoletin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ids_contactos', models.TextField()),
                ('id_boletin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='envio_boletin', to='emailmarketing.Boletin')),
            ],
        ),
    ]
