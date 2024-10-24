from django.db import models

# Create your models here.



class Medicamento(models.Model):
    nombre = models.CharField(max_length=512, blank=True, null=True)

class Tratamiento(models.Model):
    nombre = models.CharField(max_length=512, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    medicamentos = models.ManyToManyField(Medicamento, blank=True)

class CondicionEspecial(models.Model):
    nombre = models.CharField(max_length=128, blank=True, null=True)
    tratamiento = models.ManyToManyField(Tratamiento, blank=True)


class Alergia(models.Model):
    nombre = models.CharField(max_length=512)
    descripcion = models.TextField(blank=True)


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
    asignado = models.CharField(max_length=128, blank=True, null=True, choices=(
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
    nombre = models.CharField(max_length=128, blank=True, null=True)
    cedula = models.CharField(max_length=32, blank=True, null=True)
    telefono = models.CharField(max_length=128, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    parentesco = models.CharField(max_length=128, blank=True, null=True)


class Programa(models.Model):
    nombre = models.CharField(max_length=128)
    agrupacion = models.ForeignKey(Agrupacion, blank=True, on_delete=models.CASCADE, null=True)


class QuienRetira(models.Model):  
    nombre = models.CharField(blank=True, null=True, max_length=64)


class Alumno(models.Model):
    nombre = models.CharField(max_length=128) 
    apellido = models.CharField(max_length=128) 
    cedula = models.CharField(max_length=32, null=True) 
    edad = models.IntegerField()
    turno = models.ForeignKey(Turno, blank=True, on_delete=models.DO_NOTHING, null=True) 
    instrumentos = models.ManyToManyField(Instrumento, blank=True) 
    sexo = models.CharField(max_length=32, choices=( 
        ('Masculino', 'masculino'),
        ('Femenino', 'femenino'),
        ('Otro', 'otro'),
    ))
    telefono = models.CharField(max_length=128) 
    fecha_nacimiento = models.DateField(max_length=128, null=True, blank=True) 
    direccion = models.CharField(max_length=256) 
    nivel_estudiantil = models.ForeignKey(NivelEstudiantil, blank=True, null=True, on_delete=models.DO_NOTHING)
    nivel_ts = models.ForeignKey(NivelTS, blank=True, on_delete=models.DO_NOTHING, null=True) 
    representantes = models.ManyToManyField(Representante, blank=True) 
    alergias = models.ManyToManyField(Alergia, blank=True) 
    tratamientos = models.ManyToManyField(Tratamiento, blank=True) 
    programa = models.ForeignKey(Programa, on_delete=models.DO_NOTHING, blank=True, null=True) 
    quien_retiras = models.ManyToManyField(QuienRetira, blank=True) 



class Becado(models.Model):
    alumno = models.ForeignKey(Alumno, blank=True, null=True, on_delete=models.CASCADE)
    tipo = models.ForeignKey(TipoBeca, blank=True, null=True, on_delete=models.CASCADE)


class Inscripcion(models.Model):
    alumno = models.ForeignKey(Alumno, blank=True, null=True, on_delete=models.CASCADE)
    fecha_inscripcion = models.DateField(max_length=128, null=True, blank=True)
    turno = models.ForeignKey(Turno, blank=True, null=True, on_delete=models.DO_NOTHING)


class TipoCatedra(models.Model):
    nombre = models.CharField(max_length=128)


class Catedra(models.Model):
    nombre = models.CharField(max_length=128)
    instrumento = models.ForeignKey(Instrumento, blank=True, null=True, on_delete=models.DO_NOTHING)
    tipo = models.ForeignKey(TipoCatedra, blank=True, null=True, on_delete=models.DO_NOTHING)
