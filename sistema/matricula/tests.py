from django.test import TestCase
from matricula.importation import *
from matricula.tasks import *

# Create your tests here.

class ImportationTestCase(TestCase):
    tabla = leer_db_excel(ARCHIVO)
    
    def test_medicamentos(self):
        self.assertTrue(importar_medicamentos(self.tabla))
    
    def test_tratamientos(self):
        self.assertTrue(importar_tratamientos(self.tabla))

    def test_condiciones(self):
        self.assertTrue(importar_condiciones_especiales(self.tabla))

    def test_alergias(self):
        self.assertTrue(importar_alergias(self.tabla))
    
    def test_colores(self):
        self.assertTrue(importar_colores(self.tabla))
    
    def test_categorias_instrumentos(self):
        self.assertTrue(importar_categorias_instrumentos(self.tabla))

    def test_marcas_instrumentos(self):
        self.assertTrue(importar_marcas_instrumentos(self.tabla))

    def test_modelos_instrumentos(self):
        self.assertTrue(importar_modelos_instrumentos(self.tabla))
    
    def test_accesorios(self):
        self.assertTrue(importar_accesorios(self.tabla))
    
    def test_instrumentos(self):
        self.assertTrue(importar_instrumentos(self.tabla))
    
    def test_agrupaciones(self):
        self.assertTrue(importar_agrupaciones(self.tabla))
    
    def test_turnos(self):
        self.assertTrue(importar_turnos(self.tabla))

    def test_niveles_ts(self):
        self.assertTrue(importar_niveles_ts(self.tabla))
    
    def test_niveles_estudiantiles(self):
        self.assertTrue(importar_niveles_estudiantiles(self.tabla))
        
    def test_becas(self):
        self.assertTrue(importar_tipos_becas(self.tabla))

    def test_tipos_catedras(self):
        self.assertTrue(importar_tipos_catedras(self.tabla))
    
    def test_catedras(self):
        self.assertTrue(importar_catedras(self.tabla))
    
    def test_programas(self):
        self.assertTrue(importar_programas(self.tabla))
    
    def test_quienretira(self):
        self.assertTrue(importar_quienretira(self.tabla))
        
    def test_representantes(self):
        self.assertTrue(importar_representantes(self.tabla))
    
    def test_alumnos(self):
        self.assertTrue(importar_alumnos(self.tabla))
    
    def test_becados(self):
        self.assertTrue(importar_becados(self.tabla))
    
    def test_inscripciones(self):
        self.assertTrue(importar_inscripciones(self.tabla))
