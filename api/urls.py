from django.urls import path

from . import views

urlpatterns = [
    path('cardapio/', views.ItemList.as_view()),
    path('cardapio/<int:pk>/', views.ItemDetail.as_view()),
    path('pedidos/', views.PedidoList.as_view()),
    path('pedidos/<int:pk>/', views.PedidoDetail.as_view()),
    path('mesas/', views.MesaList.as_view()),
    path('mesas/<int:pk>/', views.MesaDetail.as_view()),
    path('contas/', views.ContaList.as_view()),
    path('contas/<int:pk>/', views.ContaDetail.as_view()),
    path('clientes/', views.ClienteList.as_view()),
    path('clientes/<int:pk>/', views.ClienteDetail.as_view()),
    path('gerentes/', views.GerenteList.as_view()),
    path('gerentes/<int:pk>/', views.GerenteDetail.as_view()),
    path('garcons/', views.GarcomList.as_view()),
    path('garcons/<int:pk>/', views.GarcomDetail.as_view()),
    path('chefcozinhas/', views.ChefCozinhaList.as_view()),
    path('chefcozinhas/<int:pk>/', views.ChefCozinhaDetail.as_view()),
]