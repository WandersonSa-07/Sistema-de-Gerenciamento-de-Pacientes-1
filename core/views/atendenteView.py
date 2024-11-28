from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from core.forms.registroForm import AtendenteForm, UsuarioAtendente, EspecialidadeForm, FilaEsperaForm
from core.models import FilaEspera, Medico, Paciente

def atendenteView(request):
        return render(request, template_name='atendente/atendente.html')

def atendente_medicoView(request):
        return render(request, template_name='atendente/atendente_medico.html')

def atendente_pacienteView(request):
        return render (request, template_name='atendente/atendente_paciente.html')


def cadastro_atendenteView(request):
   if str(request.method) == 'POST':
      atendente_form = AtendenteForm(request.POST)
      usuario_form = UsuarioAtendente(request.POST)

      if atendente_form.is_valid() and usuario_form.is_valid():
         usuario = usuario_form.save(commit=False)
         usuario.save()

         atendente = atendente_form.save(commit=False)
         atendente.usuario = usuario
         atendente.save()
         messages.success(request, 'Cadastro realizado com sucesso.')
         return redirect('cadastro_atendente')
      else:
         messages.error(request, 'Erro ao realizar o cadastro.')
  
   else:
      atendente_form = AtendenteForm()
      usuario_form = UsuarioAtendente()

   context = {
      'atendente_form': atendente_form,
      'usuario_form': usuario_form
   }

   return render(request,'atendente/cadastro_atendente.html', context=context)

def cadastro_especialidadeView(request):
   if str(request.method) == 'POST':
      especialidade_form = EspecialidadeForm(request.POST)

      if especialidade_form.is_valid():
         especialidade_form.save()
         messages.success(request, 'Cadastro realizado com sucesso.')
         return redirect('cadastro_especialidade')
      else:
         messages.error(request, 'Erro ao realizar o cadastro.')
  
   else:
      especialidade_form = EspecialidadeForm()

   context = {
      'especialidade_form': especialidade_form
   }

   return render(request,'atendente/cadastro_especialidade.html', context=context)

def mostrar_fila_espera(request):
   if str(request.method) == 'POST':
      fila_espera_form = FilaEsperaForm(request.POST)
      
      if fila_espera_form.is_valid():
         fila_espera = fila_espera_form.save(commit=False)
         fila_espera.save()

         messages.success(request, 'Inserido na fila.')
         return redirect('atendente_fila_espera')
      else:
         messages.error(request, 'Erro ao inserir na fila de espera.')
  
   else:
      fila_espera_form = FilaEsperaForm()
   medicos = Medico.objects.all()
   contexto = []
   for medico in medicos:
      fila = FilaEspera.objects.filter(medico=medico, estado="Waiting").order_by("created_at")
      contexto.append({"medico": medico, "fila": fila})
   return render(request, 'atendente/filaEspera.html', {'contexto': contexto, 'fila_espera_form':fila_espera_form}) 


def inserir_paciente(request):
   medico = get_object_or_404(Medico, id=1)
   paciente = get_object_or_404(Paciente, id=1)
    
   FilaEspera.objects.create(medico=medico, paciente=paciente)