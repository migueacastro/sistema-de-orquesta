from django.urls import path
from matricula.views import *

urlpatterns = [
    path('importar-archivo/', importar_archivo, name="importar-archivo"),
    path('', inicio, name='inicio'),
    path('agregar/', agregar_alumno, name='agregar_alumno'),
    path('alumnos/', listar_alumnos, name='listar_alumnos'),
    path('alumno/<int:id>', detalles_alumno, name='detalles_alumno'),

    
    path('Alergias/', alergias, name='Alergias'),
    path('Tratamientos/', tratamientos, name='Tratamientos'),
    path('Accesorios/', accesorios, name='Accesorios'),
    path('Colores/', colores, name='Colores'),
    path('CategoriasInstrumentos/', CategoriasInstrumentos, name='CategoriasInstrumentos'),
    path('MarcasInstrumentos/', MarcasInstrumentos, name='MarcasInstrumentos'),
    path('Medicamentos/', Medicamentos, name='Medicamentos'),
    path('CondicionesEspeciales/', CondicionesEspeciales, name='CondicionesEspeciales'),
    path('ModelosInstrumentos/', ModelosInstrumentos, name='ModelosInstrumentos'),
    path('Instrumentos/', Instrumentos, name='Instrumentos'),
    path('Agrupaciones/', Agrupaciones, name='Agrupaciones'),
    path('NivelesTS/', NivelesTS, name='NivelesTS'),
    path('Turnos/', Turnos, name='Turnos'),
    path('NivelesEstudiantiles/', NivelesEstudiantiles, name='NivelesEstudiantiles'),
    path('TiposBecas/', TiposBecas, name='TiposBecas'),
    path('Representantes/', Representantes, name='Representantes'),
    path('Programas/', Programas, name='Programas'),
    path('QuienesRetiran/', QuienesRetiran, name='QuienesRetiran'),
    path('Alumnos/', Alumnos, name='Alumnos'),
    path('Becados/', Becados, name='Becados'),
    path('Inscripciones/', Inscripciones, name='Inscripciones'),
    path('TiposCatedras/', TiposCatedras, name='TiposCatedras'),
    path('Catedras/', Catedras, name='Catedras'),
]
