from django.urls import path

from . import views

app_name = 'pedidos'
urlpatterns = [
    path('', views.index, name='index'),
    path('pedidos/', views.list_pedidos, name='pedidos'),
    path('cardapio/', views.cardapio, name='cardapio'),
    path('cardapio/<int:item_id>/', views.detail_item, name='detail_item'),
    path('cardapio/create/', views.create_item, name='create_item'),
]
