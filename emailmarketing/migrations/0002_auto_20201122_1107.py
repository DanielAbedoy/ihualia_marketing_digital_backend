# Generated by Django 3.0.6 on 2020-11-22 17:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contacto', '0004_auto_20201031_0853'),
        ('emailmarketing', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='envioboletin',
            name='id_boletin',
        ),
        migrations.RemoveField(
            model_name='fechahorapublicacionboletin',
            name='id_boletin',
        ),
        migrations.RemoveField(
            model_name='grupoenvioboletin',
            name='id_boletin',
        ),
        migrations.RemoveField(
            model_name='grupoenvioboletin',
            name='id_grupo',
        ),
        migrations.RemoveField(
            model_name='linkboletin',
            name='id_boletin',
        ),
        migrations.DeleteModel(
            name='PlantillaBoletin',
        ),
        migrations.RemoveField(
            model_name='boletin',
            name='tipo_publicacion',
        ),
        migrations.AddField(
            model_name='boletin',
            name='enviados',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='boletin',
            name='grupos',
            field=models.ManyToManyField(blank=True, related_name='boletines', to='contacto.Grupo'),
        ),
        migrations.AddField(
            model_name='boletin',
            name='links',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='boletin',
            name='publicacion',
            field=models.CharField(default='', max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='seenlinkboletin',
            name='boletin',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='vistos_links', to='emailmarketing.Boletin'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='seenlinkboletin',
            name='id_link',
            field=models.CharField(max_length=10),
        ),
        migrations.DeleteModel(
            name='EnvioBoletin',
        ),
        migrations.DeleteModel(
            name='FechaHoraPublicacionBoletin',
        ),
        migrations.DeleteModel(
            name='GrupoEnvioBoletin',
        ),
        migrations.DeleteModel(
            name='LinkBoletin',
        ),
    ]
