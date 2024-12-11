from rest_framework import serializers
from EvaApp.models import (Usuario, Computadora, Videojuego)

class SerialUsuario(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class SerialComputadora(serializers.ModelSerializer):
    class Meta:
        model = Computadora
        fields = '__all__'

class SerialVideojuego(serializers.ModelSerializer):
    class Meta:
        model = Videojuego
        fields = '__all__'