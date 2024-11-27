from pyexpat.errors import messages
from django.shortcuts import render, get_object_or_404, redirect
from core.forms.registroForm import PacienteForm
from core.models import ReceitaMedica
from weasyprint import HTML
import weasyprint
from django.http import HttpResponse
from django.template.loader import render_to_string

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

def visualizar_receita(request, receita_id):
   receita = get_object_or_404(ReceitaMedica, id=receita_id)
   pdf_gerado = render_to_string("receita_pdf.html", {"receita":receita})
   pdf = HTML(string = pdf_gerado).write_pdf()

   response = HttpResponse(pdf, content_type='application/pdf')
   response['Content-Disposition'] = f'attachment; filename="receita{receita.id}.pdf"'
   return response