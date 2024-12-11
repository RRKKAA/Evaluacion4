from django.contrib import admin
from EvaApp.models import Usuario, Videojuego, Computadora

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'apellido', 'telefono', 'ciudad', 'correo']

class VideojuegoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'publicador', 'genero', 'tamanio', 'costo']

class ComputadoraAdmin(admin.ModelAdmin):
    list_display = ['marca', 'disco', 'gpu', 'cpu', 'ram']

# Register your models here.
admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Videojuego, VideojuegoAdmin)
admin.site.register(Computadora, ComputadoraAdmin)