from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
from django.forms.models import model_to_dict
from itertools import chain
from django.urls.resolvers import URLPattern
from django.utils.translation import gettext_lazy as _
from django.contrib import messages 
from .forms import *
from django.apps import apps

DICCIONARIO_FORMULARIOS = {
    'medicamento': MedicamentoForm(),
    'tratamiento': TratamientoForm(),
    'condicion_especial': CondicionEspecialForm(),
    'alergias': AlergiaForm(),
    'color': ColorForm(),
    'categoria': CategoriaInstrumentoForm(),
    'marca': MarcaInstrumentoForm(),
    'modelo': ModeloInstrumentoForm(),
    'accesorio': AccesorioForm(),
    'agrupacion': AgrupacionForm(),
    'turno': TurnoForm(),
    'nivel_ts': NivelTSForm(),
    'nivel_estudiantil': NivelEstudiantilForm(),
    'tipo_beca': TipoBecaForm(),
    'representantes': RepresentanteForm(),
    'programa': ProgramaForm(),
    'quien_retira': QuienRetiraForm(),
    'tipo_catedra': TipoCatedraForm(),
    'catedras': CatedraForm(),
    'alumno': AlumnoForm(),
    'instrumentos': InstrumentoForm(),
    'becado': BecadoForm(),
    'inscripcion': InscripcionForm(),
}
DICCIONARIO_ENDPOINTS = {
    'medicamento': 'medicamentos',
    'tratamiento': 'tratamientos',
    'condicion_especial': 'condiciones-especiales',
    'alergias': 'alergias',
    'color': 'colores',
    'categoria': 'categorias-instrumentos',
    'marca': 'marcas-instrumentos',
    'modelo': 'modelos-instrumentos',
    'accesorio': 'accesorios',
    'agrupacion': 'agrupaciones',
    'turno': 'turnos',
    'nivel_ts': 'niveles-ts',
    'nivel_estudiantil': 'niveles-estudiantiles',
    'tipo_beca': 'tipos-becas',
    'representantes': 'representantes',
    'programa': 'programas',
    'quien_retira': 'quienes-retiran',
    'tipo_catedra': 'tipos-catedras',
    'catedras': 'catedras',
    'alumno': 'alumnos',
    'instrumentos': 'instrumentos',
    'becado': 'becados',
    'inscripcion': 'inscripciones',
}

def model_to_dict_better(instance, fields=None, exclude=None):
    opts = instance._meta
    data = {}
    for f in chain(opts.concrete_fields, opts.private_fields, opts.many_to_many): 
        if not getattr(f, "editable", False): 
            continue 
        if fields is not None and f.name not in fields: 
            continue 
        if exclude and f.name in exclude: 
            continue 
        value = f.value_from_object(instance) 
        if f.many_to_many: # Manejo de muchos-a-muchos 
            data[f.name] = ""
            for item in value:
                data[f.name] = data[f.name] + str(item.nombre) + "," 
            data[f.name] = data[f.name][:-1]

        elif f.is_relation and f.many_to_one: # Manejo de claves foráneas 
            related_object = getattr(instance, f.name) 
            if related_object: 
                data[f.name] = str(related_object.nombre)
            else: 
                data[f.name] = None 
        else: 
            data[f.name] = value
    if isinstance(instance, apps.get_model('matricula', 'Alumno')): 
        instrumentos = instance.instrumentos.all() 
        data['instrumentos'] = ", ".join([str(instrumento.serial) for instrumento in instrumentos])
    return data

class NullableIntConverter:
    
    regex = r'\d*'
    name = 'nullable_int'

    def to_python(self, value):
        if value:
            return int(value)
        return None

    def to_url(self, value):
        return str(value) if value is not None else ''
    

def viewset(request, model, field_list, title, model_form, main_endpoint, id=None):
    if id is None:
        match request.method:
            case 'GET':
                # Plantilla datatable
                query = model.objects.filter(activo=True)
                entries = [model_to_dict_better(i) for i in query]
                return render(request, 'administrador/table.html', {
                    'title': title, 
                    'entries': entries, 
                    'first_entry': entries[0] if len(entries) > 0 else None, 
                    'forms':DICCIONARIO_FORMULARIOS,
                    'model_form':model_form(),
                    'endpoints': DICCIONARIO_ENDPOINTS,
                    'main_endpoint': main_endpoint
                    })
                
            case 'POST':
                # TODO: Crear forma de repetir formularios
                form = model_form(request.POST) 
                if form.is_valid(): 
                    form.save() 
                    return JsonResponse({'success': True}) 
                else: 
                    return JsonResponse({'success': False, 'errors': form.errors})
                
    else:
        entry = model.objects.get(id=id)
        match request.method:
            case 'GET':
                for field in field_list:
                    field["value"] = model_to_dict(entry).get(field["name"])
                return render(request, 'administrador/details.html', {'entry':entry, 'title':title[:-1], 'forms':DICCIONARIO_FORMULARIOS, 'model_form':model_form(instance=entry), 'endpoints': DICCIONARIO_ENDPOINTS, 'main_endpoint': main_endpoint})
            case 'POST':  
                form = model_form(request.POST, instance = entry)
                print(request.POST) 
                if form.is_valid(): 
                    form.save() 
                    return JsonResponse({'success': True}) 
                else: 
                    return JsonResponse({'success': False, 'errors': form.errors})
            case 'DELETE':
                
                model_to_delete = model.objects.get(id=id)
                model_to_delete.activo = False
                model_to_delete.save()
                return HttpResponse(400)
                
    return redirect("/")



