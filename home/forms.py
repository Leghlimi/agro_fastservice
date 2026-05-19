from django import forms
from .models import MensajeContacto

class ContactoForm(forms.ModelForm):
    class Meta:
        model = MensajeContacto
        fields = ['nombre', 'telefono', 'email', 'fecha', 'direccion_finca', 'm2_finca', 'kg_estimados', 'otros_datos']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
            'otros_datos': forms.Textarea(attrs={'rows': 3}),
        }