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

def detail_item(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    context = {'item': item}
    return render(request, 'pedidos/detail_item.html', context)

def update_item(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    if request.method == 'POST':
        item_form = ItemForm(request.POST)
        if item_form.is_valid():
            item.nome = item_form.cleaned_data['nome']
            item.preco = item_form.cleaned_data['preco']
            item.descricao = item_form.cleaned_data['descricao']
            item.foto_url = item_form.cleaned_data['foto_url']
            item.disponivel = item_form.cleaned_data['disponivel']
            item.save()
            return HttpResponseRedirect(
                reverse('pedidos:detail_item', args=(item.pk, ))
            )
    else:
        item_form = ItemForm(
            initial={
                'nome': item.nome,
                'preco': item.preco,
                'descricao': item.descricao,
                'foto_url': item.foto_url,
                'disponivel': item.disponivel,
            }
        )
    context = {'item_form': item_form, 'item': item}
    return render(request, 'pedidos/update_item.html', context)

def delete_item(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    if request.method == 'POST':
        item.delete()
        return HttpResponseRedirect(reverse('pedidos:index'))
    context = {'item': item}
    return render(request, 'pedidos/delete_item.html', context)

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
