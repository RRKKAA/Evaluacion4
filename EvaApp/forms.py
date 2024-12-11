from django import forms
from EvaApp.models import (Videojuego, Computadora, Usuario)
class formVideojuego(forms.ModelForm):
    class Meta:
        model = Videojuego
        fields = '__all__'

class formComputadora(forms.ModelForm):
    class Meta:
        model = Computadora
        fields = '__all__'

class formUsuario(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'