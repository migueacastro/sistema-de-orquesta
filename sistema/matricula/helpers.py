from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
from django.forms.models import model_to_dict
from django.urls.resolvers import URLPattern
from django.utils.translation import gettext_lazy as _
from django.contrib import messages 


class NullableIntConverter:
    
    regex = r'\d*'
    name = 'nullable_int'

    def to_python(self, value):
        if value:
            return int(value)
        return None

    def to_url(self, value):
        return str(value) if value is not None else ''
    

def viewset(request, model, field_list, title, id=None):
    if id is None:
        match request.method:
            case 'GET':
                # Plantilla datatable
                query = model.objects.all()
                entries = [model_to_dict(i) for i in query]
                return render(request, 'administrador/table.html', {
                    'title': title, 
                    'entries': entries, 
                    'first_entry': entries[0] if len(entries) > 0 else None, 
                    'form':field_list
                    })
                
            case 'POST':
                # TODO: Crear forma de repetir formularios
                new_object = {}
                for field in field_list:
                    data = request.POST.get(field.get('name'))
                    new_object[field.name] = data
                    
                new_instance, created = model.objects.get_or_create(**new_object)
                if created:
                    messages.add_message(request, messages.SUCCESS, 'Registro agregado exitosamente.')
                else:
                    messages.add_message(request, messages.ERROR, 'Error al crear registro.')

                return render(request, 'administrador/table.html', {
                    'title': title, 
                    'entries': entries, 
                    'first_entry': entries[0] if len(entries) > 0 else None, 
                    'form':field_list
                    })
                
    else:
        entry = model.objects.get(id=id)
        match request.method:
            case 'GET':
                # Plantilla details
                return render(request, '', {'entry':entry})
            case 'PUT':
                # TODO: Manejar edicion de un registro
                instance_to_change = model.objects.get(id=id)
                try:

                    for field in field_list:
                        data = request.POST.get(field.get('name'))
                        setattr(instance_to_change, field.name, data)
                    instance_to_change.save()
                except Exception:
                    messages.add_message(request, messages.ERROR, 'Error al actualizar registro.')
                else:
                    messages.add_message(request, messages.SUCCESS, 'Registro actualizado exitosamente.')
                
                return render(request, '', {'entry':entry})
            case 'DELETE':
                # TODO: Manejar eliminación de un registro
                try:
                    model.objects.filter(id=id).delete()
                except Exception:
                    messages.add_message(request, messages.ERROR, 'Error al eliminar registro')
                else:
                    messages.add_message(request, messages.WARNING, 'Registro eliminado exitosamente.')
                return render(request, '', {'entry':entry})
    return redirect("/")



