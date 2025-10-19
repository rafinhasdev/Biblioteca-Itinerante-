from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Usuario
from django.contrib.auth.models import Group


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['email', 'password1', 'password2', 'cpf', 'nome', 'sobrenome', 'endereco', 'telefone', 'data_nascimento', 'cargo', 'foto_perfil']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Senha'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirmar Senha'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'CPF'}),
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome'}),
            'sobrenome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Sobrenome'}),
            'endereco': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Endereço'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Telefone'}),
            'data_nascimento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'placeholder': 'Data de Nascimento'}),
            'cargo': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Cargo'}),
            'foto_perfil': forms.FileInput(attrs={'class': 'form-control', 'placeholder': 'Foto de Perfil'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Senha'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Confirme a senha'})

class LoginForm(AuthenticationForm):
    username = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Senha'}))



class PerfilForm(forms.ModelForm):
    model = Usuario
    fields = ['cpf', 'nome', 'sobrenome', 'email', 'endereco', 'telefone', 'data_nascimento', 'cargo', 'foto_perfil']
    widgets = {
        'cpf': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'CPF'}),
        'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome'}),
        'sobrenome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Sobrenome'}),
        'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
        'endereco': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Endereço'}),
        'telefone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Telefone'}),
        'data_nascimento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        'cargo': forms.Select(attrs={'class': 'form-control'}),
        'foto_perfil': forms.FileInput(attrs={'class': 'form-control'}),
    }

class UsuarioFiltroForm(forms.Form):
    nome = forms.CharField(
        required=False, 
        label='Nome',
        widget=forms.TextInput(attrs={
            'class': 'form-control', 
            'placeholder': 'Buscar por nome: '
            })
        )
    
    email = forms.EmailField(
        required=False, 
        label='Email',
        widget=forms.EmailInput(attrs={
            'class': 'form-control', 
            'placeholder': 'Buscar por email: '
            })
    )

    cpf = forms.CharField(
        required=False, 
        label='CPF',
        widget=forms.TextInput(attrs={
            'class': 'form-control', 
            'placeholder': 'Buscar por CPF: '
            })
    )

    group = forms.ModelChoiceField(
        queryset=Group.objects.all(),
        required=False,
        label='Grupo',
        widget=forms.Select(attrs={
            'class': 'form-control', 
            'placeholder': 'Buscar por grupo: '
            })
    )

        
