from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Livro
from .forms import LivroForm, FiltroForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

@login_required
def listar_livros(request):
    livros = Livro.objects.all()

    filtro_form = FiltroForm(request.GET)
    if filtro_form.is_valid():
        categoria = filtro_form.cleaned_data['categoria']
        editora = filtro_form.cleaned_data['editora']
        autor = filtro_form.cleaned_data['autor']

        if categoria:
            livros = livros.filter(categoria__nome__icontains=categoria)
        if editora:
            livros = livros.filter(editora__nome__icontains=editora)
        if autor:
            livros = livros.filter(autor__icontains=autor)
        
    itens_por_pagina = 5
    paginator = Paginator(livros, itens_por_pagina)
    page = request.GET.get('page')
    try:
        livros = paginator.page(page)
    except PageNotAnInteger:
        livros = paginator.get_page(1)
    except EmptyPage:
        livros = paginator.get_page(paginator.num_pages)

    context = {
        'livros': livros,
        'filtro_form': filtro_form,
        'titulo': 'Livros',
        'page': page
    }

    return render(request, 'biblioteca/index.html', context)

@login_required
def adicionar_livro(request):
    if request.method == 'POST':
        form = LivroForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Livro adicionado com sucesso!')
            return redirect('listar_livros')
    else:
        form = LivroForm()
    return render(request, 'biblioteca/adicionar_livro.html', {'form': form, 'titulo': 'Cadastrar Livro'})

@login_required
def editar_livro(request, pk):
    livro = get_object_or_404(Livro, pk=pk)
    if request.method == 'POST':
        form = LivroForm(request.POST, request.FILES, instance=livro,)
        if form.is_valid():
            form.save()
            messages.success(request, 'Livro editado com sucesso!')
            return redirect('listar_livros')
    else:
        form = LivroForm(instance=livro)

    return render(request, 'biblioteca/editar_livro.html', {'form': form, 'titulo': 'Editar Livro'})

@login_required
def deletar_vaga(request, pk):
    livro = get_object_or_404(Livro, pk=pk)
    if request.method == 'POST':
        livro.delete()
        messages.success(request, 'Livro deletado com sucesso!')
        return redirect('listar_livros')
    return render(request, 'biblioteca/deletar_livro.html', {'livro': livro})
