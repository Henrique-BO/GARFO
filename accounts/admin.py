from django.contrib import admin

from accounts.models import ChefCozinha, Cliente, Garcom, Gerente


admin.site.register(Cliente)
admin.site.register(Gerente)
admin.site.register(ChefCozinha)
admin.site.register(Garcom)