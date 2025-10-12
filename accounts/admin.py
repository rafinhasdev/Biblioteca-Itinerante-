from django.contrib import admin
from .models import Usuario
from django.contrib.auth.admin import UserAdmin



@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
    model = Usuario
    list_display = ['email', 'nome', 'sobrenome', 'is_staff', 'is_active']
    list_filter = ['is_staff', 'is_active', 'groups']
    search_fields = ['email', 'nome', 'sobrenome']
    ordering = ['email']

    fieldsets = UserAdmin.fieldsets + (
        ('Informações Adicionais', {
            'fields': ('cpf', 'endereco', 'telefone', 'data_nascimento', 'cargo', 'foto_perfil')
            }),
         )
    
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Informações Adicionais', {
            'fields': ('cpf', 'endereco', 'telefone', 'data_nascimento', 'cargo', 'foto_perfil')
            }),
    )
