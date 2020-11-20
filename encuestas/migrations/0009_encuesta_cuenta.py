# Generated by Django 3.0.6 on 2020-11-15 17:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0001_initial'),
        ('encuestas', '0008_auto_20201115_0923'),
    ]

    operations = [
        migrations.AddField(
            model_name='encuesta',
            name='cuenta',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='encuestas', to='marketing.Cuenta'),
            preserve_default=False,
        ),
    ]