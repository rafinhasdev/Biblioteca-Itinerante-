from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, LoginForm, PerfilForm
from django.contrib.auth.models import Group
from .models import Usuario
from .forms import UsuarioFiltroForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def cadastrar_usuarios(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()

            group_simples = Group.objects.get(name='Cliente')
            user.groups.add(group_simples)

            messages.success(request, 'Usuário cadastrado com sucesso!')
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'cadastrar_usuarios.html', {'form': form})

def login_view(request):
    if request.user.is_authenticated:
        return redirect('listar_livros')
    
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')

            user = authenticate(request, email=email, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, 'Login realizado com sucesso!')
                return redirect('listar_livros')
            else:
                messages.error(request, 'Credenciais inválidas. Por favor, tente novamente.')
        else:
            messages.error(request, 'Erro no login. Por favor, tente novamente.')
    else:
        form = LoginForm()
    
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.success(request, 'Logout realizado com sucesso!')
    return redirect('login')

@login_required
def perfil_view(request):
    if request.method == 'POST':
        form = PerfilForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Perfil atualizado com sucesso!')
            return redirect('perfil')
    else:
        form = PerfilForm(instance=request.user)
    
    return render(request, 'perfil.html', {'form': form})

@login_required
def listar_usuarios(request):

    if not request.user.is_admistrador() and not request.user.is_superuser():
        messages.error(request, 'Você não tem permissão para acessar esta página.')
        return redirect('listar_livros')

    usuarios = Usuario.objects.all()

    filtro_form = UsuarioFiltroForm(request.GET or None)
    if filtro_form.is_valid():
        nome = filtro_form.cleaned_data.get('nome')
        if nome:
            usuarios = usuarios.filter(nome__icontains=nome)

        email = filtro_form.cleaned_data.get('email')
        if email:
            usuarios = usuarios.filter(email__icontains=email)

        group = filtro_form.cleaned_data.get('group')
        if group:
            usuarios = usuarios.filter(groups=group)

    itens_por_pagina = 10
    paginator = Paginator(usuarios, itens_por_pagina)
    page = request.GET.get('page')

    try:
        usuarios_paginados = paginator.page(page)
    except PageNotAnInteger:
        usuarios_paginados = paginator.page(1)
    except EmptyPage:
        usuarios_paginados = paginator.page(paginator.num_pages)

    return render(request, 'listar_usuarios.html', {
        'usuarios': usuarios_paginados, 
        'filtro_form': filtro_form
        })

@login_required
def criar_usuario_admin(request):

    if not request.user.is_admistrador() and not request.user.is_superuser():
        messages.error(request, 'Você não tem permissão para acessar esta página.')
        return redirect('listar_livros')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()

            grupo_simples, created = Group.objects.get_or_create(name='Cliente')
            user.groups.add(grupo_simples)

            messages.sucess(request, 'Usuário cadastrado com sucesso!')
            return redirect('listar_usuarios')
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'usuarios/form_usuarios', {'form': form, 'titulo': 'Criar Usuário'})

@login_required
def editar_usuario_admin(request, pk):

    if not request.user.is_admistrador() and not request.user.is_superuser():
        messages.error(request, 'Você não tem permissão para acessar esta página.')
        return redirect('listar_livros')
    
    usuario = get_object_or_404(Usuario, pk=pk)

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES, instance=usuario)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuário atualizado com sucesso!')
            return redirect('listar_usuarios')
    else:
        form = CustomUserCreationForm(instance=usuario)

    return render(request, 'usuarios/form_usuarios', {'form': form, 'titulo': 'Editar Usuário', 'usuario': usuario})

@login_required
def deletar_usuario(request, pk):

    if not request.user.is_admistrador() and not request.user.is_superuser():
        messages.error(request, 'Você não tem permissão para acessar esta página.')
        return redirect('listar_livros')
    
    usuario = get_object_or_404(Usuario, pk=pk)
    
    if usuario == request.user:
        messages.error(request, 'Você não pode deletar a si mesmo.')
        return redirect('listar_usuarios')
    
    if usuario.is_superuser:
        messages.error(request, 'Você não pode deletar um superusuário.')
        return redirect('listar_usuarios')

    if request.method == 'POST':
        usuario.delete()
        messages.success(request, 'Usuário deletado com sucesso!')
        return redirect('listar_usuarios')

    return render(request, 'usuarios/confirmar_exclusao.html', {'usuario': usuario})





