from matricula.models import *
from matricula.tasks import leer_db_excel, ARCHIVO
import datetime

tabla = leer_db_excel(ARCHIVO)


LISTA_NO = ["NO", "N O", "NO APLICA"]
LISTA_CATEDRAS_EXCLUIDAS = ["CORO INFANTIL", "CORO JUVENIL", "BAJO POPULAR"]
LISTA_MODELOS_EXCLUIDOS = ["ESTUDIANTES"]


# FUNCIONES DE IMPORTAR TABLAS 

# Para comprobar en tests.py si se ejecutaron correctamente, son de tipo booleano (Se ve feo)

def importar_medicamentos(tabla):
    for index, row in tabla.iterrows():
        if row["ALÉRGICO MEDICAMENTO"] not in LISTA_NO:
            Medicamento.objects.get_or_create(
                nombre=row["ALÉRGICO MEDICAMENTO"],
            ) 
    return True


def importar_tratamientos(tabla):
    for index, row in tabla.iterrows():
        if row["TRATAMIENTO"] not in LISTA_NO:
            Tratamiento.objects.get_or_create(
                nombre=row["TRATAMIENTO"],
            )
    return True

def importar_condiciones_especiales(tabla):
    for index, row in tabla.iterrows():
        if row["CONDICIÓN ESPECIAL"] not in LISTA_NO:
            CondicionEspecial.objects.get_or_create(
                nombre=row["CONDICIÓN ESPECIAL"],
            )
    return True
 

def importar_alergias(tabla):
    for index, row in tabla.iterrows():
        for key, col in row.items():
            if "ALÉRGICO" in key:
                Alergia.objects.get_or_create(
                    nombre=key,
                )
        return True
        
    

def importar_colores(tabla):
    for index, row in tabla.iterrows():
        if row["COLOR"] not in LISTA_NO:
            Color.objects.get_or_create(
                nombre=row["COLOR"],
            )
    return True


def importar_categorias_instrumentos(tabla):
    for index, row in tabla.iterrows():
        for key, col in row.items():
            if "CÁTEDRA" in key and col not in LISTA_CATEDRAS_EXCLUIDAS:
                CategoriaInstrumento.objects.get_or_create(
                nombre=col,
            )
    return True        



def importar_marcas_instrumentos(tabla):
    for index, row in tabla.iterrows():
        if row["MARCA"] not in LISTA_NO:
            MarcaInstrumento.objects.get_or_create(
                nombre=row["MARCA"],
            )

    return True

def importar_modelos_instrumentos(tabla):
    for index, row in tabla.iterrows():
        if row["MODELO"] not in LISTA_MODELOS_EXCLUIDOS:
            categoria = None
            marca = None
            try:
                categoria = CategoriaInstrumento.objects.get(nombre=row["CÁTEDRA"])
            except Exception:
                categoria = None
            
            try:
                marca = MarcaInstrumento.objects.get(nombre=row["MARCA"])
            except Exception:
                marca = None
                

            ModeloInstrumento.objects.get_or_create(
                nombre=row["MODELO"],
                marca=marca,
                categoria=categoria
            )

    return True


def importar_accesorios(tabla):
    for index, row in tabla.iterrows():
        if row["ACCESORIO"] not in LISTA_NO:
            MarcaInstrumento.objects.get_or_create(
                nombre=row["ACCESORIO"],
            )
    return True

def importar_instrumentos(tabla):
    for index, row in tabla.iterrows():
        if row["MODELO"] not in LISTA_MODELOS_EXCLUIDOS:
            modelo = None
            color = None
            accesorio = None
            serial = row["SERIAL"]

            try:
                modelo = CategoriaInstrumento.objects.get(nombre=row["CÁTEDRA"])
            except Exception:
                modelo = None

            try:
                color = Color.objects.get(nombre=row["COLOR"])
            except Exception:
                color = None
                
            try:
                accesorio = Accesorio.objects.get(nombre=row["ACCESORIO"])
            except Exception:
                accesorio = None

            Instrumento.objects.get_or_create(
                nombre="",
                modelo=modelo,
                color=color,
                serial=serial,
                accesorio=accesorio
            )

    return True

def importar_agrupaciones(tabla):
    for index, row in tabla.iterrows():
        if row["AGRUPACIÓN"] not in LISTA_NO:
            Agrupacion.objects.get_or_create(
                nombre=row["AGRUPACIÓN"],
            )

    return True

