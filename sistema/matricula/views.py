from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import *
from matricula.tasks import ejecutar_importaciones, ARCHIVO, leer_db_excel
from django.contrib import messages
from matricula.tasks import ejecutar_importaciones, ARCHIVO, leer_db_excel
from django.forms.models import model_to_dict
from .helpers import viewset, model_to_dict_better

def importar_archivo(request):
    if request.method == 'GET':
        ejecutar_importaciones(leer_db_excel({
            "nombre": "matriculasf.xlsm",
            "rango_columnas": ["A", "AJ"],
            "omitir_filas": 4,
            "tabla": "BD"
        }))
    return redirect('/')

def inicio(request):
    alumnos = Alumno.objects.all()
    return render(request, 'administrador/home.html', {'title': 'Inicio', 'alumnos':alumnos})

def cards(request):
    vistas = [
        {'nombre': 'alumnos', 'title': 'Alumnos', 'description': 'Visualiza y edita la tabla de alumnos.'},
        {'nombre': 'alergias', 'title': 'Alergias', 'description': 'Visualiza y edita la tabla de alergias.', },
        {'nombre': 'agrupaciones', 'title': 'Agrupaciones', 'description': 'Visualiza y edita la tabla de agrupaciones.'},
        {'nombre': 'accesorios', 'title': 'Accesorios', 'description': 'Visualiza y edita la tabla de accesorios.'},
        {'nombre': 'becados', 'title': 'Becados', 'description': 'Visualiza y edita la tabla de becados.'}, 
        {'nombre': 'colores', 'title': 'Colores', 'description': 'Visualiza y edita la tabla de colores.'},
        {'nombre': 'catedras', 'title': 'Cátedras', 'description': 'Visualiza y edita la tabla de cátedras.'},
        {'nombre': 'categorias-instrumentos', 'title': 'Categorías de Instrumentos', 'description': 'Visualiza y edita la tabla de categorías.'},
        {'nombre': 'condiciones-especiales', 'title': 'Condiciones Especiales', 'description': 'Visualiza y edita la tabla de condiciones especiales.'},
        {'nombre': 'instrumentos', 'title': 'Instrumentos', 'description': 'Visualiza y edita la tabla de instrumentos.'},
        {'nombre': 'inscripciones', 'title': 'Inscripciones', 'description': 'Visualiza y edita la tabla de inscripciones.'},
        {'nombre': 'marcas-instrumentos', 'title': 'Marcas de Instrumentos', 'description': 'Visualiza y edita la tabla de marcas.'},
        {'nombre': 'medicamentos', 'title': 'Medicamentos', 'description': 'Visualiza y edita la tabla de medicamentos.'},
        {'nombre': 'modelos-instrumentos', 'title': 'Modelos de Instrumentos', 'description': 'Visualiza y edita la tabla de modelos.'},
        {'nombre': 'niveles-ts', 'title': 'Niveles Técnicos', 'description': 'Visualiza y edita la tabla de niveles técnicos.'},
        {'nombre': 'niveles-estudiantiles', 'title': 'Niveles Estudiantiles', 'description': 'Visualiza y edita la tabla de niveles estudiantiles.'},
        {'nombre': 'turnos', 'title': 'Turnos', 'description': 'Visualiza y edita la tabla de turnos.'},
        {'nombre': 'programas', 'title': 'Programas', 'description': 'Visualiza y edita la tabla de programas.'},
        {'nombre': 'quienes-retiran', 'title': 'Quienes Retiran', 'description': 'Visualiza y edita la tabla de quienes retiran.'},
        {'nombre': 'representantes', 'title': 'Representantes', 'description': 'Visualiza y edita la tabla de representantes.'},
        {'nombre': 'tipos-becas', 'title': 'Tipos de Becas', 'description': 'Visualiza y edita la tabla de tipos de becas.'},
        {'nombre': 'tratamientos', 'title': 'Tratamientos', 'description': 'Visualiza y edita la tabla de tratamientos.'},
        {'nombre': 'tipos-catedras', 'title': 'Tipos de Cátedras', 'description': 'Visualiza y edita la tabla de tipos de cátedras.'},
    ]
    return render(request, 'administrador/cards.html', {'title': 'Tablas', 'vistas': vistas})

