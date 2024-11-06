from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import *
from matricula.tasks import ejecutar_importaciones, ARCHIVO, leer_db_excel
from django.contrib import messages
from django.forms.models import model_to_dict
from .helpers import viewset

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
        {'nombre': 'alergias', 'title': 'Alergias', 'description': 'Visualiza y edita la tabla de alergias.', },
        {'nombre': 'tratamientos', 'title': 'Tratamientos', 'description': 'Visualiza y edita la tabla de tratamientos.'},
        {'nombre': 'accesorios', 'title': 'Accesorios', 'description': 'Visualiza y edita la tabla de accesorios.'},
        {'nombre': 'colores', 'title': 'Colores', 'description': 'Visualiza y edita la tabla de colores.'},
        {'nombre': 'categorias-instrumentos', 'title': 'Categorías de Instrumentos', 'description': 'Visualiza y edita la tabla de categorías.'},
        {'nombre': 'marcas-instrumentos', 'title': 'Marcas de Instrumentos', 'description': 'Visualiza y edita la tabla de marcas.'},
        {'nombre': 'medicamentos', 'title': 'Medicamentos', 'description': 'Visualiza y edita la tabla de medicamentos.'},
        {'nombre': 'condiciones-especiales', 'title': 'Condiciones Especiales', 'description': 'Visualiza y edita la tabla de condiciones especiales.'},
        {'nombre': 'modelos-instrumentos', 'title': 'Modelos de Instrumentos', 'description': 'Visualiza y edita la tabla de modelos.'},
        {'nombre': 'instrumentos', 'title': 'Instrumentos', 'description': 'Visualiza y edita la tabla de instrumentos.'},
        {'nombre': 'agrupaciones', 'title': 'Agrupaciones', 'description': 'Visualiza y edita la tabla de agrupaciones.'},
        {'nombre': 'niveles-ts', 'title': 'Niveles Técnicos', 'description': 'Visualiza y edita la tabla de niveles técnicos.'},
        {'nombre': 'turnos', 'title': 'Turnos', 'description': 'Visualiza y edita la tabla de turnos.'},
        {'nombre': 'niveles-estudiantiles', 'title': 'Niveles Estudiantiles', 'description': 'Visualiza y edita la tabla de niveles estudiantiles.'},
        {'nombre': 'tipos-becas', 'title': 'Tipos de Becas', 'description': 'Visualiza y edita la tabla de tipos de becas.'},
        {'nombre': 'representantes', 'title': 'Representantes', 'description': 'Visualiza y edita la tabla de representantes.'},
        {'nombre': 'programas', 'title': 'Programas', 'description': 'Visualiza y edita la tabla de programas.'},
        {'nombre': 'quienes-retiran', 'title': 'Quienes Retiran', 'description': 'Visualiza y edita la tabla de quienes retiran.'},
        {'nombre': 'alumnos', 'title': 'Alumnos', 'description': 'Visualiza y edita la tabla de alumnos.'},
        {'nombre': 'becados', 'title': 'Becados', 'description': 'Visualiza y edita la tabla de becados.'},
        {'nombre': 'inscripciones', 'title': 'Inscripciones', 'description': 'Visualiza y edita la tabla de inscripciones.'},
        {'nombre': 'tipos-catedras', 'title': 'Tipos de Cátedras', 'description': 'Visualiza y edita la tabla de tipos de cátedras.'},
        {'nombre': 'catedras', 'title': 'Cátedras', 'description': 'Visualiza y edita la tabla de cátedras.'},
    ]
    return render(request, 'administrador/cards.html',{'vistas': vistas})

