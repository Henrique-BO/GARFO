from rest_framework import serializers
from django.contrib.auth.models import User

from pedidos.models import Conta, Item, Mesa, Pedido
from accounts.models import Cliente, Gerente, Garcom, ChefCozinha

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
        ]

class ClienteSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Cliente
        fields = [
            'id',
            'user',
            'cpf',
            'mesa',
        ]

class GerenteSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Gerente
        fields = [
            'id',
            'user',
        ]

class GarcomSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Garcom
        fields = [
            'id',
            'user',
        ]

class ChefCozinhaSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = ChefCozinha
        fields = [
            'id',
            'user',
        ]

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = [
            'id',
            'preco',
            'descricao',
            'foto_url',
            'disponivel',
        ]

class PedidoSerializer(serializers.ModelSerializer):
    cliente = ClienteSerializer()
    item = ItemSerializer()
    class Meta:
        model = Pedido
        fields = [
            'id',
            'cliente',
            'item',
            'observacoes',
            'time_realizado',
            'chefcozinha',
            'time_preparando',
            'time_pronto',
            'garcom',
            'time_entregue',
            'conta',
        ]

class MesaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mesa
        fields = [
            'id',
            'capacidade',
            'localizacao',
            'disponivel',
        ]

class ContaSerializer(serializers.ModelSerializer):
    pedido_set = PedidoSerializer(many=True)
    class Meta:
        model = Conta
        fields = [
            'id',
            'pedido_set',
            'pago',
        ]