def alumnos(request, id):
    plantilla = 'administrador/alumno_table.html'
    turnos = Turno.objects.filter(activo=True)
    # Gracias cris (te odio)
    if id:
        alumno = Alumno.objects.get(id=id)
        match request.method:
            case "GET":
                return render(request, plantilla, {"alumno": alumno, "turnos": turnos})
            case "POST":
                return render(request, plantilla, {"alumno": alumno, "turnos": turnos})
            case "DELETE":
                return render(request, "administrador/inicio.html")
            case _:
                pass
    else:
        match request.method:
            case "GET":
                return render(request, plantilla, {"turnos": turnos})
            case "POST":
                return render(request, plantilla, {"turnos": turnos})
            case _:
                pass
        

def alergias(request, id):
    return viewset(request, 
        Alergia, 
        [
            {
                'name': 'nombre',
                'type': 'text',
                'width': '50'
            },
            {
                'name': 'descripcion',
                'type': 'textarea',
                'width': '50'
            },
        ],
        'Alergias', 
        id
    )

def tratamientos(request, id):
    return viewset(request, 
        Tratamiento, 
        [
            {
                'name': 'nombre',
                'type': 'text',
                'width': '50'
            },
            {
                'name': 'description',
                'type': 'textarea',
                'width': '50'
            },
            {
                'name': 'medicamentos',
                'type': 'manytomany',
                'query': [model_to_dict(i) for i in Medicamento.objects.all()],
                'multiple': True,
                'width': '50'
            },
        ],
        'Tratamientos', 
        id
    )

def medicamentos(request, id):
    return viewset(request, 
        Medicamento, 
        [
            {
                'name': 'nombre',
                'type': 'text',
                'width': '50'
            },
        ],
        'Medicamentos', 
        id
    )

def condiciones_especiales(request, id):
    return viewset(request, 
        CondicionEspecial, 
        [
            {
                'name': 'nombre',
                'type': 'text',
                'width': '50'
            },
            {
                'name': 'tratamiento',
                'type': 'manytomany',
                'query': [model_to_dict(i) for i in Tratamiento.objects.all()],
                'multiple': True,
                'width': '50'
            },
        ],
        'Condiciones Especiales', 
        id
    )

def colores(request, id):
    return viewset(request, 
        Color, 
        [
            {
                'name': 'nombre',
                'type': 'text',
                'width': '50'
            },
        ],
        'Colores', 
        id
    )

def categorias_instrumentos(request, id):
    return viewset(request, 
        CategoriaInstrumento, 
        [
            {
                'name': 'nombre',
                'type': 'text',
                'width': '50'
            },
        ],
        'Categorías de Instrumentos', 
        id
    )

def marcas_instrumentos(request, id):
    return viewset(request, 
        MarcaInstrumento, 
        [
            {
                'name': 'nombre',
                'type': 'text',
                'width': '50'
            },
        ],
        'Marcas de Instrumentos', 
        id
    )

def modelos_instrumentos(request, id):
    return viewset(request, 
        ModeloInstrumento, 
        [
            {
                'name': 'nombre',
                'type': 'text',
                'width': '50'
            },
            {
                'name': 'marca',
                'type': 'foreignkey',
                'query': MarcaInstrumento.objects.all(),
                'width': '50'
            },
            {
                'name': 'categoria',
                'type': 'foreignkey',
                'query': CategoriaInstrumento.objects.all(),
                'width': '50'
            },
        ],
        'Modelos de Instrumentos', 
        id
    )

def accesorios(request, id):
    return viewset(request, 
        Accesorio, 
        [
            {
                'name': 'nombre',
                'type': 'text',
                'width': '50'
            },
        ],
        'Accesorios', 
        id
    )

def instrumentos(request, id):
    return viewset(request, 
        Instrumento, 
        [
            {
                'name': 'nombre',
                'type': 'text',
                'width': '50'
            },
            {
                'name': 'serial',
                'type': 'text',
                'width': '50'
            },
            {
                'name': 'modelo',
                'type': 'foreignkey',
                'query': ModeloInstrumento.objects.all(),
                'width': '50'
            },
            {
                'name': 'color',
                'type': 'foreignkey',
                'query': Color.objects.all(),
                'width': '50'
            },
            {
                'name': 'accesorio',
                'type': 'foreignkey',
                'query': Accesorio.objects.all(),
                'width': '50'
            },
            {
                'name': 'asignado',
                'type': 'select',
                'query': [
                    {'value': 'Asignado', 'label': 'Asignado'},
                    {'value': 'Propio', 'label': 'Propio'},
                ],
                'width': '50'
            },
        ],
        'Instrumentos', 
        id
    )

