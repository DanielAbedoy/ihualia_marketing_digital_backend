# Generated by Django 3.0.6 on 2020-07-18 21:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cuenta',
            name='tipo',
        ),
        migrations.AlterField(
            model_name='usuario_cuenta',
            name='id_cuenta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='id_cuenta', to='marketing.Cuenta'),
        ),
        migrations.AlterField(
            model_name='usuario_cuenta',
            name='id_usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='id_usuario', to='marketing.Usuario'),
        ),
    ]