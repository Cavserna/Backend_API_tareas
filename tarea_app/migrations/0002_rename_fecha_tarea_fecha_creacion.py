# Generated by Django 5.0.6 on 2024-05-31 13:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tarea_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tarea',
            old_name='fecha',
            new_name='fecha_creacion',
        ),
    ]