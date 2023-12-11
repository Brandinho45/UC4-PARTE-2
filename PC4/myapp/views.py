from django.shortcuts import render,HttpResponse,redirect
from .models import Course
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
def eliminar_curso(request,idcourse):
    curso=Course.objects.get(idcourse=idcourse)
    curso.delete()
    return redirect('/cursos/')

def registrar_curso(request):
    code=request.POST['code']
    name=request.POST['name']
    hour=request.POST['hour']
    credits=request.POST['credits']
    state=request.POST['state']
    curso=Course.objects.create(code=code,name=name,hour=hour,credits=credits,state=state)
    return redirect('/agregarcurso/')
