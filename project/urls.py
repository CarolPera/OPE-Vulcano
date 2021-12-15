from django.contrib import admin
from django.urls import path
from app.views import login, home, estoque, cardapio, form, create, view, edit, update, delete, entrada, \
    saida, createMovimentoEntrada, createMovimentoSaida, vendas, formVendas, deleteVenda, updateVenda, editVenda, \
    viewVenda, createVenda, compras, formCompra, createCompra, viewCompra, editCompra, updateCompra, deleteCompra
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login, name='login'),
    path('home/', home, name='home'),
    path('estoque/', estoque, name='estoque'),
    path('cardapio/', cardapio, name='cardapio'),
    path('cadastro/', form, name='form'),
    path('create/', create, name='create'),
    path('create-movimento-entrada/', createMovimentoEntrada, name='entrada'),
    path('create-movimento-saida/', createMovimentoSaida, name='entrada'),
    path('view/<int:pk>/', view, name='view'),
    path('edit/<int:pk>/', edit, name='edit'),
    path('update/<int:pk>/', update, name='update'),
    path('delete/<int:pk>/', delete, name='delete'),
    path('entrada/<int:pk>/', entrada, name='entrada'),
    path('saida/<int:pk>/', saida, name='saida'),
    path('vendas/', vendas, name='vendas'),
    path('cadastro-vendas/', formVendas, name='formVenda'),
    path('create-vendas/', createVenda, name='createVenda'),
    path('view-vendas/<int:pk>/', viewVenda, name='viewVendas'),
    path('edit-vendas/<int:pk>/', editVenda, name='editVenda'),
    path('update-vendas/<int:pk>/', updateVenda, name='updateVenda'),
    path('delete-vendas/<int:pk>/', deleteVenda, name='deleteVenda'),
    path('compras/', compras, name='compras'),
    path('cadastro-compras/', formCompra, name='formCompras'),
    path('create-compras/', createCompra, name='createCompras'),
    path('view-compras/<int:pk>/', viewCompra, name='viewCompras'),
    path('edit-compras/<int:pk>/', editCompra, name='editCompras'),
    path('update-compras/<int:pk>/', updateCompra, name='updateCompras'),
    path('delete-compras/<int:pk>/', deleteCompra, name='deleteCompras'),
] + static('/', document_root='templates/')
