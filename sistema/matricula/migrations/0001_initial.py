# Generated by Django 4.2 on 2024-10-06 06:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Accesorio",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(blank=True, max_length=128, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Agrupacion",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(blank=True, max_length=128, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Alergia",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=512)),
                ("descripcion", models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name="Alumno",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=128)),
                ("apellido", models.CharField(max_length=128)),
                ("cedula", models.CharField(max_length=32)),
                ("edad", models.IntegerField()),
                (
                    "sexo",
                    models.CharField(
                        choices=[
                            ("Masculino", "masculino"),
                            ("Femenino", "femenino"),
                            ("Otro", "otro"),
                        ],
                        max_length=32,
                    ),
                ),
                ("telefono", models.CharField(max_length=128)),
                ("fecha_nacimiento", models.DateField(max_length=128)),
                ("direccion", models.CharField(max_length=256)),
                (
                    "alergias",
                    models.ManyToManyField(blank=True, to="matricula.alergia"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="CategoriaInstrumento",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(blank=True, max_length=128, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Color",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(blank=True, max_length=128, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="MarcaInstrumento",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(blank=True, max_length=128, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Medicamento",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(blank=True, max_length=512, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="NivelEstudiantil",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(blank=True, max_length=128, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="NivelTS",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(blank=True, max_length=128, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="QuienRetira",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(blank=True, max_length=64, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Representante",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=128)),
                ("cedula", models.CharField(max_length=32)),
                ("telefono", models.CharField(max_length=128)),
                ("correo", models.EmailField(blank=True, max_length=254, null=True)),
                ("parentesco", models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name="TipoBeca",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(blank=True, max_length=128, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="TipoCatedra",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name="Turno",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(blank=True, max_length=128, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Tratamiento",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(blank=True, max_length=512, null=True)),
                ("description", models.TextField(blank=True, null=True)),
                (
                    "medicamentos",
                    models.ManyToManyField(blank=True, to="matricula.medicamento"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Programa",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=128)),
                (
                    "agrupacion",
                    models.ForeignKey(
                        blank=True,
                        max_length=64,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="matricula.agrupacion",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ModeloInstrumento",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(blank=True, max_length=128, null=True)),
                (
                    "categoria",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="matricula.categoriainstrumento",
                    ),
                ),
                (
                    "marca",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="matricula.marcainstrumento",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Instrumento",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(blank=True, max_length=128, null=True)),
                ("serial", models.CharField(blank=True, max_length=128, null=True)),
                (
                    "asignado",
                    models.CharField(
                        blank=True,
                        choices=[("Asignado", "asignado"), ("Propio", "propio")],
                        max_length=128,
                        null=True,
                    ),
                ),
                (
                    "accesorio",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="matricula.accesorio",
                    ),
                ),
                (
                    "color",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="matricula.color",
                    ),
                ),
                (
                    "modelo",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="matricula.modeloinstrumento",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Inscripcion",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("fecha_inscrpcion", models.DateField(max_length=128)),
                (
                    "alumno",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="matricula.alumno",
                    ),
                ),
                (
                    "turno",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="matricula.turno",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="CondicionEspecial",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(blank=True, max_length=128, null=True)),
                (
                    "tratamiento",
                    models.ManyToManyField(blank=True, to="matricula.tratamiento"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Catedra",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=128)),
                (
                    "instrumento",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="matricula.instrumento",
                    ),
                ),
                (
                    "tipo",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="matricula.tipocatedra",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Becado",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "alumno",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="matricula.alumno",
                    ),
                ),
                (
                    "tipo",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="matricula.tipobeca",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="alumno",
            name="instrumentos",
            field=models.ManyToManyField(blank=True, to="matricula.instrumento"),
        ),
        migrations.AddField(
            model_name="alumno",
            name="nivel_estudiantil",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="matricula.nivelestudiantil",
            ),
        ),
        migrations.AddField(
            model_name="alumno",
            name="nivel_ts",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="matricula.nivelts",
            ),
        ),
        migrations.AddField(
            model_name="alumno",
            name="programa",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="matricula.programa",
            ),
        ),
        migrations.AddField(
            model_name="alumno",
            name="quien_retiras",
            field=models.ManyToManyField(blank=True, to="matricula.quienretira"),
        ),
        migrations.AddField(
            model_name="alumno",
            name="representantes",
            field=models.ManyToManyField(blank=True, to="matricula.representante"),
        ),
        migrations.AddField(
            model_name="alumno",
            name="tratamientos",
            field=models.ManyToManyField(blank=True, to="matricula.tratamiento"),
        ),
        migrations.AddField(
            model_name="alumno",
            name="turno",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="matricula.turno",
            ),
        ),
        migrations.AddField(
            model_name="agrupacion",
            name="instrumentos",
            field=models.ManyToManyField(blank=True, to="matricula.instrumento"),
        ),
    ]