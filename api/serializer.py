from rest_framework import serializers
from cadastrar.models import Produto, Categoria


class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = '__all__'

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ('nome', 'dt_criacao')

