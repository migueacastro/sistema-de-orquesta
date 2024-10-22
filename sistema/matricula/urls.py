from django.urls import path
from matricula.views import *

urlpatterns = [
    path('importar-archivo/', importar_archivo, name="importar-archivo"),
    path('', inicio, name='inicio'),
    path('agregar/', agregar_alumno, name='agregar_alumno'),
    path('alumnos/', listar_alumnos, name='listar_alumnos'),
    path('alumno/<int:id>', detalles_alumno, name='detalles_alumno'),

    
    path('alergias/', alergias, name='alergias'),
    path('tratamientos/', tratamientos, name='tratamientos'),
    path('accesorios/', accesorios, name='accesorios'),
    path('colores/', colores, name='colores'),

]
