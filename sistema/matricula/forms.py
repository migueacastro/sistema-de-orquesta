from django import forms
from .models import *

class AlumnoForm(models.ModelForm):

    
    class Meta:
        model = Alumno
        fields = '__all__'
    