def importar_turnos(tabla):
    for index, row in tabla.iterrows():
        if row["TURNO"] not in LISTA_NO:
            Turno.objects.get_or_create(
                nombre=row["TURNO"],
            )

    return True

def importar_niveles_ts(tabla):
    for index, row in tabla.iterrows():
        if row["NIVEL T.S"] not in LISTA_NO:
            NivelTS.objects.get_or_create(
                nombre=row["NIVEL T.S"],
            )

    return True


def importar_niveles_estudiantiles(tabla):
    for index, row in tabla.iterrows():
        if row["NIVEL"] not in LISTA_NO:
            NivelEstudiantil.objects.get_or_create(
                nombre=row["NIVEL"],
            )

    return True


def importar_tipos_becas(tabla):
    TipoBeca.objects.get_or_create(nombre="Predeterminado")

    return True


def importar_tipos_catedras(tabla):
    for index, row in tabla.iterrows():
        for key, col in row.items():
            if "CÁTEDRA" in key:
                TipoCatedra.objects.get_or_create(
                    nombre=key,
                )
        return True
    

def importar_catedras(tabla):
   
    for index, row in tabla.iterrows():
        for key, col in row.items():
            if "CÁTEDRA" in key:
                tipo = None
                instrumento = None
                try:
                    tipo = TipoCatedra.objects.get(nombre=key)
                    if tipo not in LISTA_CATEDRAS_EXCLUIDAS:
                        try:
                            instrumento = Instrumento.objects.get(nombre=row[key])
                        except Exception:
                            instrumento = None
                except Exception:
                    tipo = None
                
                Catedra.objects.get_or_create(
                    nombre=row[key],
                    tipo=tipo,
                    instrumento=instrumento
                )
    
    return True        
            

def importar_programas(tabla):
    for index, row in tabla.iterrows():
        if row["PROGRAMA"] not in LISTA_NO:
            agrupacion = None
            try:
                agrupacion = Agrupacion.objects.get(nombre=row["AGRUPACIÓN"])
            except Exception:
                agrupacion = None
            

            Programa.objects.get_or_create(
                nombre=row["PROGRAMA"],
                agrupacion=agrupacion,
            )

    return True

def importar_representantes(tabla):
    for index, row in tabla.iterrows():
        if row["CÉDULA4"] not in LISTA_NO:
            cedula = row["CÉDULA4"] if row["CÉDULA4"] not in LISTA_NO else None
            nombre = row["NOMBRES2"] if row["NOMBRES2"] not in LISTA_NO else None
            telefono = row["TELÉFONO5"] if row["TELÉFONO5"] not in LISTA_NO else None
            parentesco = row["PARENTESCO"] if row["PARENTESCO"] not in LISTA_NO else None
            email = row["E-MAIL"] if row["E-MAIL"]not in LISTA_NO else None
            

            Representante.objects.get_or_create(
                cedula=cedula,
                nombre=nombre,
                telefono=telefono,
                parentesco=parentesco,
                email=email
            )


    return True


def importar_quienretira(tabla):
    for index, row in tabla.iterrows():
        lista_quien_retira = row["QUIEN RETIRA"].strip()

        if " O " in lista_quien_retira:
            lista_quien_retira = lista_quien_retira.split(" O ")
        elif " Y " in lista_quien_retira:
            lista_quien_retira = lista_quien_retira.split(" Y ")
        
        for nombre in lista_quien_retira:
            if nombre not in LISTA_NO:
                QuienRetira.objects.get_or_create(nombre=nombre)

    return True


