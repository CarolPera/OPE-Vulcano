from django.contrib import admin
from .models import Estoque, EstoqueItens, Produtos


class EstoqueItensInline(admin.TabularInline):
    model = EstoqueItens
    extra = 0


@admin.register(Estoque)
class EstoqueAdmin(admin.ModelAdmin):
    inlines = (EstoqueItensInline,)
    list_display = ('__str__', 'nf')
    search_fields = ('nf',)
    list_filter = ('funcionario',)
    date_hierarchy = 'created'


@admin.register(Produtos)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = (
        '__str__',
        'ncm',
        'estoque',
        'estoque_minimo',
    )
    search_fields = ('produto',)

