from django.urls import path
from .views import lista_produtos, cadastra_produtos, alterar_produtos, deletar_produtos, mostrar_produto, \
meus_produto, registrar, menu, pausar,alterar_senha, deletar_user,usuario_dados, alterar_dados, movimentacao, \
minhas_compras, minhas_vendas, sobre


urlpatterns = [
    path('', lista_produtos, name='lista'),
    path('sobre', sobre, name='sobre'),
    path('novo/', cadastra_produtos, name='novo_produto'),
    path('dados_usuario', usuario_dados, name='dados_usuario'),
    path('alterar/<int:id>/', alterar_produtos, name='alterar_produtos'),
    path('alterar_dados/', alterar_dados, name='alterar_dados'),
    path('deletar/<int:id>/', deletar_produtos, name='deletar_produtos'),
    path('deletar_user', deletar_user, name='deletar_user'),
    path('mostrar/<int:id>/', mostrar_produto, name='mostrar_produto'),
    path('pausar/<int:id>/', pausar, name='pausar'),
    path('meus_produto/', meus_produto,  name='meus_produto'),
    path('menu/', menu, name='menu'),
    path('registrar/', registrar, name='registrar'),
    path('alterar_senha/', alterar_senha, name='alterar_senha'),
    path('movimentacao/<int:id>/', movimentacao, name='movimentacao'),
    path('minhas_compras/', minhas_compras, name='minhas_compras'),
    path('minhas_vendas/', minhas_vendas, name='minhas_vendas'),
]
