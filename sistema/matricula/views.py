from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import *
from django.contrib import messages
from django.forms.models import model_to_dict
from .helpers import viewset

def importar_archivo(request):
    if request.method == 'POST':
        archivo = request.FILES.get('archivo')
        if archivo:
            messages.success(request, 'Archivo importado correctamente.')
        else:
            messages.error(request, 'No se seleccionó ningún archivo.')
    return render(request, '.html')

def inicio(request):
    alumnos = Alumno.objects.all()
    return render(request, 'administrador/home.html', {'title': 'Inicio', 'alumnos':alumnos})



def agregar_alumno(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        cedula = request.POST.get('cedula')
        edad = request.POST.get('edad')
        sexo = request.POST.get('sexo')
        telefono = request.POST.get('telefono')
        direccion = request.POST.get('direccion')
        if not sexo:
            return render(request, 'administrador/create.html', {
                'error': 'El campo sexo es obligatorio.',
            })
        alumno = Alumno(
            nombre=nombre,
            apellido=apellido,
            cedula=cedula,
            edad=edad,
            sexo=sexo,
            telefono=telefono,
            direccion=direccion
        )
        alumno.save()
        if not cedula:
            rep_nombre = request.POST.get('rep_nombre')
            rep_cedula = request.POST.get('rep_cedula')
            rep_telefono = request.POST.get('rep_telefono')
            rep_email = request.POST.get('rep_email')

            representante = Representante(
                nombre=rep_nombre,
                cedula=rep_cedula,
                telefono=rep_telefono,
                email=rep_email
            )
            representante.save()

            alumno.representantes.add(representante)
            alumno.save()
        return redirect('alumno_success')
    return render(request, 'administrador/create.html', {
        
    })


def editar_alumno(request, id):
    alumno = get_object_or_404(Alumno, id=id)
    
    return render(request, '.html')

def eliminar_alumno(request, id):
    alumno = get_object_or_404(Alumno, id=id)
    
    return render(request, '.html', {'alumno': alumno})


def detalles_alumno(request, id):
    alumno = get_object_or_404(Alumno, id=id)
    return render(request, '.html', {'alumno': alumno})

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

def alumnos(request):
    title = 'Alumnos'
    query = Alumno.objects.all()
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