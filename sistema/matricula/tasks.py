import pandas as pd
#from matricula.models import *



ARCHIVO = {
    "nombre": "matriculasf.xlsm",
    "rango_columnas": ["A", "AJ"],
    "omitir_filas": 4,
    "tabla": "BD"
}


def leer_db_excel(archivo):
    tabla = pd.read_excel(
        "matriculasf.xlsm", sheet_name="BD", 
        usecols=f'A:AJ', 
        skiprows=4
    )

    return tabla

"""def leer_db_excel(archivo):
    tabla = pd.read_excel(
        archivo["nombre"], sheet_name=archivo["tabla"], 
        usecols=f'{archivo["rango_columnas"][0]}:{archivo["rango_columnas"][1]}', 
        skiprows=archivo["omitir_filas"]
    )

    return tabla
"""
def ejecutar_importaciones(archivo):
    import matricula.importation as a
    for i in dir(a):
        item = getattr(a, i)
        if callable(item):
            item(archivo)

