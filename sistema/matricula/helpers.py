from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
from django.forms.models import model_to_dict
from django.urls.resolvers import URLPattern
from django.utils.translation import gettext_lazy as _


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
            case "GET":
                # Plantilla datatable
                query = model.objects.all()
                entries = [model_to_dict(i) for i in query]
                return render(request, 'administrador/table.html', {
                    'title': title, 
                    'entries': entries, 
                    'first_entry': entries[0] if len(entries) > 0 else None, 
                    'form':field_list
                    })
                
            case "POST":
                # TODO: Crear forma de repetir formularios
                return render(request, 'administrador/table.html', {
                    'title': title, 
                    'entries': entries, 
                    'first_entry': entries[0] if len(entries) > 0 else None, 
                    'form':field_list
                    })
                
    else:
        match request.method:
            case "GET":
                # Plantilla details
                entry = model.objects.get(id=id)
                return render(request, "")
            case "PUT":
                # TODO: Manejar edicion de un registro
                return render(request, "")
            case "DELETE":
                # TODO: Manejar eliminación de un registro
                return render(request, "")
    return redirect("/")