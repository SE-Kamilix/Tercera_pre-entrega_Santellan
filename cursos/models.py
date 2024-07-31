from django.db import models

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    duracion = models.IntegerField(help_text="Duración en horas")

    def __str__(self):
        return self.nombre

class Instructor(models.Model):
    nombre = models.CharField(max_length=100)
    biografia = models.TextField()
    curso = models.ManyToManyField(Curso, related_name='instructores')

    def __str__(self):
        return self.nombre
