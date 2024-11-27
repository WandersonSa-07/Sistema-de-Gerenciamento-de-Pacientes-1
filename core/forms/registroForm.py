from django import forms
from django.contrib.auth.forms import UserCreationForm
from core.models import Paciente, Usuario, Atendente

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = "__all__"
        exclude = ('usuario',)
        widgets = {
            'data_nascimento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'})
        }

class UsuarioForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['codigo','password1', 'password2','email','first_name','last_name', 'telefone']


class AtendenteForm(forms.ModelForm):
    class Meta:
        model = Atendente
        fields = ['usuario']
        exclude = ('usuario',)

class UsuarioAtendente(UsuarioForm):
    def save(self, commit=True):
        usuario = super().save(commit=False)
        usuario.tipo = 'atendente'
        if commit:
            usuario.save()
        return usuario
        

