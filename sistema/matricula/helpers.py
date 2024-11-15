from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
from django.forms.models import model_to_dict
from itertools import chain
from django.urls.resolvers import URLPattern
from django.utils.translation import gettext_lazy as _
from django.contrib import messages 
from django.apps import apps


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
    

def viewset(request, model, field_list, title, id=None):
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
                    'form':field_list
                    })
                
            case 'POST':
                # TODO: Crear forma de repetir formularios
                new_object = {}
                many_to_many_fields = {}
                for field in field_list:
                    data = request.POST.get(field['name'])
                    if data == 'None' or data == '' or data == ' ':
                        data = None
                    if field['type'] == 'manytomany' and data:
                        many_to_many_fields[field['name']] = data.split(",")
                    else:
                        if data:
                            new_object[field['name']] = data
                    
                new_instance, created = model.objects.get_or_create(**new_object)
                if created:
                    for key, value in many_to_many_fields.items():
                        many_to_many_setter = getattr(new_instance, key)
                        many_to_many_setter.set(value)
                        
                    messages.add_message(request, messages.SUCCESS, 'Registro agregado exitosamente.')
                else:
                    messages.add_message(request, messages.ERROR, 'Error al crear registro.')
                entries = [model_to_dict(i) for i in model.objects.all()]
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
                for field in field_list:
                    field["value"] = model_to_dict(entry).get(field["name"])
                return render(request, 'administrador/details.html', {'entry':entry, 'title':title[:-1], 'form':field_list})
            case 'POST':
                
                instance_to_change = model.objects.get(id=id)
                try:

                    for field in field_list:
                        data = request.POST.get(field['name'])
                        if data == 'None' or data == '' or data == ' ':
                            data = None
                            
                        if field['type'] == 'manytomany' and data:
                            many_to_many_setter = getattr(instance_to_change, field['name'])
                            many_to_many_setter.clear()
                            many_to_many_setter.set(data.split(","))
                                
                        else:     
                            if data:
                                setattr(instance_to_change, field['name'], data)
                    instance_to_change.save()
                    messages.add_message(request, messages.SUCCESS, 'Registro actualizado exitosamente.')
                except Exception:
                    messages.add_message(request, messages.ERROR, 'Error al actualizar registro.')
                
                entry = instance_to_change
                for field in field_list:
                    field["value"] = model_to_dict(entry).get(field["name"])
                return render(request, 'administrador/details.html', {'entry':entry, 'title':title[:-1], 'form':field_list})
            case 'DELETE':
                
                model_to_delete = model.objects.get(id=id)
                model_to_delete.activo = False
                model_to_delete.save()
                return HttpResponse(400)
                
    return redirect("/")



