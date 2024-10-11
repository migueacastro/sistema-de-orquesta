from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
from matricula.models import *
from matricula.tasks import *
def importar_archivo(request):
        
        ARCHIVONUEVO = {
            "nombre": "matriculasf.xlsm",
            "rango_columnas": ["A", "AJ"],
            "omitir_filas": 4,
            "tabla": "BD"
        }

        ejecutar_importaciones(leer_db_excel(ARCHIVONUEVO))
        return HttpResponse("Codigo 200: Funciono (?)")
    
        #return HttpResponse(f"Error: {str(e)}\nSapeee")
    

    