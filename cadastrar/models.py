from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.auth.admin import UserAdmin
from django.conf import settings

ESTADO_CHOICES = (
    ("AC", "Acre"),
    ("AL", "Alagoas"),
    ("PI", "Piauí"),
    ("CE", "Ceará"),
    ("PE", "Pernambuco")
)

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    dt_criacao = models.DateField(auto_now_add=True)

    def __str__(self):
        return f' {self.nome}'

class Produto(models.Model):
    foto = models.ImageField(upload_to='Foto_produtos', null=True, blank=True)
    descricao = models.CharField(max_length=200)
    preco = models.DecimalField(max_digits=7, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pausar = models.BooleanField(null=False, blank=True, default=False)

    def __str__(self):
        return f' {self.descricao}'

class UsuarioPerfil(models.Model):

     user = models.OneToOneField(User, on_delete=models.CASCADE)
     celular = models.CharField(null=False, verbose_name="Celular", max_length=19)
     endereco = models.CharField(max_length=50, null=False,verbose_name="Endereço")
     cidade = models.CharField(max_length=50, null=False, verbose_name="Cidade")
     uf = models.CharField(null=False, choices=ESTADO_CHOICES, max_length =15)

class Movimentacao(models.Model):
    descricao = models.CharField(max_length=200)
    preco = models.DecimalField(max_digits=7, decimal_places=2)
    vendedor = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)
    comprador = models.ForeignKey(User, on_delete=models.CASCADE)
    celular = models.CharField(null=False, verbose_name="Celular", max_length=19)
    endereco = models.CharField(max_length=50, null=False, verbose_name="Endereço")
    cidade = models.CharField(max_length=50, null=False, verbose_name="Cidade")
    uf = models.CharField(null=False, choices=ESTADO_CHOICES, max_length=15)
    email = models.EmailField(max_length=60)

    def __str__(self):
        return f' {self.descricao} - {self.comprador}'
