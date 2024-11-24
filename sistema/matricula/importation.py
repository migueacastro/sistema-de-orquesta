from matricula.models import *
from matricula.tasks import leer_db_excel, ARCHIVO
import datetime

tabla = leer_db_excel(ARCHIVO)


LISTA_NO = ["NO", "N O", "NO APLICA", "MO", "NO ", "NO APLICA "]
LISTA_CATEDRAS_EXCLUIDAS = ["CORO INFANTIL", "CORO JUVENIL", "BAJO POPULAR"]
LISTA_MODELOS_EXCLUIDOS = ["ESTUDIANTES"]


# FUNCIONES DE IMPORTAR TABLAS 

# Para comprobar en tests.py si se ejecutaron correctamente, son de tipo booleano (Se ve feo)

def importar_medicamentos(tabla):
    for index, row in tabla.iterrows():
        if row["ALÉRGICO MEDICAMENTO"] not in LISTA_NO:
            Medicamento.objects.update_or_create(
                nombre=row["ALÉRGICO MEDICAMENTO"].strip(),
            ) 
    return True


def importar_tratamientos(tabla):
    for index, row in tabla.iterrows():
        if row["TRATAMIENTO"] not in LISTA_NO:
            Tratamiento.objects.update_or_create(
                nombre=row["TRATAMIENTO"].strip(),
            )
    return True

def importar_condiciones_especiales(tabla):
    for index, row in tabla.iterrows():
        if row["CONDICIÓN ESPECIAL"] not in LISTA_NO:
            CondicionEspecial.objects.update_or_create(
                nombre=row["CONDICIÓN ESPECIAL"].strip(),
            )
    return True
 

def importar_alergias(tabla):
    for index, row in tabla.iterrows():
        for key, col in row.items():
            if "ALÉRGICO" in key:
                Alergia.objects.update_or_create(
                    nombre=key.strip(),
                )
        return True
        
    

def importar_colores(tabla):
    for index, row in tabla.iterrows():
        if row["COLOR"] not in LISTA_NO:
            Color.objects.update_or_create(
                nombre=str(row["COLOR"]).strip(),
            )
    return True


def importar_categorias_instrumentos(tabla):
    for index, row in tabla.iterrows():
        for key, col in row.items():
            if "CÁTEDRA" in key and col not in LISTA_CATEDRAS_EXCLUIDAS:
                CategoriaInstrumento.objects.update_or_create(
                nombre=str(col).strip(),
            )
    return True        



def importar_marcas_instrumentos(tabla):
    for index, row in tabla.iterrows():
        if row["MARCA"] not in LISTA_NO:
            MarcaInstrumento.objects.update_or_create(
                nombre=row["MARCA"].strip(),
            )

    return True

def importar_modelos_instrumentos(tabla):
    for index, row in tabla.iterrows():
        if row["MODELO"] not in LISTA_MODELOS_EXCLUIDOS:
            categoria = None
            marca = None
            try:
                categoria = CategoriaInstrumento.objects.get(nombre=row["CÁTEDRA"].strip())
            except Exception:
                categoria = None
            
            try:
                marca = MarcaInstrumento.objects.get(nombre=row["MARCA"].strip())
            except Exception:
                marca = None
                

            ModeloInstrumento.objects.update_or_create(
                nombre=str(row["MODELO"]).strip(),
                marca=marca,
                categoria=categoria
            )

    return True


def importar_accesorios(tabla):
    for index, row in tabla.iterrows():
        if row["ACCESORIO"] not in LISTA_NO:
            MarcaInstrumento.objects.update_or_create(
                nombre=row["ACCESORIO"].strip()
            )
    return True


def importar_agrupaciones(tabla):
    for index, row in tabla.iterrows():
        if row["AGRUPACIÓN"] not in LISTA_NO:
            Agrupacion.objects.update_or_create(
                nombre=row["AGRUPACIÓN"].strip(),
            )

    return True

def importar_turnos(tabla):
    for index, row in tabla.iterrows():
        if row["TURNO"] not in LISTA_NO:
            Turno.objects.update_or_create(
                nombre=row["TURNO"].strip(),
            )

    return True

def importar_niveles_ts(tabla):
    for index, row in tabla.iterrows():
        if row["NIVEL T.S"] not in LISTA_NO:
            NivelTS.objects.update_or_create(
                nombre=row["NIVEL T.S"].strip(),
            )

    return True


