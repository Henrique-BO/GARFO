from django.db import models

from accounts.models import ChefCozinha, Cliente, Garcom


class Mesa(models.Model):
    capacidade = models.IntegerField(verbose_name="Capacidade")
    localizacao = models.CharField(max_length=255, verbose_name="Localização")
    disponivel = models.BooleanField(verbose_name="Disponível")

    def __str__(self):
        return f"Mesa {self.id}"

class Item(models.Model):
    """Item do cardápio"""
    nome = models.CharField(max_length=255, verbose_name="Nome")
    preco = models.FloatField(verbose_name="Preço")
    descricao = models.CharField(max_length=255, verbose_name="Descrição")
    foto_url = models.URLField(max_length=255, verbose_name="URL da foto")
    disponivel = models.BooleanField(verbose_name="Disponível")

    def __str__(self):
        return f"{self.nome}"

class Conta(models.Model):
    pago = models.BooleanField(verbose_name="Pago")

    def __str__(self):
        return f"Conta {self.id}"

class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, verbose_name="Cliente")
    
    item = models.ForeignKey(Item, on_delete=models.CASCADE, verbose_name="Item")
    observacoes = models.CharField(max_length=255, verbose_name="Observações")

    time_realizado = models.DateTimeField() # quando o pedido foi realizado pelo cliente
    
    chefcozinha = models.ForeignKey(ChefCozinha, on_delete=models.CASCADE, blank=True, null=True, verbose_name="Chef de Cozinha")
    time_preparando = models.DateTimeField(blank=True, null=True) # quando o pedido começou a ser preparado pelo chef de cozinha
    
    time_pronto = models.DateTimeField(blank=True, null=True) # quando o pedido ficou pronto

    garcom = models.ForeignKey(Garcom, on_delete=models.CASCADE, blank=True, null=True, verbose_name="Garçom")
    time_entregue = models.DateTimeField(blank=True, null=True) # quando o pedido foi entregue ao cliente

    conta = models.ForeignKey(Conta, on_delete=models.CASCADE, blank=True, null=True, verbose_name="Conta")

    def __str__(self):
        return f"{self.item}, para {self.cliente}"


