from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import *
from django.contrib import messages
from django.forms.models import model_to_dict

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
    return render(request, 'administrador/home.html', {'title': "Inicio", "alumnos":alumnos})

def listar_alumnos(request):
    alumnos = Alumno.objects.all()
    return render(request, '.html', {'alumnos': alumnos})

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

def alergias(request):
    title = 'alergias'
    query = Alergia.objects.all()
    entries = [model_to_dict(i) for i in query]
    return render(request, 'administrador/table.html', {'title': title, 'entries': entries, 'first_entry': entries[0]})

def tratamientos(request):
    title = 'tratamientos'
    query = Tratamiento.objects.all()
    entries = [model_to_dict(i) for i in query]
    return render(request, 'administrador/table.html', {'title': title, 'entries': entries, 'first_entry': entries[0] if len(entries) > 0 else None})

def accesorios(request):
    title = 'accesorios'
    query = Accesorio.objects.all()
    entries = [model_to_dict(i) for i in query]
    return render(request, 'administrador/table.html', {'title': title, 'entries': entries, 'first_entry': entries[0] if len(entries) > 0 else None})

def colores(request):
    title = 'colores'
    query = Color.objects.all()
    entries = [model_to_dict(i) for i in query]
    return render(request, 'administrador/table.html', {'title': title, 'entries': entries, 'first_entry': entries[0] if len(entries) > 0 else None})