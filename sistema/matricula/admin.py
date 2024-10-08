from django.contrib import admin
from matricula.models import *

# Register your models here.
class AlumnoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'apellido', 'fecha_nacimiento']
admin.site.register(Alumno, AlumnoAdmin)
admin.site.register(Alergia)
admin.site.register(Accesorio)
admin.site.register(Agrupacion)
admin.site.register(Becado)
admin.site.register(Catedra)
admin.site.register(CategoriaInstrumento)
admin.site.register(Color)
admin.site.register(MarcaInstrumento)
admin.site.register(Medicamento)
admin.site.register(NivelTS)
admin.site.register(NivelEstudiantil)
admin.site.register(Programa)
admin.site.register(QuienRetira)
admin.site.register(Representante)
admin.site.register(TipoBeca)
admin.site.register(TipoCatedra)
admin.site.register(Tratamiento)
admin.site.register(Turno)
admin.site.register(Inscripcion)
