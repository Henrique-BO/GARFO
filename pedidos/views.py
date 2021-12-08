from django.shortcuts import get_object_or_404, render, HttpResponseRedirect
from django.urls import reverse

from accounts.models import ChefCozinha
from pedidos.forms import ItemForm

from .models import Pedido, Item

def index(request):
    context = {}
    return render(request,'pedidos/index.html', context)

def cardapio(request):
    item_list = Item.objects.filter(disponivel=True)
    context = {'item_list': item_list}
    return render(request, 'pedidos/cardapio.html', context)

def detail_item(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    context = {'item': item}
    return render(request, 'pedidos/detail_item.html', context)

def create_item(request):
    if request.method == 'POST':
        item_form = ItemForm(request.POST)
        if item_form.is_valid():
            item = Item(**item_form.cleaned_data)
            item.save()
            return HttpResponseRedirect(
                reverse('pedidos:detail_item', args=(item.pk, ))
            )
    else:
        item_form = ItemForm()
    context = {'item_form': item_form}
    return render(request, 'pedidos/create_item.html', context)

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
