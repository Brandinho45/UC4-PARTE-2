from django.shortcuts import render,HttpResponse,redirect

# Create your views here.
def inicio(request):
    return render(request, 'inicio.html')

def listarcursos(request):
    return render(request, 'listarCurso.html')

def listadocarreras(request):
    return render(request, 'listadoCarreras.html')

def agregarcurso(request):
    return render(request, 'agregarCurso.html')

def agregarcarreras(request):
    return render(request, 'agregarCarreras.html')
