# Generated by Django 4.2.16 on 2024-11-08 03:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('matricula', '0010_accesorio_activo_agrupacion_activo_alergia_activo_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumno',
            name='condicion_especial',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='matricula.condicionespecial'),
        ),
    ]