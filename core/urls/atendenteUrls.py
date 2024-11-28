from django.urls import path
from core.views.atendenteView import *
from core.views.pacienteView import pacienteRegistro
from core.views.medicoView import cadastro_MedicoView

urlpatterns = [
    path("", atendenteView, name='atendente'),
    path("medico/", atendente_medicoView, name='atendente_medico'),
    path("paciente/", atendente_pacienteView, name='atendente_paciente'),
    path("cadastro/",cadastro_atendenteView, name='cadastro_atendente'),
    path("medico/cadastroMedico/", cadastro_MedicoView, name='cadastro_medico'),
    path("paciente/cadastroPaciente", pacienteRegistro, name='cadastro_paciente'),
    path("medico/cadastroEspecialidade/", cadastro_especialidadeView, name='cadastro_especialidade')
]