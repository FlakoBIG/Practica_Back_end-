from django import forms
from App.models import Personaje

class FormPersonaje(forms.ModelForm):
    class Meta:
        model = Personaje
        fields = '__all__'
