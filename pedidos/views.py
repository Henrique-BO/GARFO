from django.contrib.auth import login
from django.shortcuts import get_object_or_404, render, HttpResponseRedirect
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
from django.contrib.auth.decorators import login_required, permission_required

from pedidos.forms import ItemForm, MesaForm, PedidoForm
from .models import Conta, Mesa, Pedido, Item


def index(request):
    if request.user.is_authenticated:
        try:
            request.user.cliente
            return HttpResponseRedirect(reverse('pedidos:cardapio'))
        except:
            pass
        try:
            garcom = request.user.garcom
            context = {'garcom': garcom}
            return render(request, 'pedidos/garcom.html', context)
        except ObjectDoesNotExist:
            pass
        try:
            chefcozinha = request.user.chefcozinha
            context = {'chefcozinha': chefcozinha}
            return render(request, 'pedidos/chefcozinha.html', context)
        except ObjectDoesNotExist:
            pass
        try:
            gerente = request.user.gerente
            context = {'gerente': gerente}
            return render(request, 'pedidos/gerente.html', context)
        except ObjectDoesNotExist:
            pass
    context = {}
    return render(request,'pedidos/index.html', context)

def cardapio(request):
    item_list = Item.objects.filter(disponivel=True)
    item_indisp = Item.objects.filter(disponivel=False)
    context = {'item_list': item_list, 'item_indisp': item_indisp}
    
    if request.user.is_authenticated:
        context['pode_pedir'] = True
        try:
            cliente = request.user.cliente
            for conta in Conta.objects.filter(pago=False):
                if conta.pedido_set.all()[0].cliente == cliente:
                    context['conta'] = conta
                    context['total'] = 0
                    for pedido in conta.pedido_set.all():
                        context['total'] += pedido.item.preco
                    context['pode_pedir'] = False
            if context['pode_pedir']:
                context['pedidos'] = Pedido.objects.filter(cliente=cliente).filter(conta=None)
                context['total'] = 0
                for pedido in context['pedidos']:
                    context['total'] += pedido.item.preco
        except ObjectDoesNotExist:
            context['pode_pedir'] = False
    else:
        context['pode_pedir'] = False

    return render(request, 'pedidos/cardapio.html', context)

@login_required
@permission_required('pedidos.add_item')
def create_item(request):
    if request.method == 'POST':
        item_form = ItemForm(request.POST)
        if item_form.is_valid():
            item = Item(**item_form.cleaned_data)
            item.save()
    return HttpResponseRedirect(reverse('pedidos:cardapio', args=(item.pk,)))


