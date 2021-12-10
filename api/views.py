from rest_framework import generics

from pedidos.models import Item, Pedido, Mesa, Conta
from accounts.models import Cliente, Gerente, Garcom, ChefCozinha
from .serializers import (
    ItemSerializer, PedidoSerializer, MesaSerializer, ContaSerializer, 
    ClienteSerializer, GerenteSerializer, GarcomSerializer, ChefCozinhaSerializer
)


class ItemList(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class ItemDetail(generics.RetrieveUpdateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class PedidoList(generics.ListCreateAPIView):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

class PedidoDetail(generics.RetrieveUpdateAPIView):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

class MesaList(generics.ListCreateAPIView):
    queryset = Mesa.objects.all()
    serializer_class = MesaSerializer

class MesaDetail(generics.RetrieveUpdateAPIView):
    queryset = Mesa.objects.all()
    serializer_class = MesaSerializer

class ContaList(generics.ListCreateAPIView):
    queryset = Conta.objects.all()
    serializer_class = ContaSerializer

class ContaDetail(generics.RetrieveUpdateAPIView):
    queryset = Conta.objects.all()
    serializer_class = ContaSerializer

class ClienteList(generics.ListCreateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class ClienteDetail(generics.RetrieveUpdateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class GerenteList(generics.ListCreateAPIView):
    queryset = Gerente.objects.all()
    serializer_class = GerenteSerializer

class GerenteDetail(generics.RetrieveUpdateAPIView):
    queryset = Gerente.objects.all()
    serializer_class = GerenteSerializer

class GarcomList(generics.ListCreateAPIView):
    queryset = Garcom.objects.all()
    serializer_class = GarcomSerializer

class GarcomDetail(generics.RetrieveUpdateAPIView):
    queryset = Garcom.objects.all()
    serializer_class = GarcomSerializer

class ChefCozinhaList(generics.ListCreateAPIView):
    queryset = ChefCozinha.objects.all()
    serializer_class = ChefCozinhaSerializer

class ChefCozinhaDetail(generics.RetrieveUpdateAPIView):
    queryset = ChefCozinha.objects.all()
    serializer_class = ChefCozinhaSerializer

