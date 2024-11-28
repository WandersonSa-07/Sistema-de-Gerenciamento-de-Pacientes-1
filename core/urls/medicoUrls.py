from django.urls import path
from core.views.atendenteView import *
from core.views.medicoView import gerenciar_paciente, remover_paciente

urlpatterns = [
    path('fila/', gerenciar_paciente, name='fila_espera_medico'),
    path('filaEspera/<int:fila_id>/chamar/', remover_paciente, name='chamar_paciente'),
    path('consulta/', gerenciar_paciente, name='medico_consulta')
]