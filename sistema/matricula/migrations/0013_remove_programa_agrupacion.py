# Generated by Django 4.2.16 on 2024-11-08 06:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('matricula', '0012_alumno_catedras'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='programa',
            name='agrupacion',
        ),
    ]