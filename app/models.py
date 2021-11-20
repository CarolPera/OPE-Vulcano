from django.db import models


class Produtos(models.Model):
    nome_produto = models.CharField(max_length=120)
    categoria_produto = models.CharField(max_length=150)
    quant_produto = models.IntegerField()


class MovimentoDeEstoque(models.Model):
    quantidade = models.IntegerField()
