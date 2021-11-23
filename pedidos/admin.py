from django.contrib import admin

from pedidos.models import Conta, Item, Mesa, Pedido


admin.site.register(Mesa)
admin.site.register(Item)
admin.site.register(Conta)
admin.site.register(Pedido)