def alumnos(request, id):
    return viewset(request, 
        Alumno,  
        [
            {
                'name': 'nombre',
                'type': 'text',
                'width': '50'
            },
            {
                'name': 'apellido',
                'type': 'text',
                'width': '50'
            },
            {
                'name': 'cedula',
                'type': 'text',
                'width': '50'
            },
            {
                'name': 'edad',
                'type': 'integer',
                'width': '20'
            },
            {
                'name': 'turno',
                'type': 'foreingnkey', 
                'query': Turno.objects.all(),
                'width': '50'
            },
            {
                'name': 'instrumentos',
                'type': 'manytomany', 
                'query': [model_to_dict(i) for i in Instrumento.objects.all()],
                'multiple': True,
                'width': '50'
            },
            {
                'name': 'sexo',
                'type': 'select',
                'query': [
                    {'value': 'Masculino', 'label': 'Masculino'},
                    {'value': 'Femenino', 'label': 'Femenino'},
                ],
                'width': '50'
            },
            {
                'name': 'telefono',
                'type': 'text',
                'width': '50'
            },
            {
                'name': 'fecha_nacimiento',
                'type': 'date',
                'width': '50'
            },
            {
                'name': 'direccion',
                'type': 'textarea',
                'width': '50'
            },
            {
                'name': 'nivel_estudiantil',
                'type': 'foreingnkey',
                'query': NivelEstudiantil.objects.all(),
                'width': '50'
            },
            {
                'name': 'nivel_ts',
                'type': 'foreingnkey',
                'query': NivelTS.objects.all(),
                'width': '50'
            },
            {
                'name': 'representantes',
                'type': 'manytomany', 
                'query': [model_to_dict(i) for i in Representante.objects.all()],
                'multiple': True,
                'width': '50'
            },
            {
                'name': 'alergias',
                'type': 'manytomany', 
                'query': [model_to_dict(i) for i in Alergia.objects.all()],
                'multiple': True,
                'width': '50'
            },
            {
                'name': 'tratamientos',
                'type': 'manytomany', 
                'query': [model_to_dict(i) for i in Tratamiento.objects.all()],
                'multiple': True,
                'width': '50'
            },
            {
                'name': 'programa',
                'type': 'foreignkey',
                'options': Programa.objects.all(),
                'width': '50'
            },
            {
                'name': 'quien_retiras',
                'type': 'manytomany', 
                'query': [model_to_dict(i) for i in QuienRetira.objects.all()],
                'multiple': True,
                'width': '50'
            },
        ],
        'Alumnos',  
        id  
    )

def alergias(request, id):
    return viewset(request, 
        Alergia, # Modelo
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
        'Alergias', # Título
        id) # Id


def tratamientos(request):
    title = 'Tratamientos'
    query = Tratamiento.objects.all()
    entries = [model_to_dict(i) for i in query]
    return render(request, 'administrador/table.html', {'title': title, 'entries': entries, 'first_entry': entries[0] if len(entries) > 0 else None})

def accesorios(request):
    title = 'Accesorios'
    query = Accesorio.objects.all()
    entries = [model_to_dict(i) for i in query]
    return render(request, 'administrador/table.html', {'title': title, 'entries': entries, 'first_entry': entries[0] if len(entries) > 0 else None})

def colores(request):
    title = 'Colores'
    query = Color.objects.all()
    entries = [model_to_dict(i) for i in query]
    return render(request, 'administrador/table.html', {'title': title, 'entries': entries, 'first_entry': entries[0] if len(entries) > 0 else None})

def categorias_instrumentos(request):
    title = 'Categoria Instrumentos'
    query = CategoriaInstrumento.objects.all()
    entries = [model_to_dict(i) for i in query]
    return render(request, 'administrador/table.html', {'title': title, 'entries': entries, 'first_entry': entries[0] if len(entries) > 0 else None})

def marcas_instrumentos(request):
    title = 'Marca Instrumentos'
    query = MarcaInstrumento.objects.all()
    entries = [model_to_dict(i) for i in query]
    return render(request, 'administrador/table.html', {'title': title, 'entries': entries, 'first_entry': entries[0] if len(entries) > 0 else None})

def medicamentos(request):
    title = 'Medicamentos'
    query = Medicamento.objects.all()
    entries = [model_to_dict(i) for i in query]
    return render(request, 'administrador/table.html', {'title': title, 'entries': entries, 'first_entry': entries[0] if len(entries) > 0 else None})

def condiciones_especiales(request):
    title = 'Condiciones Especiales'
    query = CondicionEspecial.objects.all()
    entries = [model_to_dict(i) for i in query]
    return render(request, 'administrador/table.html', {'title': title, 'entries': entries, 'first_entry': entries[0] if len(entries) > 0 else None})

