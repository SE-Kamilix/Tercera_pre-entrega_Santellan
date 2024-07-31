# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import Categoria, Curso, Instructor
from .forms import CategoriaForm, CursoForm, InstructorForm, BuscarCursoForm

def index(request):
    return render(request, 'cursos/index.html')

def agregar_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CategoriaForm()
    return render(request, 'cursos/form.html', {'form': form, 'titulo': 'Agregar Categoría'})

def agregar_curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CursoForm()
    return render(request, 'cursos/form.html', {'form': form, 'titulo': 'Agregar Curso'})

def agregar_instructor(request):
    if request.method == 'POST':
        form = InstructorForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = InstructorForm()
    return render(request, 'cursos/form.html', {'form': form, 'titulo': 'Agregar Instructor'})

def buscar_curso(request):
    cursos = []
    if 'nombre' in request.GET:
        nombre = request.GET['nombre']
        cursos = Curso.objects.filter(nombre__icontains=nombre)
    form = BuscarCursoForm()
    return render(request, 'cursos/buscar.html', {'form': form, 'cursos': cursos})
