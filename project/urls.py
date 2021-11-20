from django.contrib import admin
from django.urls import path
from app.views import login, home, estoque, cardapio, carrinho, form, create, view, edit, update, delete, entrada, saida
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('login/', login, name='login'),
    path('estoque/', estoque, name='estoque'),
    path('cardapio/', cardapio, name='cardapio'),
    path('carrinho/', carrinho, name='carrinho'),
    path('cadastro/', form, name='form'),
    path('create/', create, name='create'),
    path('view/<int:pk>/', view, name='view'),
    path('edit/<int:pk>/', edit, name='edit'),
    path('update/<int:pk>/', update, name='update'),
    path('delete/<int:pk>/', delete, name='delete'),
    path('entrada/<int:pk>/', entrada, name='entrada'),
    path('saida/<int:pk>/', saida, name='saida'),
] + static('/', document_root='templates/')
