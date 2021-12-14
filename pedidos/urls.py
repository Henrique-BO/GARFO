from django.urls import path

from . import views

app_name = 'pedidos'
urlpatterns = [
    path('', views.index, name='index'),
    path('pedidos/', views.list_pedidos, name='pedidos'),
    path('cardapio/', views.cardapio, name='cardapio'),
    #path('cardapio/<int:item_id>/pedir/', views.fazer_pedido, name='fazer_pedido'),
    #path('cardapio/create/', views.create_item, name='create_item'),
    #path('cardapio/<int:item_id>/update/', views.update_item, name='update_item'),
    path('contas/', views.list_contas, name='list_contas'),
    #path('contas/<int:conta_id>/', views.detail_conta, name='detail_conta'),
    #path('contas/pedir/', views.pedir_conta, name='pedir_conta'),
    path('mesas/', views.list_mesas, name='list_mesas'),
    #path('mesas/<int:mesa_id>/', views.detail_mesa, name='detail_mesa'),
    #path('mesas/create/', views.create_mesa, name='create_mesa'),
    #path('mesas/<int:mesa_id>/update/', views.update_mesa, name='update_mesa'),
]