def importar_niveles_estudiantiles(tabla):
    for index, row in tabla.iterrows():
        if row["NIVEL"] not in LISTA_NO:
            NivelEstudiantil.objects.update_or_create(
                nombre=row["NIVEL"].strip(),
            )

    return True


def importar_tipos_becas(tabla):
    TipoBeca.objects.update_or_create(nombre="Predeterminado")

    return True


def importar_tipos_catedras(tabla):
    for index, row in tabla.iterrows():
        for key, col in row.items():
            if "CÁTEDRA" in key:
                TipoCatedra.objects.update_or_create(
                    nombre=key.strip(),
                )
        return True
    

def importar_catedras(tabla):
   
    for index, row in tabla.iterrows():
        for key, col in row.items():
            if "CÁTEDRA" in key and row[key] not in LISTA_NO: 
                tipo = None
                try:
                    tipo = TipoCatedra.objects.get(nombre=key.strip())
                except Exception:
                    tipo = None
                
                Catedra.objects.update_or_create(
                    nombre=str(row[key]).strip(),
                    tipo=tipo,
                )
    
    return True        
            

def importar_programas(tabla):
    for index, row in tabla.iterrows():
        if row["PROGRAMA"] not in LISTA_NO:
            Programa.objects.update_or_create(
                nombre=row["PROGRAMA"].strip(),
            )

    return True

