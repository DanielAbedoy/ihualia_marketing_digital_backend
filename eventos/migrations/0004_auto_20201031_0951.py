# Generated by Django 3.0.6 on 2020-10-31 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0003_auto_20201031_0950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='zona_horaria',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]