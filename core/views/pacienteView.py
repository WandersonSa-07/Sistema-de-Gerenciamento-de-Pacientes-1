from pyexpat.errors import messages
from django.shortcuts import render
from core.forms.registroForm import PacienteForm

def pacienteRegistro(request):
   if str(request.method) == 'POST':
      form = PacienteForm(request.POST)
      if form.is_valid():
         paciente = form.save()

         print(f'codigo: {paciente.codigo}')

         messages.sucess(request, 'Cadastro realizado com sucesso.')
      else:
         messages.error(request, 'Erro ao realizar o cadastro.')
   else:
      form = PacienteForm()
   
   context = {
      'form': form
   }

   return render(request,'registro.html', context=context)