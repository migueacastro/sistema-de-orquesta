from django.db import models

# Create your models here.



class Medicamento(models.Model):
    nombre = models.CharField(max_length=512, blank=True, null=True)

class Tratamiento(models.Model):
    nombre = models.CharField(max_length=512, blank=True, null=True)
    description = models.TextField(blank=True)
    medicamentos = models.ManyToManyField(Medicamento, blank=True)

class CondicionEspecial(models.Model):
    nombre = models.CharField(max_length=128, blank=True, null=True)
    tratamiento = models.ManyToManyField(Tratamiento, blank=True)

class TipoAlergia(models.Model):
    nombre = models.CharField(max_length=128, blank=True, null=True)

class Alergia(models.Model):
    nombre = models.CharField(max_length=512)
    descripcion = models.TextField(blank=True)
    tipo = models.ForeignKey(TipoAlergia, null=True, on_delete=models.CASCADE)

class Color(models.Model):
    nombre = models.CharField(max_length=128, blank=True, null=True)

class CategoriaInstrumento(models.Model):
    nombre = models.CharField(max_length=128, blank=True, null=True)

class MarcaInstrumento(models.Model):
    nombre = models.CharField(max_length=128, blank=True, null=True)

class ModeloInstrumento(models.Model):
    nombre = models.CharField(max_length=128, blank=True, null=True)
    marca = models.ForeignKey(MarcaInstrumento, null=True, on_delete=models.CASCADE)
    categoria = models.ForeignKey(CategoriaInstrumento, null=True, on_delete=models.CASCADE)

class Accesorio(models.Model):
    nombre = models.CharField(max_length=128, blank=True, null=True)

class Instrumento(models.Model):
    nombre = models.CharField(max_length=128, blank=True, null=True)
    serial = models.CharField(max_length=128, blank=True, null=True)
    modelo = models.ForeignKey(ModeloInstrumento, null=True, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, null=True, on_delete=models.CASCADE)
    accesorio = models.ForeignKey(Accesorio, null=True, blank=True, on_delete=models.CASCADE)
    asignado = models.CharField(max_length=128, choices=(
        ('Asignado', 'asignado'),
        ('Propio', 'propio')
    ))

class Agrupacion(models.Model):
    nombre = models.CharField(max_length=128, blank=True, null=True)
    instrumentos = models.ManyToManyField(Instrumento, blank=True)

class Turno (models.Model):
    nombre = models.CharField(max_length=128, blank=True, null=True)

class NivelTS (models.Model):
    nombre = models.CharField(max_length=128, blank=True, null=True)

class NivelEstudiantil (models.Model):
    nombre = models.CharField(max_length=128, blank=True, null=True)

class TipoBeca(models.Model):
    nombre = models.CharField(max_length=128, blank=True, null=True)

class Representante(models.Model):
    nombre = models.CharField(max_length=128)
    cedula = models.CharField(max_length=32)
    telefono = models.CharField(max_length=128)
    correo = models.EmailField()
    parentesco = models.CharField(max_length=128)

class Alumno(models.Model):
    nombre = models.CharField(max_length=128)
    ellido = models.CharField(max_length=128)
    cedula = models.CharField(max_length=32)
    edad = models.IntegerField()
    turno = models.ForeignKey(Turno, blank=True, on_delete=models.DO_NOTHING, null=True)
    instrumentos = models.ManyToManyField(Instrumento, blank=True)
    # TODO para Cris: Agregar choices
    sexo = models.CharField(max_length=32, choices=(
        ('Masculino', 'masculino'),
        ('Femenino', 'femenino'),
        ('Otro', 'otro'),
    ))
    telefono = models.CharField(max_length=128)
    fecha_nacimiento = models.DateField(max_length=128)
    direccion = models.CharField(max_length=256)
    nivel_estudiantil = models.ForeignKey(NivelEstudiantil, blank=True, null=True, on_delete=models.DO_NOTHING)
    nivel_ts = models.ForeignKey(NivelTS, blank=True, on_delete=models.DO_NOTHING, null=True)
    representantes = models.ManyToManyField(Representante, blank=True, null=True)

class Becado(models.Model):
    alumno = models.ForeignKey(Alumno, blank=True, null=True, on_delete=models.CASCADE)
    tipo = models.ForeignKey(TipoBeca, blank=True, null=True, on_delete=models.CASCADE)

class Programas(models.Model):
    nombre = models.CharField(max_length=128)
    agrupacion = models.ForeignKey(Agrupacion, blank=True, on_delete=models.CASCADE)

class QuienRetira(models.Model):  
    alumno = models.ForeignKey(Alumno, blank=True, null=True, on_delete=models.CASCADE)
    Representante = models.ForeignKey(Representante, blank=True, null=True)

class Inscripcion(models.Model):
    alumno = models.ForeignKey(Alumno, blank=True, null=True, on_delete=models.CASCADE)
    fecha_inscrpcion = models.DateField(max_length=128)
    turno = models.ForeignKey(Turno, blank=True, null=True)

class Tipo_catedra(models.Model):
    nombre = models.CharField(max_length=128)

class Catedra(models.Model):
    nombreCatedra = models.CharField(max_length=128)
    instrumento = models.ForeignKey(Instrumento, blank=True, null=True)
    nombreTipoCatedra = models.ForeignKey(Tipo_catedra, blank=True, null=True)
