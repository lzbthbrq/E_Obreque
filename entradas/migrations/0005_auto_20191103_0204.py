# Generated by Django 2.2.5 on 2019-11-03 05:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('entradas', '0004_auto_20191102_2243'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artistas',
            name='genero',
        ),
        migrations.AddField(
            model_name='artistas',
            name='genero',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='entradas.Genero'),
        ),
    ]
