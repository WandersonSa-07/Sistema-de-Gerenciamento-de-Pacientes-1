from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from core.forms.registroForm import AtendenteForm, UsuarioAtendente, EspecialidadeForm, FilaEsperaForm, PacienteForm, UsuarioPaciente
from core.models import FilaEspera, Medico, Paciente, Consulta

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

# def mostrar_fila_espera(request):
#    if str(request.method) == 'POST':
#       fila_espera_form = FilaEsperaForm(request.POST)
      
#       if fila_espera_form.is_valid():
#          fila_espera = fila_espera_form.save(commit=False)
#          fila_espera.save()

#          messages.success(request, 'Inserido na fila.')
#          return redirect('atendente_fila_espera')
#       else:
#          messages.error(request, 'Erro ao inserir na fila de espera.')
  
#    else:
#       fila_espera_form = FilaEsperaForm()
#    medicos = Medico.objects.all()
#    contexto = []
#    for medico in medicos:
#       fila = FilaEspera.objects.filter(medico=medico, estado="Waiting").order_by("created_at")
#       contexto.append({"medico": medico, "fila": fila})
#    return render(request, 'atendente/filaEspera.html', {'contexto': contexto, 'fila_espera_form':fila_espera_form}) 

def mostrar_fila_espera(request):
    if request.method == 'POST':
        fila_espera_form = FilaEsperaForm(request.POST)

        if fila_espera_form.is_valid():
            fila_espera = fila_espera_form.save(commit=False)
            fila_espera.medico = fila_espera.consulta.medico
            fila_espera.paciente = fila_espera.consulta.paciente
            fila_espera.save()
            messages.success(request, 'Inserido na fila.')
            return redirect('atendente_fila_espera')
        else:
            messages.error(request, 'Erro ao inserir na fila de espera.')

    else:
        fila_espera_form = FilaEsperaForm()

    # Preparar contexto com médicos e filas existentes
    medicos = Medico.objects.all()
    contexto = []
    for medico in medicos:
        fila = FilaEspera.objects.filter(medico=medico, estado="Waiting").order_by("created_at")
        contexto.append({"medico": medico, "fila": fila})


    return render(request, 'atendente/filaEspera.html', {
        'contexto': contexto,
        'fila_espera_form': fila_espera_form,
    })


def inserir_paciente(request):
   medico = get_object_or_404(Medico, id=1)
   paciente = get_object_or_404(Paciente, id=1)
    
   FilaEspera.objects.create(medico=medico, paciente=paciente)

def cadastro_pacienteView(request):
    if str(request.method) == 'POST':
        paciente_form = PacienteForm(request.POST)
        usuario_form = UsuarioPaciente(request.POST)

        if paciente_form.is_valid() and usuario_form.is_valid():
            usuario = usuario_form.save(commit=False)
            usuario.save()

            paciente = paciente_form.save(commit=False)
            paciente.usuario = usuario
            paciente.save()

            messages.success(request, 'Cadastro realizado com sucesso.')
            return redirect('cadastro_paciente')
        else:
            messages.error(request, 'Erro ao realizar o cadastro.')
    else:
        paciente_form = PacienteForm() 
        usuario_form = UsuarioPaciente()

    context = {
        'paciente_form': paciente_form,
        'usuario_form': usuario_form
    }

    return render(request, 'registro.html', context=context)

def ver_relatorio(request):
    medicos = Medico.objects.all()
    medicos_dados = []

    for medico in medicos:
        consultas = Consulta.objects.filter(medico=medico)  # Consultas do médico
        pacientes_na_fila = FilaEspera.objects.filter(medico=medico)  # Pacientes na fila de espera

        # Agora, mapear as consultas e a fila de espera
        consultas_e_fila = []
        for consulta in consultas:
            paciente_na_fila = pacientes_na_fila.filter(paciente=consulta.paciente).first()  # Verifica se o paciente está na fila de espera
            consultas_e_fila.append({
                'consulta': consulta,
                'updated_at_fila': paciente_na_fila.horario_chamado if paciente_na_fila else None  # Se o paciente estiver na fila, pega o updated_at
            })

        # Adiciona o médico com as consultas e a fila de espera
        medicos_dados.append({
            'medico': medico,
            'consultas_e_fila': consultas_e_fila
        })

    return render(request, 'atendente/medicos_com_consultas_e_fila.html', {
        'medicos_com_dados': medicos_dados,
    })
    
# def marcar_consulta(request):
#     if request.method == "GET":
#         horarios_disponiveis = HorarioDisponivel.objects.all().select_related('medico', 'medico__especialidade')
#         return render(request, "paciente/marcar_consulta.html", {"horarios_disponiveis": horarios_disponiveis})

#     elif request.method == "POST":
#         horario_id = request.POST.get("horario")

#         horario = HorarioDisponivel.objects.get(id=horario_id)
#         medico = horario.medico

#         # Criar a consulta
#         Consulta.objects.create(paciente=request.user.paciente, medico=medico, horario=horario)
#         horario.delete()  # Remove o horário disponível já marcado
#         return redirect("marcar_consulta")