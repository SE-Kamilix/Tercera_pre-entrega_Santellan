from django import forms
from .models import Categoria, Curso, Instructor

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = '__all__'

class InstructorForm(forms.ModelForm):
    class Meta:
        model = Instructor
        fields = '__all__'

class BuscarCursoForm(forms.Form):
    nombre = forms.CharField(max_length=100, required=False)