@login_required
@permission_required('pedidos.add_pedido')
def fazer_pedido(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    if request.method == 'POST':
        pedido_form = PedidoForm(request.POST)
        if pedido_form.is_valid():
            pedido = Pedido(
                cliente=request.user.cliente,
                item=item,
                observacoes=pedido_form.cleaned_data['observacoes'],
                time_realizado=timezone.localtime(timezone.now()),
            )
            pedido.save()
    return HttpResponseRedirect(reverse('pedidos:cardapio'))

@login_required
@permission_required('pedidos.change_item')
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
    return HttpResponseRedirect(reverse('pedidos:cardapio'))

@login_required
@permission_required('pedidos.view_pedido')
def list_pedidos(request):
    if request.method == 'POST':
        if 'preparando' in request.POST and request.user.has_perm('pedidos.preparar_pedido'):
            pedido_id = request.POST['pedido_id']
            pedido = Pedido.objects.get(pk=pedido_id)
            try:
                chefcozinha = request.user.chefcozinha
                pedido.chefcozinha = chefcozinha
                pedido.time_preparando = timezone.localtime(timezone.now())
                pedido.save()
            except ObjectDoesNotExist:
                pass
        if 'pronto' in request.POST and request.user.has_perm('pedidos.preparar_pedido'):
            pedido_id = request.POST['pedido_id']
            pedido = Pedido.objects.get(pk=pedido_id)
            try:
                pedido.time_pronto = timezone.localtime(timezone.now())
                pedido.save()
            except ObjectDoesNotExist:
                pass
        if 'entregue' in request.POST and request.user.has_perm('pedidos.entregar_pedido'):
            pedido_id = request.POST['pedido_id']
            pedido = Pedido.objects.get(pk=pedido_id)
            try:
                garcom = request.user.garcom
                pedido.garcom = garcom
                pedido.time_entregue = timezone.localtime(timezone.now())
                pedido.save()
            except ObjectDoesNotExist:
                pass
        return HttpResponseRedirect(reverse('pedidos:pedidos'))
    
    pedidos_realizados = Pedido.objects.filter(time_preparando=None)
    pedidos_preparacao = Pedido.objects.filter(time_pronto=None).exclude(time_preparando=None)
    pedidos_prontos = Pedido.objects.filter(time_entregue=None).exclude(time_preparando=None).exclude(time_pronto=None)
    context = {
        'pedidos_realizados': pedidos_realizados,
        'pedidos_preparacao': pedidos_preparacao,
        'pedidos_prontos': pedidos_prontos,
    }
    return render(request, 'pedidos/pedidos.html', context)

@login_required
@permission_required('pedidos.add_conta')
def pedir_conta(request):
    if request.method == 'POST':
        cliente = request.user.cliente
        pedidos = Pedido.objects.filter(cliente=cliente).filter(conta=None)
        if pedidos:
            conta = Conta(pago=False)
            conta.save()
            for pedido in pedidos:
                pedido.conta = conta
                pedido.save()
    return HttpResponseRedirect(reverse('pedidos:cardapio'))

@login_required
def detail_conta(request, conta_id):
    conta = get_object_or_404(Conta, pk=conta_id)
    if request.method == 'POST':
        conta.pago = True
        conta.save()
        return HttpResponseRedirect(reverse('pedidos:list_contas'))
    total = 0
    for pedido in conta.pedido_set.all():
        total += pedido.item.preco
    context = {'conta': conta, 'total': total}
    return render(request, 'pedidos/detail_conta.html', context)

@login_required
@permission_required('pedidos.view_conta')
def list_contas(request):
    contas = Conta.objects.filter(pago=False)
    context = {'contas': contas}
    return render(request, 'pedidos/list_contas.html', context)

@login_required
@permission_required('pedidos.view_mesa')
def list_mesas(request):
    mesas_disp = Mesa.objects.filter(disponivel=True)
    mesas_indisp = Mesa.objects.filter(disponivel=False)
    context = {'mesas_disp': mesas_disp, 'mesas_indisp': mesas_indisp}
    return render(request, 'pedidos/list_mesas.html', context)

@login_required
@permission_required('pedidos.view_mesa')
def detail_mesa(request, mesa_id):
    mesa = get_object_or_404(Mesa, pk=mesa_id)
    context = {'mesa': mesa}
    return render(request, 'pedidos/detail_mesa.html', context)

@login_required
@permission_required('pedidos.add_mesa')
def create_mesa(request):
    if request.method == 'POST':
        mesa_form = MesaForm(request.POST)
        if mesa_form.is_valid():
            mesa = Mesa(**mesa_form.cleaned_data)
            mesa.save()
    return HttpResponseRedirect(
        reverse('pedidos:list_mesas')
    )

@login_required
@permission_required('pedidos.change_mesa')
def update_mesa(request, mesa_id):
    mesa = get_object_or_404(Mesa, pk=mesa_id)
    if request.method == 'POST':
        mesa_form = MesaForm(request.POST)
        if mesa_form.is_valid():
            mesa.capacidade = mesa_form.cleaned_data['capacidade']
            mesa.localizacao = mesa_form.cleaned_data['localizacao']
            mesa.disponivel = mesa_form.cleaned_data['disponivel']
            mesa.save()
    return HttpResponseRedirect(
        reverse('pedidos:list_mesas')
    )