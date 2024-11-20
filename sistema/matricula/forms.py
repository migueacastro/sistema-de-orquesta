from django import forms
from .models import *


class CustomClassForm(forms.ModelForm):
    def __init__(self, *args, **kwargs): 
        super(forms.ModelForm, self).__init__(*args, **kwargs) 
        for field in self.fields: 
            
            try:
                if self.fields[field].widget.input_type != 'select':
                    # Text, Number
                    self.fields[field].widget.attrs.update({'class': 'bg-gray-100 rounded-md indent-2 p-2 shadow-md focus:border-gray-700 focus:outline-none focus:ring'})
                else:
                    # Select
                    self.fields[field].widget.attrs.update({'class': 'bg-gray-100 rounded-md p-2 shadow-md focus:border-gray-700 focus:outline-none focus:ring'})
            except Exception:
                # Textarea
                self.fields[field].widget.attrs.update({'class': 'bg-gray-100 rounded-md p-2 shadow-md focus:border-gray-700 focus:outline-none focus:ring'})
class AlumnoForm(CustomClassForm):
    instrumentos = forms.ModelMultipleChoiceField(queryset=Instrumento.objects.filter(activo=True))
    class Meta:
        model = Alumno
        exclude = ('activo',)
        fields = ['nombre', 'apellido', 'cedula', 'edad', 'telefono', 'fecha_nacimiento', 'direccion', 'turno', 'sexo', 'nivel_estudiantil', 'nivel_ts', 'condicion_especial', 'programa', 'agrupacion', 'representantes', 'alergias', 'catedras', 'instrumentos']
    

class TurnoForm(CustomClassForm):
    class Meta:
        model = Turno
        exclude = ('activo',)
        fields = '__all__'
    
class NivelEstudiantilForm(CustomClassForm):
    class Meta:
        model = NivelEstudiantil
        exclude = ('activo',)
        fields = '__all__'

class NivelTSForm(CustomClassForm):
    class Meta:
        model = NivelTS
        exclude = ('activo',)
        fields = '__all__'

class AlergiaForm(CustomClassForm):
    class Meta:
        model = Alergia
        exclude = ('activo',)
        fields = '__all__'

class RepresentanteForm(CustomClassForm):
    class Meta:
        model = Representante
        exclude = ('activo',)
        fields = '__all__'
    
class CondicionEspecialForm(CustomClassForm):
    class Meta:
        model = CondicionEspecial
        exclude = ('activo',)
        fields = '__all__'

class TratamientoForm(CustomClassForm):
    class Meta:
        model = Tratamiento
        exclude = ('activo',)
        fields = '__all__'

class ProgramaForm(CustomClassForm):
    class Meta:
        model = Programa
        exclude = ('activo',)
        fields = '__all__'

class AgrupacionForm(CustomClassForm):
    class Meta:
        model = Agrupacion
        exclude = ('activo',)
        fields = '__all__'

class CatedraForm(CustomClassForm):
    class Meta:
        model = Catedra
        exclude = ('activo',)
        fields = '__all__'

class QuienRetiraForm(CustomClassForm):
    class Meta:
        model = QuienRetira
        exclude = ('activo',)
        fields = '__all__'

class InstrumentoForm(CustomClassForm,):
    alumno = forms.ModelChoiceField(queryset=Alumno.objects.all())
    class Meta:
        
        model = Instrumento
        exclude = ('activo',)
        fields = '__all__'

class MedicamentoForm(CustomClassForm):
    class Meta:
        model = Medicamento
        exclude = ('activo',)
        fields = '__all__'

class ColorForm(CustomClassForm):
    class Meta:
        model = Color
        exclude = ('activo',)
        fields = '__all__'
    
class CategoriaInstrumentoForm(CustomClassForm):
    class Meta:
        model = CategoriaInstrumento
        exclude = ('activo',)
        fields = '__all__'

class MarcaInstrumentoForm(CustomClassForm):
    class Meta:
        model = MarcaInstrumento
        exclude = ('activo',)
        fields = '__all__'
    
class ModeloInstrumentoForm(CustomClassForm):
    class Meta:
        model = ModeloInstrumento
        exclude = ('activo',)
        fields = '__all__'
    
class AccesorioForm(CustomClassForm):
    class Meta:
        model = Accesorio
        exclude = ('activo',)
        fields = '__all__'

class TipoBecaForm(CustomClassForm):
    class Meta:
        model = TipoBeca
        exclude = ('activo',)
        fields = '__all__'

class TipoCatedraForm(CustomClassForm):
    class Meta:
        model = TipoCatedra
        exclude = ('activo',)
        fields = '__all__'
    
class BecadoForm(CustomClassForm):
    class Meta:
        model = Becado
        exclude = ('activo',)
        fields = '__all__'

class InscripcionForm(CustomClassForm):
    class Meta:
        model = Inscripcion
        exclude = ('activo',)
        fields = '__all__'
        