def importar_alumnos(tabla):
    for index, row in tabla.iterrows():
        nombre = row["NOMBRES"] if row["NOMBRES"] not in LISTA_NO else ""
        apellido = row["APELLIDOS"] if row["APELLIDOS"] not in LISTA_NO else ""
        cedula = row["CÉDULA"] if row["CÉDULA"] not in LISTA_NO else None
        edad = int(row["EDAD"]) if row["EDAD"] not in LISTA_NO else None
        sexo = "Masculino" if row["SEXO"] == "M" else "Femenino"
        telefono = row["TELÉFONO"] if row["TELÉFONO"] not in LISTA_NO else None
        direccion = row["DIRECCIÓN"] if row["DIRECCIÓN"] not in LISTA_NO else None

        fecha_nacimiento = row["FECHA DE NACIMIENTO"]
        try:
            datetime.datetime.strptime(str(fecha_nacimiento), "%d/%m/%Y")
        except Exception as e:
            
            try:
                fecha_nacimiento = datetime.datetime.strptime(str(fecha_nacimiento), "%Y-%m-%d")
            except Exception as e:
                fecha_nacimiento = datetime.datetime.strptime(str(fecha_nacimiento), "%Y-%m-%d %H:%M:%S")
            
        print(fecha_nacimiento)
        turno = None
        try:
            turno = Turno.objects.get(nombre=row["TURNO"])
        except Exception:
            turno = None

        nivel_estudiantil = None
        try:
            nivel_estudiantil = NivelEstudiantil.objects.get(nombre=row["NIVEL"])
        except Exception:
            nivel_estudiantil = None
        
        nivel_ts = None
        try:
            nivel_ts = NivelTS.objects.get(nombre=row["NIVEL T.S"])
        except Exception:
            nivel_ts = None

        try:
            programa = Programa.objects.get(nombre=row["PROGRAMA"])
        except Exception:
            programa = None
        

        alumno, created = Alumno.objects.get_or_create(
            nombre=nombre,
            apellido=apellido,
            cedula=cedula,
            edad=edad,
            sexo=sexo,
            telefono=telefono,
            fecha_nacimiento=fecha_nacimiento,
            turno=turno,
            nivel_estudiantil=nivel_estudiantil,
            nivel_ts=nivel_ts,
            direccion=direccion,
            programa=programa

        )
        
        try:
            instrumento = Instrumento.objects.get(serial=row["SERIAL"])
            alumno.instrumentos.add(instrumento)
        except Exception:
            instrumento = None
        
        try:
            representante = Representante.objects.get(cedula=row["CÉDULA4"])
            alumno.representantes.add(representante)
            
        except Exception:
            representante = None
        
        for key, col in row.items():
            if "ALÉRGICO" in key:
                try:
                    alergia = Alergia.objects.get(nombre=col)
                    alumno.alergias.add(alergia)
                except Exception:
                    continue
        
        try:
            tratamiento = Tratamiento.objects.get(nombre=row["TRATAMIENTO"])
            alumno.tratamientos.add(tratamiento)
        except Exception:
            tratamiento = None

        lista_quien_retira = row["QUIEN RETIRA"].strip()

        if " O " in lista_quien_retira:
            lista_quien_retira = lista_quien_retira.split(" O ")
        elif " Y " in lista_quien_retira:
            lista_quien_retira = lista_quien_retira.split(" Y ")
        
        

        for nombre in lista_quien_retira:
            if nombre not in LISTA_NO:
                try:
                    nuevo_quien_retira = QuienRetira.objects.get(nombre=nombre)
                    alumno.quien_retiras.add(nuevo_quien_retira)
                except Exception as e:
                    print(e)
                    continue
    print(Alumno.objects.all().count())
    return Alumno.objects.all().count() > 0


def importar_becados(tabla):
    for index, row in tabla.iterrows():
        if row["BECADO"] not in LISTA_NO and row["BECADO"] == "SI":
            alumno = None
            try:
                alumno = Alumno.objects.filter(nombre=row["NOMBRES"], apellido=row["APELLIDOS"]).first()
                continue
            except Exception as e:
                print(alumno,row["NOMBRES"], e)
            
            try:
                tipo = TipoBeca.objects.get(nombre="Predeterminado")
            except Exception as e:
                print(e)
                continue 
            Becado.objects.get_or_create(
                alumno=alumno,
                tipo=tipo
            )

    return True

def importar_inscripciones(tabla):
    
    for index, row in tabla.iterrows():
        try:
            alumno = Alumno.objects.filter(nombre=row["NOMBRES"], apellido=row["APELLIDOS"]).first()
        except Exception:
            alumno = None

        try:
            turno = Turno.objects.get(nombre=row["TURNO"])
        except Exception:
            turno = None
        

        fecha_inscripcion = row["FECHA DE INSCRIPCIÓN"]

        try:
            fecha_inscripcion = datetime.datetime.strptime(str(fecha_inscripcion), "%d/%m/%Y")
        except Exception as e:
            try: 
                fecha_inscripcion = datetime.datetime.strptime(str(fecha_inscripcion), "%Y-%m-%d")
            except Exception as e:
                fecha_inscripcion = datetime.datetime.strptime(str(fecha_inscripcion), "%Y-%m-%d %H:%M:%S")
            print(fecha_inscripcion)

        Inscripcion.objects.get_or_create(
            alumno=alumno,
            turno=turno,
            fecha_inscripcion=fecha_inscripcion
        )

    return True


