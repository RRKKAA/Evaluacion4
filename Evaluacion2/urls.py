"""Evaluacion2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
#from EvaApp import views
from EvaApiRest import views

router = DefaultRouter()
router.register('usuariosViewSets', views.UsuarioViewSets)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('usuarios/',views.UsuarioLista.as_view()),
    path('usuarios/<int:pk>', views.UsuarioDetail.as_view()),
    path('computadoras/',views.ComputadoraLista.as_view()),
    path('computadoras/<int:pk>', views.ComputadoraDetail.as_view()),
    path('videojuegos/',views.VideojuegoLista.as_view()),
    path('videojuegos/<int:pk>', views.VideojuegoDetail.as_view()),
    #path('',views.index),

    #path('usuarios/',views.listadoUsuarios),
    #path('agregarUsuario/',views.agregarUsuario),
    #path('actualizarUsuario/<int:id>',views.actualizarUsuario),
    #path('eliminarUsuario/<int:id>',views.eliminarUsuario),
    #path('usuario/<int:id>',views.detalleUsuario),

    #path('computadoras/',views.listadoComputadoras),
    #path('agregarComputadora/',views.agregarComputadora),
    #path('actualizarComputadora/<int:id>',views.actualizarComputadora),
    #path('eliminarComputadora/<int:id>',views.eliminarComputadora),

    #path('videojuegos/',views.listadoVideojuegos),
    #path('agregarVideojuego/',views.agregarJuego),
    #path('actualizarJuego/<int:id>',views.actualizarJuego),
    #path('eliminarJuego/<int:id>',views.eliminarJuego),
]
