# Generated by Django 2.2.5 on 2019-11-06 05:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entradas', '0008_auto_20191106_0159'),
    ]

    operations = [
        migrations.RenameField(
            model_name='genero',
            old_name='nomg',
            new_name='nombre',
        ),
    ]
