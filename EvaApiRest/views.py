from django.shortcuts import render
from .serializers import (SerialUsuario, SerialComputadora, SerialVideojuego)
from EvaApp.models import (Usuario, Computadora, Videojuego)
from rest_framework.response import Response
from rest_framework import generics, mixins, status, viewsets
from rest_framework.views import APIView
from django.http import Http404

# Create your views here.

class UsuarioLista(generics.ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = SerialUsuario
    
class UsuarioDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = SerialUsuario




class ComputadoraLista(generics.ListCreateAPIView):
    queryset = Computadora.objects.all()
    serializer_class = SerialComputadora
    
class ComputadoraDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Computadora.objects.all()
    serializer_class = SerialComputadora




class VideojuegoLista(generics.ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = SerialVideojuego
    
class VideojuegoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = SerialVideojuego




class UsuarioViewSets(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = SerialUsuario
        