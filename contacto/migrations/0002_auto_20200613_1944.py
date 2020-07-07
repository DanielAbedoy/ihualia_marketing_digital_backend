# Generated by Django 3.0.6 on 2020-06-14 00:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contacto', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campoextra_grupo',
            name='campo_extra',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='campo_grupo', to='contacto.CampoExtra'),
        ),
        migrations.AlterField(
            model_name='campoextra_grupo',
            name='grupo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gupo_campo', to='contacto.Grupo'),
        ),
    ]
