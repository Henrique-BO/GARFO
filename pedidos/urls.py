from django.urls import path

from . import views

app_name = 'pedidos'
urlpatterns = [
    path('', views.index, name='index'),
    path('pedidos/', views.list_pedidos, name='pedidos'),
    path('cardapio/', views.cardapio, name='cardapio'),
    path('cardapio/<int:item_id>/', views.detail_item, name='detail_item'),
    path('cardapio/create/', views.create_item, name='create_item'),
    path('cardapio/<int:item_id>/update/', views.update_item, name='update_item'),
    path('cardapio/<int:item_id>/delete/', views.delete_item, name='delete_item'),
    path('contas/', views.list_contas, name='list_contas'),
    path('contas/<int:conta_id>/', views.detail_conta, name='detail_conta'),
    path('contas/pedir/', views.pedir_conta, name='pedir_conta'),
]
