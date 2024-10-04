from django.forms.models import model_to_dict
from matricula.models import *

LISTA_NO = ["NO", "N O"]
# FUNCIONES DE IMPORTAR TABLAS 

def importar_medicamentos(tabla):
    for row in tabla.iterrows():
        if row["ALÉRGICO MEDICAMENTO"] not in LISTA_NO:
            Medicamento.objects.get_or_create(
                nombre=row["ALÉRGICO MEDICAMENTO"],
            ) 

def importar_tratamientos(tabla):
    for row in tabla.iterrows():
        if row["TRATAMIENTO"] not in LISTA_NO:
            Tratamiento.objects.get_or_create(
                nombre=row["TRATAMIENTO"],
            )

def importar_condiciones_especiales(tabla):
    for row in tabla.iterrows():
        if row["CONDICIÓN ESPECIAL"] not in LISTA_NO:
            CondicionEspecial.objects.get_or_create(
                nombre=row["CONDICIÓN ESPECIAL"],
            )

def importar_tipos_alergias(tabla):
    for row in tabla.iterrows():
        for key, col in row:
            if "ALÉRGICO" in key:
                TipoAlergia.objects.get_or_create(
                    nombre=key,
                )
        return

def importar_alergias(tabla):
    pass

def importar_colores(tabla):
    pass

def importar_categorias_instrumentos(tabla):
    pass

def importar_marcas_instrumentos(tabla):
    pass

def importar_modelos_instrumentos(tabla):
    pass

def importar_accesorios(tabla):
    pass

def importar_instrumentos(tabla):
    pass

def importar_agrupaciones(tabla):
    pass

def importar_turnos(tabla):
    pass

def importar_niveles_tls(tabla):
    pass

def importar_niveles_estudiantiles(tabla):
    pass

def importar_tipos_becas(tabla):
    pass

def importar_becas(tabla):
    pass

def importar_representantes(tabla):
    pass

def importar_alumnos(tabla):
    pass

def importar_alumnos(tabla):
    pass

def importar_becados(tabla):
    pass

def importar_programas(tabla):
    pass

def importar_quienretira(tabla):
    pass

def importar_inscripciones(tabla):
    pass

def importar_tipos_catedras(tabla):
    pass

def importar_catedras(tabla):
    pass

