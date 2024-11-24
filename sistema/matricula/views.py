from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from matricula.tasks import ejecutar_importaciones, ARCHIVO, leer_db_excel
from django.contrib import messages
from matricula.tasks import ejecutar_importaciones, ARCHIVO, leer_db_excel
from django.forms.models import model_to_dict
from django.http import JsonResponse
from .helpers import viewset, model_to_dict_better
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, PageBreak, Paragraph
from reportlab.lib.styles import getSampleStyleSheet


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
    alumnos = Alumno.objects.filter(activo=True)
    query = alumnos
    entries = [model_to_dict_better(i) for i in query]
    return render(request, 'administrador/home.html', {'title': 'Inicio', 'alumnos':alumnos, 'entries': entries, 
                    'first_entry': entries[0] if len(entries) > 0 else None, })


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
                'endpoint': 'turnos',
                'width': '50'
            },
            {
                'name': 'instrumentos',
                'type': 'manytomany', 
                'endpoint': 'instrumentos',
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
                'endpoint': 'niveles-estudiantiles',
                'width': '50'
            },
            {
                'name': 'nivel_ts',
                'type': 'foreingnkey',
                'endpoint': 'niveles-ts',
                'width': '50'
            },
            {
                'name': 'representantes',
                'type': 'manytomany', 
                'endpoint': 'representantes',
                'multiple': True,
                'width': '50'
            },
            {
                'name': 'alergias',
                'type': 'manytomany', 
                'endpoint': 'alergias',
                'multiple': True,
                'width': '50'
            },
            {
                'name': 'tratamientos',
                'type': 'manytomany', 
                'endpoint': 'tratamientos',
                'width': '50'
            },
            {
                'name': 'programa',
                'type': 'foreignkey',
                'endpoint': 'programas',
                'width': '50'
            },
            {
                'name': 'condición especial',
                'type': 'foreignkey',
                'endpoint': 'condiciones-especiales',
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
        AlumnoForm,  
        'alumnos',
        id  
    )

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
        AlergiaForm, 
        'alergias',
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
        TratamientoForm,
        'tratamientos',
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
        MedicamentoForm,
        'medicamentos',
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
        CondicionEspecialForm,
        'condiciones-especiales',
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
        ColorForm,
        'colores',
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
        CategoriaInstrumentoForm,
        'categorias-instrumentos',
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
        MarcaInstrumentoForm,
        'marcas-instrumentos',
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
        ModeloInstrumentoForm,
        'modelos-instrumentos',
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
        AccesorioForm,
        'accesorios',
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
        InstrumentoForm,
        'instrumentos',
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
        AgrupacionForm,
        'agrupaciones',
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
        NivelEstudiantilForm,
        'niveles-estudiantiles',
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
        NivelTSForm,
        'niveles-ts',
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
        TurnoForm,
        'turnos',
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
        TipoBecaForm,
        'tipos-becas',
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
        RepresentanteForm,
        'representantes',
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
        ProgramaForm,
        'programas',
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
        QuienRetiraForm,
        'quienes-retiran',
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
        BecadoForm,
        'becados',
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
        InscripcionForm,
        'inscripciones',
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
        TipoCatedraForm, 
        'tipos-catedras',
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
        CatedraForm,
        'catedras',
        id
    )
def generar_pdf(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="matricula_alumnos.pdf"'

    ancho = 2500  
    alto = 850  
    doc = SimpleDocTemplate(response, pagesize=(ancho, alto))

    alumnos = Alumno.objects.filter(activo=True).order_by('id')

    headers = ['ID', 'Nombre', 'Apellido', 'Cédula', 'Edad', 'Turno', 'Sexo', 'Teléfono', 'Fecha Nacimiento',
               'Fecha Inscripción', 'Dirección', 'Nivel Estudiantil', 'Condición Especial', 'Programa', 'Agrupación',
               'Representantes', 'Alergias', 'Tratamientos', '¿Quién Retira?', 'Catedras']

    data = [headers]

    def validacion(valor):
        return valor if valor not in [None, "", " "] else "Ninguno"

    for alumno in alumnos:
        representantes_texto = ", ".join([rep.nombre for rep in alumno.representantes.all()]) if alumno.representantes.exists() else "Ninguno"
        alergias_texto = ", ".join([alergia.descripcion for alergia in alumno.alergias.all()]) if alumno.alergias.exists() else "Ninguno"
        tratamientos_texto = ", ".join([tratamiento.nombre for tratamiento in alumno.tratamientos.all()]) if alumno.tratamientos.exists() else "Ninguno"
        quienretira_texto = ", ".join([quienretira.nombre for quienretira in alumno.quien_retiras.all()]) if alumno.quien_retiras.exists() else "Ninguno"
        catedras_texto = ", ".join([catedra.nombre for catedra in alumno.catedras.all()]) if alumno.catedras.exists() else "Ninguno"
        fecha_inscripcion = alumno.inscripcion_set.first().fecha_inscripcion if alumno.inscripcion_set.exists() else "Ninguno"
        row = [
            alumno.id,
            Paragraph(str(validacion(alumno.nombre))),
            Paragraph(str(validacion(alumno.apellido))),
            Paragraph(str(validacion(alumno.cedula))),
            Paragraph(str(validacion(alumno.edad))),
            Paragraph(str(validacion(alumno.turno))),
            Paragraph(str(validacion(alumno.sexo))),
            Paragraph(str(validacion(alumno.telefono))),
            Paragraph(str(validacion(alumno.fecha_nacimiento))),
            Paragraph(str(validacion(fecha_inscripcion))),
            Paragraph(str(validacion(alumno.direccion))),
            Paragraph(str(validacion(alumno.nivel_estudiantil))),
            Paragraph(str(validacion(alumno.condicion_especial))),
            Paragraph(str(validacion(alumno.programa))),
            Paragraph(str(validacion(alumno.agrupacion))),
            Paragraph(str(representantes_texto)),
            Paragraph(str(alergias_texto)),
            Paragraph(str(tratamientos_texto)),
            Paragraph(str(quienretira_texto)),
            Paragraph(str(catedras_texto))
        ]
        data.append(row)

    styles = getSampleStyleSheet()
    title_style = styles['Title']  

    title = Paragraph("Matrícula de El Sistema Orquesta - Sede Carabobo", title_style)

    table = Table(data, colWidths=[50, 120, 120, 90, 40, 60, 60, 90, 90, 245, 95, 100, 150, 220, 150, 150, 150, 150, 150])

    style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),  
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),  
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),  
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),  
        ('FONTSIZE', (0, 0), (-1, -1), 10),  
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),  
        ('TOPPADDING', (0, 1), (-1, -1), 6),  
        ('BOTTOMPADDING', (0, 1), (-1, -1), 6),  
        ('GRID', (0, 0), (-1, -1), 1, colors.black),  
        ('LINEABOVE', (0, 0), (-1, 0), 2, colors.black),  
        ('LINEBELOW', (0, -1), (-1, -1), 2, colors.black),  
        ('SPLITLONGWORDS', (0, 1), (-1, -1), True),  # Allow text to wrap to the next line
        ('KEEPWITHNEXT', (0, 1), (-1, -1), True),  
    ])
    table.setStyle(style)

    elements = [title] 


    page_table = Table(data, colWidths=[50, 120, 120, 90, 40, 60, 60, 80, 90, 90, 245, 95, 100, 150, 220, 150, 150, 150, 150, 150])
    page_table.setStyle(style)
    elements.append(page_table)

    doc.build(elements)

    return response
