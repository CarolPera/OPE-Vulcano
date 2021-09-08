from django.db import models


class Produtos(models.Model):
    nome_produto = models.CharField(max_length=120)
    categoria_produto = models.CharField(max_length=150)
    quant_produto = models.IntegerField()
    data_vencimento = models.DateField()
