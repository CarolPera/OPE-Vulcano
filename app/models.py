import decimal

from django.db import models
from djmoney.models.fields import MoneyField


class Produtos(models.Model):
    nome_produto = models.CharField(max_length=120)
    categoria_produto = models.CharField(max_length=150)
    quant_produto = models.IntegerField()


class MovimentoDeEstoque(models.Model):
    quantidade = models.IntegerField()


class Vendas(models.Model):
    data = models.DateField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    forma_de_pagamento = models.CharField(max_length=50)
    descricao = models.CharField(max_length=120)


class Compras(models.Model):
    data = models.DateField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.CharField(max_length=120)