def agrupaciones(request, id):
    return viewset(request, 
        Agrupacion, 
        [
            {
                'name': 'nombre',
                'type': 'text',
                'width': '50'
            },
            {
                'name': 'instrumentos',
                'type': 'manytomany',
                'query': [model_to_dict(i) for i in Instrumento.objects.all()],
                'multiple': True,
                'width': '50'
            },
        ],
        'Agrupaciones', 
        id
    )

def niveles_estudiantiles(request,id):
    return viewset(request, 
        NivelEstudiantil,
        [
            {
                'name': 'nombre',
                'type': 'text',
                'width': '50'
            },
        ],
        'Niveles Estudiantiles',
        id
    )

def nivelests(request,id):
    return viewset(request, 
        NivelTS,
        [
            {
                'name': 'nombre',
                'type': 'text',
                'width': '50'
            },
        ],
        'Niveles TS',
        id
    )

def turnos(request,id):
    return viewset(request, 
        Turno,
        [
            {
                'name': 'nombre',
                'type': 'text',
                'width': '50'
            },
        ],
        'Turnos',
        id
    )

def tipos_becas(request,id):
    return viewset(request, 
        TipoBeca,
        [
            {
                'name': 'nombre',
                'type': 'text',
                'width': '50'
            },
        ],
        'Tipos de Beca',
        id
    )

def representantes(request,id):
    return viewset(request, 
        Representante,
        [
            {
                'name': 'nombre',
                'type': 'text',
                'width': '50'
            },
            {
                'name': 'cedula',
                'type': 'text',
                'width': '50'
            },
            {
                'name': 'telefono',
                'type': 'text',
                'width': '50'
            },
            {
                'name': 'email',
                'type': 'email',
                'width': '50'
            },
            {
                'name': 'parentesco',
                'type': 'text',
                'width': '50'
            },
        ],
        'Representantes',
        id
    )

def programas(request,id):
    return viewset(request, 
        Programa,
        [
            {
                'name': 'nombre',
                'type': 'text',
                'width': '50'
            },
            {
                'name': 'agrupacion',
                'type': 'foreignkey',
                'query': Agrupacion.objects.all(),
                'width': '50'
            },
        ],
        'Programas',
        id
    )

def quienes_retiran(request,id):
    return viewset(request, 
        QuienRetira,
        [
            {
                'name': 'nombre',
                'type': 'text',
                'width': '50'
            },
        ],
        'Quien Retira',
        id
    )
def becados(request, id):
    return viewset(request, 
        Becado, 
        [
            {
                'name': 'nombre_becado',
                'type': 'text',
                'width': '50'
            },
            {
                'name': 'tipo_beca',
                'type': 'text',
                'width': '50'
            },
        ],
        'Becados', 
        id
    )
def inscripciones(request,id):
    return viewset(request, 
        Inscripcion,
        [
            {
                'name': 'alumno',
                'type': 'foreignkey',
                'query': Alumno.objects.all(),
                'width': '50'
            },
            {
                'name': 'fecha_inscripcion',
                'type': 'date',
                'width': '50'
            },
            {
                'name': 'turno',
                'type': 'foreignkey',
                'query': Turno.objects.all(),
                'width': '50'
            },
        ],
        'Inscripciones',
        id
    )
def tipos_catedras(request, id):
    return viewset(request, 
        TipoCatedra, 
        [
            {
                'name': 'nombre',
                'type': 'text',
                'width': '50'
            },
            {
                'name': 'descripcion',
                'type': 'textarea',
                'width': '50'
            },
        ],
        'Tipos de Cátedra', 
        id
    )

def catedras(request,id):
    return viewset(request, 
        Catedra,
        [
            {
                'name': 'nombre',
                'type': 'text',
                'width': '50'
            },
            {
                'name': 'instrumento',
                'type': 'foreignkey',
                'query': Instrumento.objects.all(),
                'width': '50'
            },
            {
                'name': 'tipo',
                'type': 'foreignkey',
                'query': TipoCatedra.objects.all(),
                'width': '50'
            },
        ],
        'Cátedras',
        id
    )