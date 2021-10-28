from django.shortcuts import render, redirect
from app.forms import ProdutosForm, Estoque
from app.models import Produtos


def home(request):
    data = {}
    data['db'] = Produtos.objects.all()
    return render(request, 'index.html', data)


def form(request):
    data = {}
    data['form'] = ProdutosForm
    return render(request, 'form.html', data)


def create(request):
    form = ProdutosForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')


def view(request, pk):
    data = {}
    data['db'] = Produtos.objects.get(pk=pk)
    return render(request, 'view.html', data)


def edit(request, pk):
    data = {}
    data['db'] = Produtos.objects.get(pk=pk)
    data['form'] = ProdutosForm(instance=data['db'])
    return render(request, 'form.html', data)


def update(request, pk):
    data = {}
    data['db'] = Produtos.objects.get(pk=pk)
    form = ProdutosForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('home')


def delete(request, pk):
    db = Produtos.objects.get(pk=pk)
    db.delete()
    return redirect('home')

def addProduto(request, pk, quantidade):
    if request.method == 'PUT':
        data = {}
        data['db'] = Produtos.objects.get(pk=pk)
        form = ProdutosForm(request.POST or None, instance=data['db'])
        if form.is_valid():
            form.estoque += quantidade
            form.save()
    return redirect('home')



def removeProduto(request, pk):
    data = {}
    data['db'] = Produtos.objects.get(pk=pk)
    form = ProdutosForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('home')
