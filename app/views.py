from django.shortcuts import render, redirect, get_object_or_404
from app.forms import ProdutosForm, MovimentoDeEstoqueForm
from app.models import Produtos


def login(request):
    return render(request, 'login.html')


def home(request):
    return render(request, 'index.html')


def estoque(request):
    data = {}
    data['db'] = Produtos.objects.all()
    return render(request, 'estoque.html', data)


def cardapio(request):
    data = {}
    data['db'] = Produtos.objects.all()
    return render(request, 'cardapio.html')


def carrinho(request):
    data = {}
    data['db'] = Produtos.objects.all()
    return render(request, 'carrinho.html')


def form(request):
    data = {}
    data['form'] = ProdutosForm
    return render(request, 'cadastro.html', data)


def create(request):
    form = ProdutosForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('estoque')


def createMovimentoEntrada(request):
    formEntrada = MovimentoDeEstoqueForm(request.POST or None)
    if formEntrada.is_valid():
        formEntrada.save()
        return redirect('estoque')


def createMovimentoSaida(request):
    formSaida = MovimentoDeEstoqueForm(request.POST or None)
    if formSaida.is_valid():
        formSaida.save()
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


def entrada(request, pk):
    data = {}
    data['db'] = Produtos.objects.get(pk=pk)
    data['form'] = ProdutosForm(instance=data['db'])
    return render(request, 'cadastro-entrada.html', data)

    # formEntrada = MovimentoDeEstoqueForm()
    #
    # if request.method == 'POST':
    #     return redirect('estoque')
    # else:
    #     return render(request, 'cadastro-entrada.html')

# def calcEntrada(request, pk)


def saida(request, pk):
    data = {}
    data['db'] = Produtos.objects.get(pk=pk)
    data['form'] = ProdutosForm(instance=data['db'])
    return render(request, 'cadastro-saida.html', data)