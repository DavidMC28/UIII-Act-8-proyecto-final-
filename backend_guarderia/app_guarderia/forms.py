from django import forms
from .models import *

class NinoForm(forms.ModelForm):
    class Meta:
        model = Nino
        fields = '__all__'
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}),
            'alergias': forms.Textarea(attrs={'rows': 3}),
            'necesidades_especiales': forms.Textarea(attrs={'rows': 3}),
        }

class PadreMadreForm(forms.ModelForm):
    nino = forms.ModelChoiceField(queryset=Nino.objects.all(), empty_label="Seleccione un niño", required=False)

    class Meta:
        model = PadreMadre
        fields = '__all__'

class PersonalGuarderiaForm(forms.ModelForm):
    class Meta:
        model = PersonalGuarderia
        fields = '__all__'
        widgets = {
            'fecha_contratacion': forms.DateInput(attrs={'type': 'date'}),
            'certificaciones': forms.Textarea(attrs={'rows': 3}),
        }

class GrupoNinosForm(forms.ModelForm):
    class Meta:
        model = GrupoNinos
        fields = '__all__'
        widgets = {
            'descripcion_actividades': forms.Textarea(attrs={'rows': 3}),
        }

class ActividadGuarderiaForm(forms.ModelForm):
    class Meta:
        model = ActividadGuarderia
        fields = '__all__'
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 3}),
            'material_requerido': forms.Textarea(attrs={'rows': 3}),
        }

class AsistenciaForm(forms.ModelForm):
    class Meta:
        model = AsistenciaNino
        fields = '__all__'
        widgets = {
            'fecha_asistencia': forms.DateInput(attrs={'type': 'date'}),
            'hora_entrada': forms.TimeInput(attrs={'type': 'time'}),
            'hora_salida': forms.TimeInput(attrs={'type': 'time'}),
            'notas_dia': forms.Textarea(attrs={'rows': 3}),
        }

class PagoForm(forms.ModelForm):
    class Meta:
        model = PagoMensualidad
        fields = '__all__'
        widgets = {
            'mes_correspondiente': forms.DateInput(attrs={'type': 'date'}),
            'fecha_vencimiento': forms.DateInput(attrs={'type': 'date'}),
        }