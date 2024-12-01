from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from core.forms.registroForm import MedicoForm, UsuarioMedico, Funcionalidades_de_ConsultaForm
from core.models import FilaEspera, Medico, Paciente, Consulta, ReceitaMedica, FichaMedica
from django.http import HttpResponse

def cadastro_MedicoView(request):
   if str(request.method) == 'POST':
      medico_form = MedicoForm(request.POST)
      usuario_form = UsuarioMedico(request.POST)

      if medico_form.is_valid() and usuario_form.is_valid():
         usuario = usuario_form.save(commit=False)
         usuario.save()

         medico = medico_form.save(commit=False)
         medico.usuario = usuario
         medico.save()
         messages.success(request, 'Cadastro realizado com sucesso.')
         return redirect('cadastro_medico')
      else:
         messages.error(request, 'Erro ao realizar o cadastro.')
  
   else:
      medico_form = MedicoForm()
      usuario_form = UsuarioMedico()

   context = {
      'medico_form': medico_form,
      'usuario_form': usuario_form
   }

   return render(request,'atendente/cadastro_medico.html', context=context)


def remover_paciente(request, fila_id):
   medico=request.user.medico
   if not FilaEspera.objects.filter(medico=medico, estado="Being_Attended_to").exists():
      fila = get_object_or_404(FilaEspera, id=fila_id, estado="Waiting")
      fila.estado = "Being_Attended_to"
      fila.save()
   return redirect('fila_espera_medico')

def gerenciar_paciente(request):
   medico=request.user.medico
   fila = FilaEspera.objects.filter(medico=medico, estado="Waiting").order_by("created_at")
   return render(request, 'medico/fila_espera.html', {'fila': fila})

def realizar_consulta(request):
   medico=request.user.medico
   fila =  FilaEspera.objects.filter(estado="Being_Attended_to").first()

   if (fila==None):
      messages.warning(request, "Nenhum paciente encontrado.")
      return redirect("home")
   
   paciente = fila.paciente
   if str(request.method) == 'POST':
      funcionalidades_consulta = Funcionalidades_de_ConsultaForm(request.POST)
      


      if funcionalidades_consulta.is_valid():
         horario = funcionalidades_consulta.cleaned_data["horario"]
         data = funcionalidades_consulta.cleaned_data["data"]
         sintomas_apresentados = funcionalidades_consulta.cleaned_data["sintomas_apresentados"]
         remedio = funcionalidades_consulta.cleaned_data["remedio"]
         dosagem = funcionalidades_consulta.cleaned_data["dosagem"]
         qtd_de_dias  = funcionalidades_consulta.cleaned_data["qtd_de_dias"]
         qtd_por_dia  = funcionalidades_consulta.cleaned_data["qtd_por_dia"]

         Consulta.objects.create(
            medico=medico,
            data=data,
            horario=horario,
            paciente=paciente,
            sintomas_apresentados=sintomas_apresentados
            )

            # Criar Ficha Médica
         ReceitaMedica.objects.create(
            medico=medico,
            paciente=paciente,
            remedio=remedio,
            dosagem=dosagem,
            qtd_de_dias=qtd_de_dias,
            qtd_por_dia= qtd_por_dia                
            )


            # Alterar estado do Paciente
         fila.estado = "Attended"
         #fila.horario_chamado = data
         fila.save()
         
         
         return redirect('home')
      else:
         messages.error(request, 'Erro ao realizar o cadastro.')
  
   else:
      funcionalidades_consulta = Funcionalidades_de_ConsultaForm()

   ficha_medica =  FichaMedica.objects.filter(paciente=paciente).first()

   context = {
      'funcionalidades_consulta': funcionalidades_consulta,
      'ficha_medica': ficha_medica
   }

   return render(request,'medico/funcionalidades_consulta.html', context=context)