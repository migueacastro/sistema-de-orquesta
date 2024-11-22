from django.db import models

# Create your models here.

class Medicamento(models.Model):
    nombre = models.CharField(max_length=512, blank=True, null=True)
    activo = models.BooleanField(default=True)
    def __unicode__(self):
        return self.nombre
    def __str__(self):
        return self.nombre

class Tratamiento(models.Model):
    nombre = models.CharField(max_length=512, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    medicamentos = models.ManyToManyField(Medicamento, blank=True)
    activo = models.BooleanField(default=True)
    def __unicode__(self):
        return self.nombre
    def __str__(self):
        return self.nombre

class CondicionEspecial(models.Model):
    nombre = models.CharField(max_length=128, blank=True, null=True)
    tratamiento = models.ManyToManyField(Tratamiento, blank=True)
    activo = models.BooleanField(default=True)
    def __unicode__(self):
        return self.nombre
    def __str__(self):
        return self.nombre


class Alergia(models.Model):
    nombre = models.CharField(max_length=512)
    descripcion = models.TextField(blank=True)
    activo = models.BooleanField(default=True)
    def __unicode__(self):
        return self.nombre
    def __str__(self):
        return self.nombre

class Color(models.Model):
    nombre = models.CharField(max_length=128, blank=True, null=True)
    activo = models.BooleanField(default=True)
    def __unicode__(self):
        return self.nombre
    def __str__(self):
        return self.nombre

class CategoriaInstrumento(models.Model):
    nombre = models.CharField(max_length=128, blank=True, null=True)
    activo = models.BooleanField(default=True)
    def __unicode__(self):
        return self.nombre
    def __str__(self):
        return self.nombre

class MarcaInstrumento(models.Model):
    nombre = models.CharField(max_length=128, blank=True, null=True)
    activo = models.BooleanField(default=True)
    def __unicode__(self):
        return self.nombre
    def __str__(self):
        return self.nombre

class ModeloInstrumento(models.Model):
    nombre = models.CharField(max_length=128, blank=True, null=True)
    marca = models.ForeignKey(MarcaInstrumento, null=True, on_delete=models.CASCADE)
    categoria = models.ForeignKey(CategoriaInstrumento, null=True, on_delete=models.CASCADE)
    activo = models.BooleanField(default=True)
    def __unicode__(self):
        return self.nombre
    def __str__(self):
        return self.nombre

class Accesorio(models.Model):
    nombre = models.CharField(max_length=128, blank=True, null=True)
    activo = models.BooleanField(default=True)
    def __unicode__(self):
        return self.nombre
    def __str__(self):
        return self.nombre


class Agrupacion(models.Model):
    nombre = models.CharField(max_length=128, blank=True, null=True)
    activo = models.BooleanField(default=True)
    def __unicode__(self):
        return self.nombre
    def __str__(self):
        return self.nombre

class Turno (models.Model):
    nombre = models.CharField(max_length=128, blank=True, null=True)
    activo = models.BooleanField(default=True)
    def __unicode__(self):
        return self.nombre
    def __str__(self):
        return self.nombre

class NivelTS (models.Model):
    nombre = models.CharField(max_length=128, blank=True, null=True)
    activo = models.BooleanField(default=True)
    def __unicode__(self):
        return self.nombre
    def __str__(self):
        return self.nombre

class NivelEstudiantil (models.Model):
    nombre = models.CharField(max_length=128, blank=True, null=True)
    activo = models.BooleanField(default=True)
    def __unicode__(self):
        return self.nombre
    def __str__(self):
        return self.nombre

class TipoBeca(models.Model):
    nombre = models.CharField(max_length=128, blank=True, null=True)
    activo = models.BooleanField(default=True)
    def __unicode__(self):
        return self.nombre
    def __str__(self):
        return self.nombre

class Representante(models.Model):
    nombre = models.CharField(max_length=128, blank=True, null=True)
    cedula = models.CharField(max_length=32, blank=True, null=True)
    telefono = models.CharField(max_length=128, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    parentesco = models.CharField(max_length=128, blank=True, null=True)
    activo = models.BooleanField(default=True)
    def __str__(self):
        return self.nombre + " " + self.cedula 
    def __unicode__(self):
        return self.nombre + " " + self.cedula

class Programa(models.Model):
    nombre = models.CharField(max_length=128)
    #agrupacion = models.ForeignKey(Agrupacion, blank=True, on_delete=models.CASCADE, null=True)
    activo = models.BooleanField(default=True)
    def __unicode__(self):
        return self.nombre
    def __str__(self):
        return self.nombre
class QuienRetira(models.Model):  
    nombre = models.CharField(blank=True, null=True, max_length=64)
    activo = models.BooleanField(default=True)
    def __str__(self):
        return self.nombre 
    def __unicode__(self):
        return self.nombre
class TipoCatedra(models.Model):
    nombre = models.CharField(max_length=128)
    activo = models.BooleanField(default=True)
    def __unicode__(self):
        return self.nombre
    def __str__(self):
        return self.nombre
class Catedra(models.Model):
    nombre = models.CharField(max_length=128)
    tipo = models.ForeignKey(TipoCatedra, blank=True, null=True, on_delete=models.DO_NOTHING)
    activo = models.BooleanField(default=True)
    def __str__(self):
        return self.nombre 
    def __unicode__(self):
        return self.nombre
class Alumno(models.Model):
    nombre = models.CharField(max_length=128) 
    apellido = models.CharField(max_length=128) 
    cedula = models.CharField(max_length=32, null=True) 
    edad = models.IntegerField()
    turno = models.ForeignKey(Turno, blank=True, on_delete=models.DO_NOTHING, null=True) 
    sexo = models.CharField(max_length=32, choices=( 
        ('Masculino', 'Masculino'),
        ('Femenino', 'Femenino'),
        ('Otro', 'Otro'),
    ))
    telefono = models.CharField(max_length=128, null=True, blank=True) 
    fecha_nacimiento = models.DateField(max_length=128, null=True, blank=True) 
    direccion = models.CharField(max_length=256, null=True, blank=True) 
    nivel_estudiantil = models.ForeignKey(NivelEstudiantil, blank=True, null=True, on_delete=models.DO_NOTHING)
    nivel_ts = models.ForeignKey(NivelTS, blank=True, on_delete=models.DO_NOTHING, null=True) 
    representantes = models.ManyToManyField(Representante, blank=True) 
    alergias = models.ManyToManyField(Alergia, blank=True) 
    condicion_especial = models.ForeignKey(CondicionEspecial, blank=True, null=True, on_delete=models.DO_NOTHING)
    tratamientos = models.ManyToManyField(Tratamiento, blank=True) 
    programa = models.ForeignKey(Programa, on_delete=models.DO_NOTHING, blank=True, null=True) 
    quien_retiras = models.ManyToManyField(QuienRetira, blank=True)
    activo = models.BooleanField(default=True) 
    catedras = models.ManyToManyField(Catedra, blank=True)
    agrupacion = models.ForeignKey(Agrupacion, on_delete=models.DO_NOTHING, blank=True, null=True)
    def __unicode__(self):
        return self.nombre + " " + self.apellido + " " + self.cedula if self.cedula else self.nombre + " " + self.apellido
    def __str__(self):
        return self.nombre + " " + self.apellido + " " + self.cedula if self.cedula else self.nombre + " " + self.apellido
class Instrumento(models.Model):
    nombre = models.CharField(max_length=128, blank=True, null=True)
    serial = models.CharField(max_length=128, blank=True, null=True)
    alumno = models.ForeignKey(Alumno, on_delete=models.SET_NULL, blank=True, null=True,related_name='instrumentos')
    modelo = models.ForeignKey(ModeloInstrumento, null=True, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, null=True, on_delete=models.CASCADE)
    accesorio = models.ForeignKey(Accesorio, null=True, blank=True, on_delete=models.CASCADE)
    asignado = models.CharField(max_length=128, blank=True, null=True, choices=(
        ('Asignado', 'Asignado'),
        ('Propio', 'Propio')
    ))
    activo = models.BooleanField(default=True)
    def __str__(self):
        return self.serial 
    def __unicode__(self):
        return self.serial

class Becado(models.Model):
    alumno = models.ForeignKey(Alumno, blank=True, null=True, on_delete=models.CASCADE)
    tipo = models.ForeignKey(TipoBeca, blank=True, null=True, on_delete=models.CASCADE)
    activo = models.BooleanField(default=True)
    def __unicode__(self):
        return self.alumno + " - " + self.tipo
    def __str__(self):
        return self.alumno + " - " + self.tipo
class Inscripcion(models.Model):
    alumno = models.ForeignKey(Alumno, blank=True, null=True, on_delete=models.CASCADE)
    fecha_inscripcion = models.DateField(max_length=128, null=True, blank=True)
    turno = models.ForeignKey(Turno, blank=True, null=True, on_delete=models.DO_NOTHING)
    activo = models.BooleanField(default=True)

    def __unicode__(self):
        return self.alumno + " - " + self.turno + " - " + str(self.fecha_inscripcion)
    def __str__(self):
        return self.alumno + " - " + self.turno + " - " + str(self.fecha_inscripcion)