from django.shortcuts import render

from accounts.models import ChefCozinha

from .models import Pedido, Item

def index(request):
    context = {}
    return render(request,'pedidos/index.html', context)

def cardapio(request):
    item_list = Item.objects.filter(disponivel=True)
    context = {'item_list': item_list}
    return render(request, 'pedidos/cardapio.html', context)

def list_pedidos(request):
    pedidos_realizados = Pedido.objects.filter(chefcozinha=None)
    pedidos_preparacao = Pedido.objects.filter(pronto=False).exclude(chefcozinha=None)
    pedidos_prontos = Pedido.objects.filter(pronto=True).exclude(chefcozinha=None).filter(garcom=None)
    context = {
        'pedidos_realizados': pedidos_realizados,
        'pedidos_preparacao': pedidos_preparacao,
        'pedidos_prontos': pedidos_prontos,
    }
    return render(request, 'pedidos/pedidos.html', context)
