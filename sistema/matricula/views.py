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

def listar_alumnos(request):
    alumnos = Alumno.objects.all()
    return render(request, '.html', {'alumnos': alumnos})

def agregar_alumno(request):
    if request.method == 'POST':
        form = AlumnoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Alumno agregado con éxito.')
            return redirect('listar_alumnos')
    else:
        form = AlumnoForm()
    return render(request, '.html', {'form': form})


def editar_alumno(request, id):
    alumno = get_object_or_404(Alumno, id=id)
    if request.method == 'POST':
        form = AlumnoForm(request.POST, instance=alumno)
        if form.is_valid():
            form.save()
            messages.success(request, 'Alumno actualizado con éxito.')
            return redirect('listar_alumnos')
    else:
        form = AlumnoForm(instance=alumno)
    return render(request, '.html', {'form': form})

def eliminar_alumno(request, id):
    alumno = get_object_or_404(Alumno, id=id)
    if request.method == 'POST':
        alumno.delete()
        messages.success(request, 'Alumno eliminado con éxito.')
        return redirect('listar_alumnos')
    return render(request, '.html', {'alumno': alumno})


def detalles_alumno(request, id):
    alumno = get_object_or_404(Alumno, id=id)
    return render(request, '.html', {'alumno': alumno})

