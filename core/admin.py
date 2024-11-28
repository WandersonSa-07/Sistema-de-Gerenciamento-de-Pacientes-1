from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario, Atendente, Especialidade, Medico, Paciente, Consulta, ReceitaMedica, FilaEspera

class UsuarioAdmin(UserAdmin):
    # Campos exibidos na lista de usuários no admin
    list_display = ('codigo', 'tipo', 'telefone', 'is_staff', 'is_superuser')

    # Campos clicáveis para acessar os detalhes
    list_display_links = ('codigo',)

    # Campos de filtro na lateral
    list_filter = ('tipo', 'is_staff', 'is_superuser', 'is_active')

    # Configura os campos para o formulário de edição
    fieldsets = (
        (None, {'fields': ('codigo', 'password')}),
        ('Informações Pessoais', {'fields': ('tipo', 'telefone', 'email')}),
        ('Permissões', {'fields': ('is_staff', 'is_superuser', 'is_active', 'groups', 'user_permissions')}),
        ('Datas importantes', {'fields': ('last_login', 'date_joined')}),
    )

    # Campos exibidos ao criar um novo usuário
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('codigo', 'tipo', 'telefone', 'email', 'password1', 'password2'),
        }),
    )

    # Define que a busca será feita pelo código
    search_fields = ('codigo', 'email', 'telefone')

    # Define a ordenação padrão
    ordering = ('codigo',)


# Registra o modelo com o admin customizado
admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Atendente)
admin.site.register(Especialidade)
admin.site.register(Medico)
admin.site.register(Paciente)
admin.site.register(Consulta)
admin.site.register(ReceitaMedica)
admin.site.register(FilaEspera)