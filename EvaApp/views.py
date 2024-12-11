from django.shortcuts import (render, redirect, get_object_or_404)
from EvaApp.forms import (formVideojuego, formUsuario, formComputadora)
from EvaApp.models import (Videojuego, Usuario, Computadora)

# Create your views here.

def index(request):
    return render(request,"index.html")

def listadoUsuarios(request):
    usuarios = Usuario.objects.all()
    data = {'usuarios':usuarios}
    return render(request,"listadoUsuarios.html",data)

def agregarUsuario(request):
    form = formUsuario()
    if request.method == 'POST':
        form = formUsuario(request.POST)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form':form}
    return render(request,"agregarUsuario.html",data)

def actualizarUsuario(request, id):
    usuario = Usuario.objects.get(id = id)
    form = formUsuario(instance=usuario)
    if request.method == 'POST':
        form = formUsuario(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form':form}
    return render(request,"agregarUsuario.html",data)

def eliminarUsuario(request, id):
    usuario = Usuario.objects.get(id = id)
    usuario.delete()
    return redirect("/usuarios")





def listadoVideojuegos(request):
    videojuegos = Videojuego.objects.all()
    data = {'videojuegos':videojuegos}
    return render(request,"listadoVideojuegos.html",data)

def agregarJuego(request):
    form = formVideojuego()
    if request.method == 'POST':
        form = formVideojuego(request.POST)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form':form}
    return render(request,"agregarVideojuego.html",data)

def actualizarJuego(request, id):
    videojuego = Videojuego.objects.get(id = id)
    form = formVideojuego(instance=videojuego)
    if request.method == 'POST':
        form = formVideojuego(request.POST, instance=videojuego)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form':form}
    return render(request,"agregarVideojuego.html",data)

def eliminarJuego(request, id):
    videojuego = Videojuego.objects.get(id = id)
    videojuego.delete()
    return redirect("/videojuegos")



def listadoComputadoras(request):
  computadoras = Computadora.objects.all()
  data = {'computadoras': computadoras}
  return render(request, "listadoComputadoras.html", data)

def agregarComputadora(request):
  form = formComputadora()
  if request.method == 'POST':
    form = formComputadora(request.POST)
    if form.is_valid():
      form.save()
      return listadoComputadoras(request)
  data = {'form': form}
  return render(request, "agregarComputadora.html", data)

def actualizarComputadora(request, id):
  computadora = Computadora.objects.get(pk=id)
  form = formComputadora(instance=computadora)
  if request.method == 'POST':
    form = formComputadora(request.POST, instance=computadora)
    if form.is_valid():
      form.save()
      return listadoComputadoras(request)
  data = {'form': form}
  return render(request, "agregarComputadora.html", data)

def eliminarComputadora(request, id):
  computadora = Computadora.objects.get(pk=id)
  computadora.delete()
  return redirect("/computadoras")

def detalleUsuario(request, id):
    usuario = get_object_or_404(Usuario, pk=id)
    #videojuegos = usuario.videojuego_set.all()
    #computadoras = usuario.computadora_set.all()
    videojuegos = usuario.videojuego_set.filter(usuario=usuario)
    computadoras = usuario.computadora_set.filter(usuario=usuario)
    return render(request, 'detalleUsuario.html', {'usuario': usuario, 'videojuegos': videojuegos, 'computadoras': computadoras})  # Pass user data to template