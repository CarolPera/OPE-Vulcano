from django.shortcuts import render, redirect, get_object_or_404
from app.forms import ProdutosForm, MovimentoDeEstoqueForm, VendasForm
from app.models import Produtos, Vendas


def login(request):
    return render(request, 'login.html')


def home(request):
    return render(request, 'index.html')


def cardapio(request):
    data = {}
    data['db'] = Produtos.objects.all()
    return render(request, 'cardapio.html')


def estoque(request):
    data = {}
    data['db'] = Produtos.objects.all()
    return render(request, 'estoque.html', data)


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


def entrada(request, pk):
    data = {}
    data['db'] = Produtos.objects.get(pk=pk)
    data['form'] = ProdutosForm(instance=data['db'])
    return render(request, 'cadastro-entrada.html', data)


def saida(request, pk):
    data = {}
    data['db'] = Produtos.objects.get(pk=pk)
    data['form'] = ProdutosForm(instance=data['db'])
    return render(request, 'cadastro-saida.html', data)


def vendas(request):
    data = {}
    data['db'] = Vendas.objects.all()
    return render(request, 'vendas.html', data)


def formVendas(request):
    data = {}
    data['formVenda'] = VendasForm
    return render(request, 'cadastroVenda.html', data)


def createVenda(request):
    form = VendasForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('vendas')


def viewVenda(request, pk):
    data = {}
    data['db'] = Vendas.objects.get(pk=pk)
    return render(request, 'viewVendas.html', data)


def editVenda(request, pk):
    data = {}
    data['db'] = Vendas.objects.get(pk=pk)
    data['formVenda'] = VendasForm(instance=data['db'])
    return render(request, 'cadastroVenda.html', data)


def updateVenda(request, pk):
    data = {}
    data['db'] = Vendas.objects.get(pk=pk)
    form = VendasForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('vendas')


def deleteVenda(request, pk):
    db = Vendas.objects.get(pk=pk)
    db.delete()
    return redirect('vendas')