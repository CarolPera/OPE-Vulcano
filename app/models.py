from django.db import models


class Produtos(models.Model):
    nome_produto = models.CharField(max_length=120, unique=True)
    estoque = models.IntegerField('estoque atual')
    estoque_minimo = models.IntegerField('estoque minimo', default=0)

    def __str__(self):
        return self.nome_produto

