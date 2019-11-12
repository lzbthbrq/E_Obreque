# Generated by Django 2.2.5 on 2019-11-12 02:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('entradas', '0014_auto_20191111_1925'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artistas',
            name='gen',
        ),
        migrations.AddField(
            model_name='artistas',
            name='gen',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='entradas.Genero'),
        ),
        migrations.AlterField(
            model_name='artistas',
            name='nombre',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]