# Generated by Django 2.2.5 on 2019-11-08 02:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('entradas', '0010_auto_20191106_2004'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artistas',
            name='gen',
        ),
        migrations.AddField(
            model_name='artistas',
            name='gen',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='entradas.Genero'),
        ),
        migrations.AlterField(
            model_name='suscriptor',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]