def importar_representantes(tabla):
    for index, row in tabla.iterrows():
        if row["CÉDULA4"] not in LISTA_NO:
            cedula = str(row["CÉDULA4"]).strip() if row["CÉDULA4"] not in LISTA_NO else None
            nombre = str(row["NOMBRES2"]).strip() if row["NOMBRES2"] not in LISTA_NO else None
            telefono = str(row["TELÉFONO5"]).strip() if row["TELÉFONO5"] not in LISTA_NO else None
            parentesco = str(row["PARENTESCO"]).strip() if row["PARENTESCO"] not in LISTA_NO else None
            email = str(row["E-MAIL"]).strip() if row["E-MAIL"] not in LISTA_NO else None
            

            Representante.objects.update_or_create(
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
        lista_quien_retira = lista_quien_retira.replace(" O ", " ").replace(" Y ", " ")
        lista_quien_retira = lista_quien_retira.split(" ")
        
        if len(lista_quien_retira) > 1:
            for nombre in lista_quien_retira:
                if nombre not in LISTA_NO:
                    QuienRetira.objects.update_or_create(nombre=nombre)
        else:
            QuienRetira.objects.update_or_create(nombre=lista_quien_retira[0])

    return True


def importar_alumnos(tabla):
    for index, row in tabla.iterrows():
        nombre = row["NOMBRES"] if row["NOMBRES"] not in LISTA_NO else ""
        apellido = row["APELLIDOS"] if row["APELLIDOS"] not in LISTA_NO else ""
        cedula = row["CÉDULA"] if row["CÉDULA"] not in LISTA_NO else None
        edad = int(row["EDAD"]) if row["EDAD"] not in LISTA_NO else None
        sexo = "Masculino" if row["SEXO"].strip() == "M" else "Femenino"
        telefono = row["TELÉFONO"].strip() if row["TELÉFONO"] not in LISTA_NO else None
        direccion = row["DIRECCIÓN"].strip() if row["DIRECCIÓN"] not in LISTA_NO else None

        fecha_nacimiento = row["FECHA DE NACIMIENTO"]
        try:
            fecha_nacimiento = datetime.datetime.strptime(str(fecha_nacimiento), "%d/%m/%Y")
        except Exception as e:
            
            try:
                fecha_nacimiento = datetime.datetime.strptime(str(fecha_nacimiento), "%Y-%m-%d")
            except Exception as e:
                try:
                    fecha_nacimiento = datetime.datetime.strptime(str(fecha_nacimiento), "%Y-%m-%d %H:%M:%S")
                except Exception as e:
                    fecha_nacimiento = None
        

        turno = None
        try:
            turno = Turno.objects.get(nombre=row["TURNO"].strip())
        except Exception:
            turno = None

        nivel_estudiantil = None
        try:
            nivel_estudiantil = NivelEstudiantil.objects.get(nombre=row["NIVEL"].strip())
        except Exception:
            nivel_estudiantil = None
        
        nivel_ts = None
        try:
            nivel_ts = NivelTS.objects.get(nombre=row["NIVEL T.S"].strip())
        except Exception:
            nivel_ts = None

        programa = None
        try:
            programa = Programa.objects.get(nombre=row["PROGRAMA"].strip())
        except Exception as e:
            print(e)
            programa = None

        agrupacion = None
        try:
            agrupacion = Agrupacion.objects.get(nombre=row["AGRUPACIÓN"].strip())
        except Exception:
            agrupacion = None
        

        condicion_especial = None
        try:
            condicion_especial = CondicionEspecial.objects.get(nombre=row["CONDICIÓN ESPECIAL"].strip())
        except Exception:
            condicion_especial = None

        
    
        

        alumno, created = Alumno.objects.update_or_create(
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
            programa=programa,
            condicion_especial=condicion_especial,
            agrupacion=agrupacion

        )
        
        try:
            representante = Representante.objects.get(cedula=row["CÉDULA4"].strip())
            alumno.representantes.add(representante)
            
        except Exception:
            representante = None
        
        for key, col in row.items():
            if "ALÉRGICO" in key:
                try:
                    alergia = Alergia.objects.get(nombre=col.strip())
                    alumno.alergias.add(alergia)
                except Exception:
                    continue
        
        try:
            tratamiento = Tratamiento.objects.get(nombre=row["TRATAMIENTO"].strip())
            alumno.tratamientos.add(tratamiento)
        except Exception:
            tratamiento = None

        lista_quien_retira = row["QUIEN RETIRA"].strip()
        lista_quien_retira = row["QUIEN RETIRA"].strip()
        lista_quien_retira = lista_quien_retira.replace(" O ", " ").replace(" Y ", " ")
        lista_quien_retira = lista_quien_retira.split(" ")
        
        if len(lista_quien_retira) > 1: 
            for nombre in lista_quien_retira:
                if nombre not in LISTA_NO:
                    try:
                        nuevo_quien_retira = QuienRetira.objects.get(nombre=nombre.strip())
                        alumno.quien_retiras.add(nuevo_quien_retira)
                    except Exception as e:
                        print(e)
        else:
            try:
                nuevo_quien_retira = QuienRetira.objects.get(nombre=lista_quien_retira[0].strip())
                alumno.quien_retiras.add(nuevo_quien_retira)
            except Exception as e:
                print(e)

        
        for key, col in row.items():
            if "CÁTEDRA" in key:
                nombre_catedra = str(row[key]).strip()
                try:
                    catedra = Catedra.objects.get(nombre=nombre_catedra)
                except Exception:
                    catedra = None

                alumno.catedras.add(catedra)

        alumno.save()
    print(Alumno.objects.all().count())
    return Alumno.objects.all().count() > 0


def importar_instrumentos(tabla):
    for index, row in tabla.iterrows():
        if row["MODELO"] not in LISTA_MODELOS_EXCLUIDOS and row["SERIAL"] not in LISTA_NO:
            modelo = None
            color = None
            accesorio = None
            serial = row["SERIAL"]
            alumno = None

            try:
                modelo = CategoriaInstrumento.objects.get(nombre=row["CÁTEDRA"].strip())
            except Exception:
                modelo = None

            try:
                color = Color.objects.get(nombre=row["COLOR"].strip())
            except Exception:
                color = None
                
            try:
                accesorio = Accesorio.objects.get(nombre=row["ACCESORIO"].strip())
            except Exception:
                accesorio = None

            try:
                alumno = Alumno.objects.get(nombre=row["NOMBRES"], apellido=row["APELLIDOS"])
            except Exception:
                alumno = None

            Instrumento.objects.update_or_create(
                nombre="",
                modelo=modelo,
                color=color,
                serial=serial,
                accesorio=accesorio,
                alumno=alumno
            )

    return True


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
            Becado.objects.update_or_create(
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
                try:
                    fecha_inscripcion = datetime.datetime.strptime(str(fecha_inscripcion), "%Y-%m-%d %H:%M:%S")
                except Exception as e:
                    fecha_inscripcion = None

        Inscripcion.objects.update_or_create(
            alumno=alumno,
            turno=turno,
            fecha_inscripcion=fecha_inscripcion
        )

    return True