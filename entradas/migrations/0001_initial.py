# Generated by Django 2.2.6 on 2019-10-17 14:18

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artistas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('discos', models.IntegerField()),
                ('fundacion', models.DateField(blank=True, null=True)),
                ('n_integrantes', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomg', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Suscriptor',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='id unico del subscriptor', primary_key=True, serialize=False)),
                ('nickname', models.CharField(max_length=200)),
                ('nombre', models.CharField(max_length=200)),
                ('apellido', models.CharField(max_length=200)),
                ('correo', models.CharField(max_length=200)),
                ('f_nacimiento', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Entradas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artista', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='entradas.Artistas')),
            ],
        ),
        migrations.CreateModel(
            name='Conciertos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_concierto', models.DateField(blank=True, null=True)),
                ('lugar', models.CharField(max_length=200)),
                ('artista', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='entradas.Artistas')),
            ],
        ),
        migrations.AddField(
            model_name='artistas',
            name='genero',
            field=models.ManyToManyField(to='entradas.Genero'),
        ),
    ]
