from django.shortcuts import render, redirect
from app.forms import ProdutosForm
from app.models import Produtos


def login(request):
    return render(request, 'login.html')


def home(request):
    data = {}
    data['db'] = Produtos.objects.all()
    return render(request, 'index.html', data)


def estoque(request):
    data = {}
    data['db'] = Produtos.objects.all()
    return render(request, 'estoque.html', data)


def cardapio(request):
    data = {}
    data['db'] = Produtos.objects.all()
    return render(request, 'cardapio.html')


def form(request):
    data = {}
    data['form'] = ProdutosForm
    return render(request, 'cadastro.html', data)


def create(request):
    form = ProdutosForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('estoque')


def view(request, pk):
    data = {}
    data['db'] = Produtos.objects.get(pk=pk)
    return render(request, 'view.html', data)


def edit(request, pk):
    data = {}
    data['db'] = Produtos.objects.get(pk=pk)
    data['form'] = ProdutosForm(instance=data['db'])
    return render(request, 'cadastro.html', data)


def update(request, pk):
    data = {}
    data['db'] = Produtos.objects.get(pk=pk)
    form = ProdutosForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('estoque')


def delete(request, pk):
    db = Produtos.objects.get(pk=pk)
    db.delete()
    return redirect('estoque')
