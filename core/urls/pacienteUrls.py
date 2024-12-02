from django.urls import path
from core.views.pacienteView import pacienteRegistro, cadastrar_ficha_medica, marcar_consulta

urlpatterns = [
    path("", pacienteRegistro, name='pacienteRegistro'),
    path("ficha_medica/", cadastrar_ficha_medica, name='cadastrar_ficha_medica'),
    path('marcar_consulta/', marcar_consulta, name='marcar_consulta')
]