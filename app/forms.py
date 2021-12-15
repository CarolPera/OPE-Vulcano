from django.forms import ModelForm
from app.models import Produtos, MovimentoDeEstoque, Vendas, Compras


class ProdutosForm(ModelForm):
    class Meta:
        model = Produtos
        fields = ['nome_produto', 'categoria_produto', 'quant_produto']


class MovimentoDeEstoqueForm(ModelForm):
    class Meta:
        model = MovimentoDeEstoque
        fields = ['quantidade']


class VendasForm(ModelForm):
    class Meta:
        model = Vendas
        fields = ['data', 'valor', 'forma_de_pagamento', 'descricao']


class ComprasForm(ModelForm):
    class Meta:
        model = Compras
        fields = ['data', 'valor', 'descricao']
