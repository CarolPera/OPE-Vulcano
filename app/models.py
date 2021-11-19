from django.db import models


class Produtos(models.Model):
    nome_produto = models.CharField(max_length=120)
    quant_produto = models.IntegerField()
