from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *

def inicio(request):
    return render(request, "inicio.html")



def ver_futbol(request):
    return render (request, "ver_futbol.html")

def ver_basquet(request):
    return render (request, "ver_basquet.html")

def ver_rugby(request):
    return render (request, "ver_rugby.html")

def crear_jugador(request):
    
        if request.method == "POST":
            
            formulario1 = RegistroJugadores (request.POST)
            
            if formulario1.is_valid():
                    info = formulario1.cleaned_data
                    jugador_nuevo = jugadores(nombre = info ['nombre'], apellido = info ['apellido'], 
                                            edad = info ['edad'], estatura = info ['estatura'], 
                                            deporte = info['deporte'] )
                    jugador_nuevo.save()
                    return render (request, "inicio.html")
        else:
            formulario1 = RegistroJugadores()
                
        return render(request, 'crear_jugador.html', {"form1":formulario1})
    
def crear_futbol(request):
    
    if request.method == "POST":
        
        formulario1 = RegistroBasquet (request.POST)
        
        if formulario1.is_valid():
                info = formulario1.cleaned_data
                jugador_nuevo = Futbol(nombre = info ['nombre'], apellido = info ['apellido'], 
                                        posicion = info ['posicion'])
                jugador_nuevo.save()
                return render (request, "inicio.html")
    else:
        formulario1 = RegistroBasquet()
            
    return render(request, 'crear_futbol.html', {"form1":formulario1})

def buscar_jugador(request):
    return render (request, "buscar_jugador.html")

def buscar_futbol(request):
    return render (request, "buscar_futbol.html")

def buscar_basquet(request):
    return render (request, "buscar_basquet.html")

def buscar_rugby(request):
    return render (request, "buscar_rugby.html")

def ver_jugadores(request):
    todos = jugadores.objects.all()
    return render (request, "ver_jugadores.html", {"jugador":todos})
    

def resultadojugador (request):
    
    if 'jugador' in request.GET:
        jugador_busqueda = request.GET['jugador']
        resultados = jugadores.objects.filter(nombre__icontains=jugador_busqueda)
        return render(request, "resultado_jugador.html", {"res": resultados, "busJugador": jugador_busqueda})
# Maneja el caso en el que el parámetro 'jugador' no está presente en la solicitud GET
# ...
    return render(request, '/resultado_jugador.html', {"res": None})



def resultado_futbol(request):
    if 'jugador' in request.GET:
        jugador_busqueda = request.GET['jugador']
        resultados = Futbol.objects.filter(nombre__icontains=jugador_busqueda)
        return render(request, 'resultado_futbol.html', {'res': resultados, 'busJugador': jugador_busqueda})
# Maneja el caso en el que el parámetro 'jugador' no está presente en la solicitud GET
# ...
    return render(request, '/resultado_futbol.html', {"res": None})

def resultado_basquet (request):
    
    if 'jugador' in request.GET:
        jugador_busqueda = request.GET['jugador']
        resultados = Basquet.objects.filter(nombre__icontains=jugador_busqueda)
        return render(request, "resultado_basquet.html", {"res": resultados, "busJugador": jugador_busqueda})
# Maneja el caso en el que el parámetro 'jugador' no está presente en la solicitud GET
# ...
    return render(request, '/resultado_basquet.html', {"res": None})

def crear_basquet(request):
    
    if request.method == "POST":
        
        formulario1 = RegistroBasquet (request.POST)
        
        if formulario1.is_valid():
                info = formulario1.cleaned_data
                jugador_nuevo = Basquet(nombre = info ['nombre'], apellido = info ['apellido'], 
                                        posicion = info ['posicion'])
                jugador_nuevo.save()
                return render (request, "inicio.html")
    else:
        formulario1 = RegistroBasquet()
            
    return render(request, 'crear_basquet.html', {"form1":formulario1})

def resultado_rugby (request):
    
    if 'jugador' in request.GET:
        jugador_busqueda = request.GET['jugador']
        resultados = Rugby.objects.filter(nombre__icontains=jugador_busqueda)
        return render(request, "resultado_rugby.html", {"res": resultados, "busJugador": jugador_busqueda})
# Maneja el caso en el que el parámetro 'jugador' no está presente en la solicitud GET
# ...
    return render(request, '/resultado_rugby.html', {"res": None})

def crear_rugby(request):
    
    if request.method == "POST":
        
        formulario1 = RegistroRugby (request.POST)
        
        if formulario1.is_valid():
                info = formulario1.cleaned_data
                jugador_nuevo = Rugby(nombre = info ['nombre'], apellido = info ['apellido'], 
                                        posicion = info ['posicion'])
                jugador_nuevo.save()
                return render (request, "inicio.html")
    else:
        formulario1 = RegistroRugby()
            
    return render(request, 'crear_rugby.html', {"form1":formulario1})

def eliminar_jugador(request, jugadores_nombre):
    jugador_escogido = jugadores.objects.get(nombre=jugadores_nombre)
    jugador_escogido.delete()
    todos = jugadores.objects.all()
    
    return render(request, "ver_jugadores.html", {"jugador": todos})

def actualizar_jugador (request, jugadores_nombre):
    jugador_escogido = jugadores.objects.get(nombre=jugadores_nombre)
     
    if request.method == "POST":
            
            formulario1 = RegistroJugadores (request.POST)
            
            if formulario1.is_valid():
                    info = formulario1.cleaned_data
                    jugador_escogido.nombre = info ["nombre"]
                    jugador_escogido.apellido = info ["apellido"]
                    jugador_escogido.edad = info ["edad"]
                    jugador_escogido.estatura = info ["estatura"]
                    jugador_escogido.deporte = info ["deporte"]
                    jugador_escogido.save()
                    
                    return render (request, "inicio.html")
    else:
        formulario1 = RegistroJugadores(initial = {"nombre": jugador_escogido.nombre,
                                                   "apellido": jugador_escogido.apellido,
                                                   "edad": jugador_escogido.edad,
                                                   "estatura":jugador_escogido.estatura,
                                                   "deporte":jugador_escogido.deporte})
                
    return render(request, 'crear_jugador.html', {"form1":formulario1})
    





# Create your views here.
