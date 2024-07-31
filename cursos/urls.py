from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('agregar_categoria/', views.agregar_categoria, name='agregar_categoria'),
    path('agregar_curso/', views.agregar_curso, name='agregar_curso'),
    path('agregar_instructor/', views.agregar_instructor, name='agregar_instructor'),
    path('buscar_curso/', views.buscar_curso, name='buscar_curso'),
]
