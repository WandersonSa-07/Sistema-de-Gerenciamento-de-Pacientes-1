from django.urls import path
from core.views.pacienteView import pacienteRegistro

urlpatterns = [
    path("", pacienteRegistro, name='pacienteRegistro')
]