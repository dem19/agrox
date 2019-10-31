from django.forms import ModelForm
from .models import Produto, UsuarioPerfil, Movimentacao

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError

class CadastraForm(ModelForm):
    class Meta:
        model = Produto
        fields = ['foto', 'descricao', 'preco', 'categoria', 'user']

class PausarForm(ModelForm):
    class Meta:
        model = Produto
        fields = ['foto', 'descricao', 'preco', 'categoria', 'user', 'pausar']


class MovimentacaoForm(ModelForm):
    class Meta:
        model = Movimentacao
        fields = ['descricao', 'preco', 'vendedor', 'comprador', 'celular', 'endereco', 'cidade', 'uf', 'email']


class ExtendeUsercreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=40)
    last_name = forms.CharField(max_length=150)

    class Meta:
        model = User
        fields = ( 'username', 'email', 'first_name', 'last_name', 'password1', 'password2')

        def save(self, commit=True):
            user = super().save(commit=False)

            user.email = self.cleaned_data['email']
            user.first_name = self.cleaned_data['first_name']
            user.last_name = self.cleaned_data['last_name']

            if commit:
                user.save()
            return user

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = UsuarioPerfil
        fields = ['user', 'celular', 'endereco', 'cidade', 'uf']

