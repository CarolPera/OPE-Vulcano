from django.forms import ModelForm
from app.models import Produtos, MovimentoDeEstoque


class ProdutosForm(ModelForm):
    class Meta:
        model = Produtos
        fields = ['nome_produto', 'categoria_produto', 'quant_produto']


class MovimentoDeEstoqueForm(ModelForm):
    class Meta:
        model = MovimentoDeEstoque
        fields = ['quantidade']
