from django import forms
from .models import MensajeContacto, Consulta


class ContactoForm(forms.ModelForm):
    class Meta:
        model = MensajeContacto
        fields = ['nombre', 'telefono', 'email', 'fecha', 'direccion_finca', 'm2_finca', 'kg_estimados', 'otros_datos']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
            'otros_datos': forms.Textarea(attrs={'rows': 3}),
        }


class ConsultaForm(forms.ModelForm):
    class Meta:
        model = Consulta
        fields = ['nombre', 'telefono', 'mensaje']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'mensaje': forms.Textarea(attrs={'rows': 4, 'class': 'form-control'}),
        }
