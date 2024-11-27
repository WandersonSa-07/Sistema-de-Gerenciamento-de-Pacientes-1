from django.contrib import messages
from django.shortcuts import redirect, render
from core.forms.registroForm import PacienteForm, UsuarioForm

def pacienteRegistro(request):
    if str(request.method) == 'POST':
        paciente_form = PacienteForm(request.POST)
        usuario_form = UsuarioForm(request.POST)

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
        usuario_form = UsuarioForm()

    context = {
        'paciente_form': paciente_form,
        'usuario_form': usuario_form
    }

    return render(request, 'registro.html', context=context)
