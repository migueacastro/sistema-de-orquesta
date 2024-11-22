from django import forms
from .models import *

class CustomClassForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Define the fields that require filtering with activo=True
        active_fields = {
            'instrumentos': Instrumento.objects.filter(activo=True, alumno=None),
            'representantes': Representante.objects.filter(activo=True),
            'alergias': Alergia.objects.filter(activo=True),
            'condicion_especial': CondicionEspecial.objects.filter(activo=True),
            'nivel_estudiantil': NivelEstudiantil.objects.filter(activo=True),
            'nivel_ts': NivelTS.objects.filter(activo=True),
            'catedras': Catedra.objects.filter(activo=True),
            'modelo': ModeloInstrumento.objects.filter(activo=True),
            'agrupacion': Agrupacion.objects.filter(activo=True),
            'programa': Programa.objects.filter(activo=True),
            'tipo_beca': TipoBeca.objects.filter(activo=True),
            'turno': Turno.objects.filter(activo=True),
            'tipo_catedra': TipoCatedra.objects.filter(activo=True),
            'medicamento': Medicamento.objects.filter(activo=True),
            'tratamiento': Tratamiento.objects.filter(activo=True),
            'color': Color.objects.filter(activo=True),
            'categoria': CategoriaInstrumento.objects.filter(activo=True),
            'marca': MarcaInstrumento.objects.filter(activo=True),
        }

        # Set queryset for active fields
        for field_name, queryset in active_fields.items():
            if field_name in self.fields:
                self.fields[field_name].queryset = queryset
        
        # Customize widget attributes
        for field_name, field in self.fields.items():
            try:
                if field.widget.input_type != 'select':
                    # Text, Number
                    field.widget.attrs.update({
                        'class': 'bg-gray-100 disabled:bg-gray-300 rounded-md indent-2 p-2 shadow-md focus:border-gray-700 focus:outline-none focus:ring'
                    })
                else:
                    # Select
                    field.widget.attrs.update({
                        'class': 'bg-gray-100 disabled:bg-gray-300 rounded-md p-2 shadow-md focus:border-gray-700 focus:outline-none focus:ring'
                    })
            except AttributeError:
                # Textarea
                field.widget.attrs.update({
                    'class': 'bg-gray-100 disabled:bg-gray-300 rounded-md p-2 shadow-md focus:border-gray-700  focus:outline-none focus:ring'
                })


class AlumnoForm(CustomClassForm):
    instrumentos = forms.ModelMultipleChoiceField(queryset=Instrumento.objects.filter(activo=True, alumno = None), required=False)
    representantes = forms.ModelMultipleChoiceField(queryset=Representante.objects.filter(activo=True), required=False)
    alergias = forms.ModelMultipleChoiceField(queryset=Alergia.objects.filter(activo=True), required=False)
    condicion_especial = forms.ModelChoiceField(queryset=CondicionEspecial.objects.filter(activo=True), required=False)
    class Meta:
        model = Alumno
        exclude = ('activo',)
        fields = ['nombre', 'apellido', 'cedula', 'edad', 'telefono', 'fecha_nacimiento', 'direccion', 'turno', 'sexo', 'nivel_estudiantil', 'nivel_ts', 'condicion_especial', 'programa', 'agrupacion', 'representantes', 'alergias', 'catedras', 'instrumentos']
    
    def save(self, commit=True): 
        instance = super().save(commit=False) 
        instance.save() 
        self.save_m2m() 
        self.cleaned_data['instrumentos'].update(alumno=instance) 
        return instance
    
    def __init__(self, *args, **kwargs): 
        super().__init__(*args, **kwargs) 
        instance = kwargs.get('instance') 
        if instance: 
            self.fields['instrumentos'].queryset = Instrumento.objects.filter( activo=True ).filter( models.Q(alumno__isnull=True) | models.Q(alumno=instance) ) 
            self.fields['instrumentos'].initial = instance.instrumentos.all() 
        else: 
            self.fields['instrumentos'].queryset = Instrumento.objects.filter(activo=True, alumno=None)

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
    alumno = forms.ModelChoiceField(queryset=Alumno.objects.filter(activo=True), required=False)
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
        