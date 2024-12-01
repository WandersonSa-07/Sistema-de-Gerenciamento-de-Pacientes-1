from django.urls import path
from core.views.pacienteView import pacienteRegistro, cadastrar_ficha_medica

urlpatterns = [
    path("", pacienteRegistro, name='pacienteRegistro'),
    path("ficha_medica/", cadastrar_ficha_medica, name='cadastrar_ficha_medica')
]