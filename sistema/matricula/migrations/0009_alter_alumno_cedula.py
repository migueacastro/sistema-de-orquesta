# Generated by Django 4.2 on 2024-10-08 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matricula', '0008_alter_alumno_fecha_nacimiento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumno',
            name='cedula',
            field=models.CharField(max_length=32, null=True),
        ),
    ]
