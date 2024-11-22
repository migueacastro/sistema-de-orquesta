from django.urls import path
from django.urls import register_converter
from .helpers import NullableIntConverter
from .views import *
register_converter(NullableIntConverter, 'nullable_int')

urlpatterns = [
    path('importar-archivo/', importar_archivo, name="importar-archivo"),
    path('', inicio, name='inicio'),
    path('alumnos/<nullable_int:id>', alumnos, name='alumnos'),
    path('cards/', cards, name='cards'),
    path('exportar_pdf/', generar_pdf, name='exportar_pdf'), 

    
    path('alumnos/<nullable_int:id>', alumnos, name='alumnos'),
    path('alergias/<nullable_int:id>', alergias, name='alergias'),
    path('agrupaciones/<nullable_int:id>', agrupaciones, name='agrupaciones'),
    path('accesorios/<nullable_int:id>', accesorios, name='accesorios'),
    path('becados/<nullable_int:id>', becados, name='becados'),
    path('colores/<nullable_int:id>', colores, name='colores'),
    path('catedras/<nullable_int:id>', catedras, name='catedras'),
    path('categorias-instrumentos/<nullable_int:id>', categorias_instrumentos, name='categorias-instrumentos'),
    path('condiciones-especiales/<nullable_int:id>', condiciones_especiales, name='condiciones-especiales'),
    path('instrumentos/<nullable_int:id>',instrumentos, name='instrumentos'),
    path('inscripciones/<nullable_int:id>', inscripciones, name='inscripciones'),
    path('marcas-instrumentos/<nullable_int:id>', marcas_instrumentos, name='marcas-instrumentos'),
    path('medicamentos/<nullable_int:id>', medicamentos, name='medicamentos'),
    path('modelos-instrumentos/<nullable_int:id>', modelos_instrumentos, name='modelos-instrumentos'),
    path('niveles-ts/<nullable_int:id>', nivelests, name='niveles-ts'),
    path('niveles-estudiantiles/<nullable_int:id>', niveles_estudiantiles, name='niveles-estudiantiles'),
    path('programas/<nullable_int:id>', programas, name='programas'),
    path('quienes-retiran/<nullable_int:id>', quienes_retiran, name='quienes-retiran'),
    path('representantes/<nullable_int:id>', representantes, name='representantes'),
    path('tratamientos/<nullable_int:id>', tratamientos, name='tratamientos'),
    path('turnos/<nullable_int:id>', turnos, name='turnos'),
    path('tipos-becas/<nullable_int:id>', tipos_becas, name='tipos-becas'),
    path('tipos-catedras/<nullable_int:id>', tipos_catedras, name='tipos-catedras'),
]
