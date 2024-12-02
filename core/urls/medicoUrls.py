from django.urls import path
from core.views.atendenteView import *
from core.views.medicoView import gerenciar_paciente, remover_paciente, realizar_consulta, definir_horarios
urlpatterns = [
    path('fila/', gerenciar_paciente, name='fila_espera_medico'),
    path('filaEspera/<int:fila_id>/chamar/', remover_paciente, name='chamar_paciente'),
    path('consulta/', realizar_consulta, name='medico_consulta'),
    path('definir_horarios/', definir_horarios, name='medico_definir_horario')
]