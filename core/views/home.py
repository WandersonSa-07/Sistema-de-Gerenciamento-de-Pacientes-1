from django.shortcuts import render

def home_view(request):
    if request.user.is_authenticated:
        if request.user.tipo == 'paciente':
            return render(request, template_name='paciente/paciente.html')
        elif request.user.tipo == 'medico':
            return render(request, template_name='medico/medico.html')
        elif request.user.tipo == 'atendente':
            return render(request, template_name='atendente/atendenteHome.html')
    else:
        return render(request, template_name='home/home.html')
