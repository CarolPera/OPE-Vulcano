from django.forms import ModelForm
from app.models import Produtos


class ProdutosForm(ModelForm):
    class Meta:
        model = Produtos
        fields = ['nome_produto','categoria_produto','quant_produto']