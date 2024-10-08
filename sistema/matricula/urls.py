from django.urls import path
from matricula.views import *

urlpatterns = [
    path('importar-archivo/', importar_archivo, name="importar-archivo"),
]
