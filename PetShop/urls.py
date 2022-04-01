"""PetShop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from atendimento.views import listagem, delete, atualizar, novo_atendimento, novo_pet, novo_responsavel, \
    lista_pet, lista_responsaveis, home, atualizar_pet, atualizar_responsavel, deleteResponsavel, deletePet

urlpatterns = [
    path('', home, name='url_home'),
    path('admin/', admin.site.urls),
    path('lista/', listagem, name='url_lista'),
    path('lista_pets/', lista_pet, name='url_lista_pet'),
    path('lista_responsaveis/', lista_responsaveis, name='url_lista_responsavel'),
    path('delete/<int:pk>/', delete, name="url_delete"),
    path('delete_pet/<int:pk>/', deletePet, name="url_delete_pet"),
    path('delete_responsavel/<int:pk>/', deleteResponsavel, name="url_delete_responsavel"),
    path('atualizar/<int:pk>/', atualizar, name="url_atualizar"),
    path('atualizar_pet/<int:pk>/', atualizar_pet, name="url_atualizar_pet"),
    path('atualizar_responsavel/<int:pk>/', atualizar_responsavel, name="url_atualizar_responsavel"),
    path('novo_atendimento/', novo_atendimento, name="url_novoatendimento"),
    path('novo_pet/', novo_pet, name="url_novopet"),
    path('novo_responsavel/', novo_responsavel, name="url_novoresponsavel"),
    path('', include('usuarios.urls'))
]