def modelos_instrumentos(request):
    title = 'Modelos Instrumentos'
    query = ModeloInstrumento.objects.all()
    entries = [model_to_dict(i) for i in query]
    return render(request, 'administrador/table.html', {'title': title, 'entries': entries, 'first_entry': entries[0] if len(entries) > 0 else None})

def instrumentos(request):
    title = 'Instrumentos'
    query = Instrumento.objects.all()
    entries = [model_to_dict(i) for i in query]
    return render(request, 'administrador/table.html', {'title': title, 'entries': entries, 'first_entry': entries[0] if len(entries) > 0 else None})

def agrupaciones(request):
    title = 'Agrupaciones'
    query = Agrupacion.objects.all()
    entries = [model_to_dict(i) for i in query]
    return render(request, 'administrador/table.html', {'title': title, 'entries': entries, 'first_entry': entries[0] if len(entries) > 0 else None})

def nivelests(request):
    title = 'Niveles TS'
    query = NivelTS.objects.all()
    entries = [model_to_dict(i) for i in query]
    return render(request, 'administrador/table.html', {'title': title, 'entries': entries, 'first_entry': entries[0] if len(entries) > 0 else None})

def turnos(request):
    title = 'Turnos'
    query = Turno.objects.all()
    entries = [model_to_dict(i) for i in query]
    return render(request, 'administrador/table.html', {'title': title, 'entries': entries, 'first_entry': entries[0] if len(entries) > 0 else None})

def niveles_estudiantiles(request):
    title = 'Niveles Estudiantiles'
    query = NivelEstudiantil.objects.all()
    entries = [model_to_dict(i) for i in query]
    return render(request, 'administrador/table.html', {'title': title, 'entries': entries, 'first_entry': entries[0] if len(entries) > 0 else None})

def tipos_becas(request):
    title = 'Tipos Becas'
    query = TipoBeca.objects.all()
    entries = [model_to_dict(i) for i in query]
    return render(request, 'administrador/table.html', {'title': title, 'entries': entries, 'first_entry': entries[0] if len(entries) > 0 else None})

def representantes(request):
    title = 'Representantes'
    query = Representante.objects.all()
    entries = [model_to_dict(i) for i in query]
    return render(request, 'administrador/table.html', {'title': title, 'entries': entries, 'first_entry': entries[0] if len(entries) > 0 else None})

def programas(request):
    title = 'Programas'
    query = Programa.objects.all()
    entries = [model_to_dict(i) for i in query]
    return render(request, 'administrador/table.html', {'title': title, 'entries': entries, 'first_entry': entries[0] if len(entries) > 0 else None})

def quienes_retiran(request):
    title = 'Quienes Retiran'
    query = QuienRetira.objects.all()
    entries = [model_to_dict(i) for i in query]
    return render(request, 'administrador/table.html', {'title': title, 'entries': entries, 'first_entry': entries[0] if len(entries) > 0 else None})

def becados(request):
    title = 'Becados'
    query = Becado.objects.all()
    entries = [model_to_dict(i) for i in query]
    return render(request, 'administrador/table.html', {'title': title, 'entries': entries, 'first_entry': entries[0] if len(entries) > 0 else None})

def inscripciones(request):
    title = 'Inscripciones'
    query = Inscripcion.objects.all()
    entries = [model_to_dict(i) for i in query]
    return render(request, 'administrador/table.html', {'title': title, 'entries': entries, 'first_entry': entries[0] if len(entries) > 0 else None})

def tipos_catedras(request):
    title = 'Tipos Catedras'
    query = TipoCatedra.objects.all()
    entries = [model_to_dict(i) for i in query]
    return render(request, 'administrador/table.html', {'title': title, 'entries': entries, 'first_entry': entries[0] if len(entries) > 0 else None})

def catedras(request):
    title = 'Catedras'
    query = Catedra.objects.all()
    entries = [model_to_dict(i) for i in query]
    return render(request, 'administrador/table.html', {'title': title, 'entries': entries, 'first_entry': entries[0] if len(entries) > 0 else None})