from django import forms
from django.contrib.auth.forms import UserCreationForm
from core.models import Paciente, Usuario, Atendente, Medico, Especialidade, FilaEspera

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

class UsuarioPaciente(UsuarioForm):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['codigo'].label = 'CPF'


class AtendenteForm(forms.ModelForm):
    class Meta:
        model = Atendente
        fields = ['usuario']
        exclude = ('usuario',)

class UsuarioAtendente(UsuarioForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['codigo'].label = 'ID'

    def save(self, commit=True):
        usuario = super().save(commit=False)
        usuario.tipo = 'atendente'
        if commit:
            usuario.save()
        return usuario
        
class MedicoForm(forms.ModelForm):
    class Meta:
        model = Medico
        fields = "__all__"
        exclude = ('usuario',)

class UsuarioMedico(UsuarioForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['codigo'].label = 'CRM'

    def save(self, commit=True):
        usuario = super().save(commit=False)
        usuario.tipo = 'medico'
        if commit:
            usuario.save()
        return usuario
    
class EspecialidadeForm(forms.ModelForm):
    class Meta:
        model = Especialidade
        fields = ['nome']
        
class FilaEsperaForm(forms.ModelForm):
    class Meta:
        model = FilaEspera
        fields = ['medico', 'paciente', 'estado']
        widgets = {
            'medico': forms.Select(attrs={'class': 'form-control'}),
            'paciente': forms.Select(attrs={'class': 'form-control'}),
            'estado': forms.Select(choices=[('Waiting', 'Em espera'), ('Attended', 'Atendido'), ('Cancelled', 'Cancelado')], attrs={'class': 'form-control'}),
        }
