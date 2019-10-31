from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .models import Produto, UsuarioPerfil, Movimentacao
from .forms import CadastraForm, UsuarioForm,PausarForm, MovimentacaoForm
from .forms import ExtendeUsercreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm,  PasswordChangeForm # Formulario de criacao de usuarios
from django.contrib.auth import update_session_auth_hash, authenticate, login
from  django.contrib import messages



def menu(request):
    return render(request,'menu.html')


def lista_produtos(request):
    termo_busca = request.GET.get('pesquisa', None)

    if termo_busca:
        product = Produto.objects.all().order_by('preco')
        product = product.filter(descricao__icontains=termo_busca)
    else:
        product = Produto.objects.filter(pausar=False)

    return render(request, 'listagem_produto.html', {'product': product})


@login_required
def cadastra_produtos(request):
    form = CadastraForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        messages.success(request, 'Produto cadastro com sucesso!')
        return redirect('meus_produto')
    return render(request, 'cadastrar_produto.html', {'form': form})


@login_required
def alterar_produtos(request, id):
    product = get_object_or_404(Produto, pk=id)
    form = CadastraForm(request.POST or None, request.FILES or None, instance=product)

    if form.is_valid():
        form.save()
        messages.success(request, 'Produto atualizado com sucesso!')
        return redirect('meus_produto')

    return render(request, 'cadastrar_produto.html', {'form': form})

@login_required
def deletar_produtos(request, id):
    product = get_object_or_404(Produto, pk=id)

    if request.method == 'POST':
        product.delete()
        messages.success(request, 'Produto excluido com sucesso!')
        return redirect('meus_produto')

    return render(request, 'deletar_produto.html', {'product': product})


def mostrar_produto(request, id):
    product = Produto.objects.filter(pk=id)
    return render(request, 'mostrar_produto.html', {'product': product})

@login_required
def pausar(request, id):
    marcar = Produto.objects.get(id=id)
    pausar = PausarForm(request.POST or None,instance=marcar)
    if pausar.is_valid():
        pausar.save()
        messages.success(request, 'Produto Pausado!')
        return redirect('lista')

    return render(request, 'pausar.html', {'pausar': pausar})

def sobre(request):
    return render(request, 'sobre.html')


@login_required
def meus_produto(request):
    product = Produto.objects.filter(user=request.user.id)
    return render(request, 'meus_produto.html', {'product': product})

def minhas_compras(request):
    product = Movimentacao.objects.filter(comprador=request.user.id)
    return render(request, 'minhas_compras.html', {'product': product})

def minhas_vendas(request):
    product = Movimentacao.objects.filter(vendedor=request.user.id)
    return render(request, 'minhas_vendas.html', {'product': product})

@login_required
def deletar_user(request):
    user = request.user
    if request.method == 'POST':
        user.delete()
        messages.success(request, 'Produto atualizado com sucesso!')
        return redirect('lista')

    return render(request, 'deletar_user.html', {'user': user})


def registrar(request):
        if request.method == 'POST':
            form = ExtendeUsercreationForm(request.POST)

            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                raw_pass = form.cleaned_data.get('password1')
                user = authenticate(request, username=username, password=raw_pass)
                login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                messages.success(request, 'Registrado com sucesso, preencha o formulário abaixo para completa o cadastro!')

                return redirect('dados_usuario')
            else:
                return render(request, "registrar.html", {"form": form})

        return render(request, 'registrar.html', {'form': ExtendeUsercreationForm})

@login_required(login_url='login')
def usuario_dados(request):
    form = UsuarioForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        messages.success(request, 'Cadastrado com sucesso!')
        return redirect('lista')
    return render(request, 'cadastrar_dados.html', {'form': form})

@login_required
def alterar_dados(request):
    perfil = get_object_or_404(UsuarioPerfil, user=request.user.id)
    form = UsuarioForm(request.POST or None, request.FILES or None, instance=perfil)

    if form.is_valid():
        form.save()
        messages.success(request, 'Atualizado com sucesso!')
        return redirect('lista')

    return render(request, 'alterar_dados.html', {'form': form})

# @login_required
# def alterar_usuario(request, id):
#     usuario = get_object_or_404(Usuario, pk=id)
#     form = CadastraForm(request.POST or None, request.FILES or None, instance=usuario)
#
#     if form.is_valid():
#         form.save()
#         return redirect('lista')
#
#     return render(request, 'alterar_dados.html', {'form': form})

@login_required
def alterar_senha(request):
    if request.method == "POST":
        form_senha = PasswordChangeForm(request.user, request.POST)
        if form_senha.is_valid():
            user = form_senha.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Senha alterada com sucesso!')
            return redirect('menu')
    else:
        form_senha = PasswordChangeForm(request.user)
    return render(request, 'alterar_senha.html', {'form_senha': form_senha})

@login_required
def movimentacao(request,id):
    prod = Produto.objects.get(id=id)
    form = MovimentacaoForm(request.POST or None, request.FILES or None, instance=prod)
    movim = MovimentacaoForm(request.POST or None, request.FILES or None)
    if movim.is_valid():
        movim.save()
        messages.success(request, 'Compra realizada com sucesso!')
        return redirect('lista')

    return render(request, 'movimentacao.html', {'form': form})
