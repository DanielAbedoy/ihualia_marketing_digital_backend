# Generated by Django 3.0.6 on 2020-11-14 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('encuestas', '0004_encuesta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='encuesta',
            name='anonima',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='encuesta',
            name='despedida',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='encuesta',
            name='imagen',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='encuesta',
            name='paginacion',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='encuesta',
            name='poderacion',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='encuesta',
            name='preguntas_json',
            field=models.TextField(blank=True),
        ),
    ]