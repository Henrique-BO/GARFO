from django.db import models
from django.conf import settings
from cpf_field.models import CPFField


class Cliente(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Usuário"
    )
    cpf = CPFField(verbose_name="CPF")
    mesa = models.ForeignKey("pedidos.Mesa", on_delete=models.CASCADE, verbose_name="Mesa")

    def __str__(self):
        return self.user.__str__()

class Gerente(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Usuário"
    )

    def __str__(self):
        return self.user.__str__()

class Garcom(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Usuário"
    )

    def __str__(self):
        return self.user.__str__()

class ChefCozinha(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Usuário"
    )

    def __str__(self):
        return self.user.__str__()
