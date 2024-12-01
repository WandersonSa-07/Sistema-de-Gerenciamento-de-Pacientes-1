from django.contrib import messages
from django.shortcuts import redirect, render
from core.forms.registroForm import PacienteForm, UsuarioPaciente, FichaMedicaForm
from core.models import FichaMedica

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