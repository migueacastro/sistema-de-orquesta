# Generated by Django 4.2 on 2024-10-06 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("matricula", "0007_alter_inscripcion_fecha_inscripcion"),
    ]

    operations = [
        migrations.AlterField(
            model_name="alumno",
            name="fecha_nacimiento",
            field=models.DateField(blank=True, max_length=128, null=True),
        ),
    ]
