from django.urls import path
from matricula.views import *
from django.urls import register_converter
from .helpers import NullableIntConverter
register_converter(NullableIntConverter, 'nullable_int')

urlpatterns = [
    path('importar-archivo/', importar_archivo, name="importar-archivo"),
    path('', inicio, name='inicio'),
    path('alumnos/<nullable_int:id>', alumnos, name='alumnos'),
    path('cards/', cards, name='cards'),

    
    path('alergias/<nullable_int:id>', alergias, name='alergias'),
    path('tratamientos/', tratamientos, name='tratamientos'),
    path('accesorios/', accesorios, name='accesorios'),
    path('colores/', colores, name='colores'),
    path('categorias-instrumentos/', categorias_instrumentos, name='categorias-instrumentos'),
    path('marcas-instrumentos/', marcas_instrumentos, name='marcas-instrumentos'),
    path('medicamentos/', medicamentos, name='medicamentos'),
    path('condiciones-especiales/', condiciones_especiales, name='condiciones-especiales'),
    path('modelos-instrumentos/', modelos_instrumentos, name='modelos-instrumentos'),
    path('instrumentos/',instrumentos, name='instrumentos'),
    path('agrupaciones/', agrupaciones, name='agrupaciones'),
    path('niveles-ts/', nivelests, name='niveles-ts'),
    path('turnos/', turnos, name='turnos'),
    path('niveles-estudiantiles/', niveles_estudiantiles, name='niveles-estudiantiles'),
    path('tipos-becas/', tipos_becas, name='tipos-becas'),
    path('representantes/', representantes, name='representantes'),
    path('programas/', programas, name='programas'),
    path('quienes-retiran/', quienes_retiran, name='quienes-retiran'),
    path('alumnos/', alumnos, name='alumnos'),
    path('becados/', becados, name='becados'),
    path('inscripciones/', inscripciones, name='inscripciones'),
    path('tipos-catedras/', tipos_catedras, name='tipos-catedras'),
    path('catedras/', catedras, name='catedras'),
]
