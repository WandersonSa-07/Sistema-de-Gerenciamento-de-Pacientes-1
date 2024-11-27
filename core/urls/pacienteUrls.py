from django.urls import path
from core.views.pacienteView import pacienteRegistro, visualizar_receita

urlpatterns = [
    path("", pacienteRegistro, name='pacienteRegistro'),
    path('receita/<int:receita_id>/pdf/', visualizar_receita, name='gerar_pdf'),

]