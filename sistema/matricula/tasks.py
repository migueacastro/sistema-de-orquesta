import pandas as pd
#from matricula.models import *



ARCHIVO = {
    "nombre": "matriculas.xlsm",
    "rango_columnas": ["A", "AJ"],
    "omitir_filas": 4,
    "tabla": "BD"
} 
def leer_db_excel(archivo):
    tabla = pd.read_excel(
        "matriculas.xlsm", sheet_name="BD", 
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
    #for i in dir(a):
    #    item = getattr(a, i)
    #    if callable(item):
    #        item(archivo)
    a.importar_medicamentos(archivo)
    a.importar_tratamientos(archivo)
    a.importar_condiciones_especiales(archivo)
    a.importar_alergias(archivo)
    a.importar_colores(archivo)
    a.importar_categorias_instrumentos(archivo)
    a.importar_marcas_instrumentos(archivo)
    a.importar_modelos_instrumentos(archivo)
    a.importar_accesorios(archivo)
    a.importar_agrupaciones(archivo)
    a.importar_turnos(archivo)
    a.importar_niveles_ts(archivo)
    a.importar_niveles_estudiantiles(archivo)
    a.importar_tipos_becas(archivo)
    a.importar_tipos_catedras(archivo)
    a.importar_catedras(archivo)
    a.importar_programas(archivo)
    a.importar_representantes(archivo)
    a.importar_quienretira(archivo)
    a.importar_alumnos(archivo)
    a.importar_instrumentos(archivo)
    a.importar_becados(archivo)
    a.importar_inscripciones(archivo)

