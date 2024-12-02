from django.contrib import messages
from django.shortcuts import redirect, render
from core.forms.registroForm import PacienteForm, UsuarioPaciente, FichaMedicaForm
from core.models import FichaMedica, Especialidade, Consulta, HorarioDisponivel, Medico

def pacienteRegistro(request):
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
            return redirect('pacienteRegistro')
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


def cadastrar_ficha_medica(request):
   paciente=request.user.paciente
   
   if str(request.method) == 'POST':
        ficha_medica = FichaMedicaForm(request.POST)
      


        if ficha_medica.is_valid():
            especialidade = ficha_medica.cleaned_data["especialidade"]
            alergias = ficha_medica.cleaned_data["alergias"]
            medicamentos_em_uso = ficha_medica.cleaned_data["medicamentos_em_uso"]
            observacoes = ficha_medica.cleaned_data["observacoes"]
            

            FichaMedica.objects.create(
                especialidade=especialidade,
                alergias=alergias,
                medicamentos_em_uso=medicamentos_em_uso,
                observacoes=observacoes,
                paciente=paciente
                )
            return redirect('home')
        else:
            messages.error(request, 'Erro ao realizar o cadastro.')
  
   else:
      ficha_medica = FichaMedicaForm()
      

   context = {
      'ficha_medica': ficha_medica
   }

   return render(request,'paciente/ficha_medica.html', context=context)

# def marcar_consulta(request):
#     especialidades = Especialidade.objects.all()

#     if request.method == "POST":
#         especialidade_id = request.POST.get("especialidade")
#         medico_id = request.POST.get("medico")
#         horario_id = request.POST.get("horario")

#         especialidade = Especialidade.objects.get(id=especialidade_id)
#         medico = Medico.objects.get(id=medico_id)
#         horario = HorarioDisponivel.objects.get(id=horario_id)

#         # Criar a consulta e marcar o horário como indisponível
#         Consulta.objects.create(paciente=request.user, medico=medico, horario=horario)
#         horario.delete()  # Remove o horário disponível já marcado
#         return redirect("marcar_consulta")

#     return render(request, "paciente/marcar_consulta.html", {"especialidades": especialidades})

def marcar_consulta(request):
    if request.method == "GET":
        horarios_disponiveis = HorarioDisponivel.objects.all().select_related('medico', 'medico__especialidade')
        return render(request, "paciente/marcar_consulta.html", {"horarios_disponiveis": horarios_disponiveis})

    elif request.method == "POST":
        horario_id = request.POST.get("horario")

        horario = HorarioDisponivel.objects.get(id=horario_id)
        medico = horario.medico

        # Criar a consulta
        Consulta.objects.create(paciente=request.user.paciente, medico=medico, horario=horario)
        return redirect("marcar_consulta")