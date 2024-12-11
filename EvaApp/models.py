from django.db import models

# Create your models here.

class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    telefono = models.IntegerField()
    ciudad = models.CharField(max_length=50)
    correo = models.CharField(max_length=50)

class Videojuego(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    publicador = models.CharField(max_length=50)
    genero = models.CharField(max_length=50)
    tamanio = models.IntegerField()
    costo = models.IntegerField()
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

class Computadora(models.Model):
    id = models.AutoField(primary_key=True)
    marca = models.CharField(max_length=50)
    disco = models.IntegerField()
    gpu = models.IntegerField()
    cpu = models.IntegerField()
    ram = models.IntegerField()
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)