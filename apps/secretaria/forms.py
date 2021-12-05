from django import forms
from .models import *

class FacultadForm(forms.ModelForm):
    class Meta:
        model = Facultad
        fields = '__all__'
class CarreraForm(forms.ModelForm):
    class Meta:
        model = Carrera
        fields = '__all__'
class ProfesorForm(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = '__all__'
class TribunalForm(forms.ModelForm):
    class Meta:
        model = Tribunal
        fields = '__all__'

class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = '__all__'
class TesisForm(forms.ModelForm):
    class Meta:
        model = Tesis
        fields = '__all__'
class TribunalTesisFormTutor(forms.ModelForm):
    class Meta:
        model = TRibunalTesisTutor
        fields = '__all__'
class TribunalTesisFormOponenete(forms.ModelForm):
    class Meta:
        model = TRibunalTesisOponente
        fields = '__all__'

class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = '__all__'


class UbicacionForm(forms.ModelForm):
    class Meta:
        model = Ubicacion
        fields = '__all__'

class ExpedienteForm(forms.ModelForm):
    class Meta:
        model = Expediente
        fields = '__all__'