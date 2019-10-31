"""agroX URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from rest_framework import routers
from api.viewsets import CategoriaViewSet, MeusProdutoViewSet,ProdutosViewSet

#
router = routers.DefaultRouter()
# #router.register(r'produto/id', MostraProdutoViewSet, base_name='api_produto')
router.register(r'produtos/', ProdutosViewSet, base_name='api_produtos')
router.register(r'categoria/', CategoriaViewSet, base_name='api_categoria')
router.register(r'meus_Produtos/user-id/', MeusProdutoViewSet, base_name="api_meusProduto")
#outer.register(r'obterToken/', CustomAuthToken, base_name="token")


urlpatterns = [
    path('', include('cadastrar.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    path('api/', include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
