from rest_framework.viewsets import ModelViewSet
from .serializer import ProdutoSerializer, CategoriaSerializer
from cadastrar.models import Produto, Categoria
from rest_framework import generics

# class MeusProdutoViewset(generics):
#     queryset = Produto.objects.filter(produtor=id)
#     serializer_class = ProdutoSerializer

class ProdutosViewSet(ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

# class Mostrar_produtoViewSet(ModelViewSet):
#     queryset = Produto.objects.filter(id)
#     serializer_class = ProdutoSerializer

class MeusProdutoViewSet(ModelViewSet):
    serializer_class = ProdutoSerializer
    def get_queryset(self):
        return Produto.objects.filter(user=self.request.user.id)


