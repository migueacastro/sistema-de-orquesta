# Generated by Django 4.2 on 2024-10-06 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("matricula", "0006_rename_fecha_inscrpcion_inscripcion_fecha_inscripcion"),
    ]

    operations = [
        migrations.AlterField(
            model_name="inscripcion",
            name="fecha_inscripcion",
            field=models.DateField(blank=True, max_length=128, null=True),
        ),
    ]
