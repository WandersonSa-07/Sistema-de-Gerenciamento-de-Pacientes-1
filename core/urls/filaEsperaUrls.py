from django.urls import path
from core.views.filaEsperaView import mostrar_fila_espera

urlpatterns = [
    path("", mostrar_fila_espera, name='mostrar_fila_espera')
]