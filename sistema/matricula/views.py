from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Alumno, Inscripcion
from django.contrib import messages

def importar_archivo(request):
    if request.method == 'POST':
        archivo = request.FILES.get('archivo')
        if archivo:
            messages.success(request, 'Archivo importado correctamente.')
        else:
            messages.error(request, 'No se seleccionó ningún archivo.')
    return render(request, '.html')

def inicio(request):
    return render(request, 'administrador/home.html', {'title': "Hola pipipipip"})

def listar_alumnos(request):
    alumnos = Alumno.objects.all()
    return render(request, '.html', {'alumnos': alumnos})

def agregar_alumno(request):

    return render(request, '.html')


def editar_alumno(request, id):
    alumno = get_object_or_404(Alumno, id=id)
    
    return render(request, '.html')

def eliminar_alumno(request, id):
    alumno = get_object_or_404(Alumno, id=id)
    
    return render(request, '.html', {'alumno': alumno})


def detalles_alumno(request, id):
    alumno = get_object_or_404(Alumno, id=id)
    return render(request, '.html', {'alumno': alumno})

