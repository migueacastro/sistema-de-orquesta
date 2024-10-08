import pandas as pd
#from matricula.models import *
from matricula.importation import *


ARCHIVO = {
    "nombre": "matriculasf.xlsm",
    "rango_columnas": ["A", "AJ"],
    "omitir_filas": 4,
    "tabla": "BD"
}


def leer_db_excel(archivo):
    tabla = pd.read_excel(
        archivo["nombre"], sheet_name=archivo["tabla"], 
        usecols=f'{archivo["rango_columnas"][0]}:{archivo["rango_columnas"][1]}', 
        skiprows=archivo["omitir_filas"]
    )

    return tabla

leer_db_excel(ARCHIVO)