from django.shortcuts import render, redirect
from django.contrib import messages
from core.forms.registroForm import AtendenteForm, UsuarioAtendente

def atendenteView(request):
        return render(request, template_name='atendente/atendente.html')

def atendente_medicoView(request):
        return render(request, template_name='atendente/atendente_medico.html')

def atendente_pacienteView(request):
        return render (request, template_name='atendente/atendente_paciente.html')

def atendente_medicoCadastro(request):
     return render (request, template_name='atendente/atendente_medicoCadastro.html')

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
   print("testando")

   return render(request,'atendente/cadastro_atendente.html', context=context)