from django.shortcuts import render, redirect
from django.contrib import messages
from core.forms.registroForm import MedicoForm, UsuarioMedico

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