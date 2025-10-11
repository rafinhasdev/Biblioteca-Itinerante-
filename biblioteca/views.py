from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Livro
from .forms import LivroForm, FiltroForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

@login_required
def listar_livros(request):
    livros = Livro.objects.all()

    filtro_form = FiltroForm(request.GET or None)

    if filtro_form.is_valid():

        autor = filtro_form.cleaned_data.get('autor')
        if autor:
            livros = livros.filter(autor__icontains=autor)

        editora = filtro_form.cleaned_data.get('editora')
        if editora:
            livros = livros.filter(editora__icontains=editora)

        categoria = filtro_form.cleaned_data.get('categoria')
        if categoria:
            livros = livros.filter(categoria__nome__icontains=categoria)

    itens_por_pagina = 6
    paginator = Paginator(livros, itens_por_pagina)
    page = request.GET.get('page')

    try:
        livros_paginados = paginator.page(page)
    except PageNotAnInteger:
        livros_paginados = paginator.page(1)
    except EmptyPage:
        livros_paginados = paginator.page(paginator.num_pages)
    
    return render(request, 'biblioteca/listar_livros.html', {
        'livros': livros_paginados, 
        'filtro_form': filtro_form,
        'pagina': page
    })

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
