from django.shortcuts import render, get_object_or_404, redirect
from core.models import Medico, FilaEspera, Paciente

# Create your views here.
def mostrar_fila_espera(request):
    medico = get_object_or_404(Medico, id=1)
    fila = FilaEspera.objects.filter(medico=medico, estado="Waiting").order_by("created_at")

    return render(request, 'fila_espera.html', {'medico': medico, 'fila': fila}) 

def inserir_paciente(request):
    medico = get_object_or_404(Medico, id=1)
    paciente = get_object_or_404(Paciente, id=1)
    
    FilaEspera.objects.create(medico=medico, paciente=paciente)

def remover_paciente(request):
    fila = get_object_or_404(FilaEspera, id=1, estado="Waiting")
    fila.estado = "Attended"
    fila.save()

def posicao(request):
    paciente = get_object_or_404(Paciente, id=1)
    medico = get_object_or_404(Medico, id=1)
    FilaEspera.objects.filter(medico=medico, estado="Waiting", paciente=paciente).order_by("created_at")