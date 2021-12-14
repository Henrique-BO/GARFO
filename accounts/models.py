from django.db import models
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save
from cpf_field.models import CPFField
from django.contrib.auth.models import Group, Permission


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


PERMISSIONS = {
    'Gerente': {
        'Mesa': ['add', 'change', 'view'],
        'Item': ['add', 'change', 'view'],
        'Conta': ['view'],
        'Pedido': ['view'],
    },
    'Garcom': {
        'Conta': ['change', 'view'],
        'Item': ['view'],
        'Mesa': ['view'],
        'Pedido': ['entregar', 'view'],
    },
    'ChefCozinha': {
        'Item': ['view'],
        'Mesa': ['view'],
        'Pedido': ['preparar', 'view'],        
    },
    'Cliente': {
        'Conta': ['add'],
        'Item': ['view'],
        'Mesa': ['view'],
        'Pedido': ['add'],
    },
}

@receiver(post_save, sender=Gerente)
@receiver(post_save, sender=Garcom)
@receiver(post_save, sender=ChefCozinha)
@receiver(post_save, sender=Cliente)
def update_permissions(sender, instance, created, **kwargs):
    group_name = sender.__name__
    group, created = Group.objects.get_or_create(name=group_name)
    for model_name in PERMISSIONS[group_name]:
        for permission_name in PERMISSIONS[group_name][model_name]:
            name = f"Can {permission_name} {model_name.lower()}"
            try:
                permission = Permission.objects.get(name=name)
            except:
                print("Permissão não encontrada")
                print(permission_name)
                continue
            group.permissions.add(permission)
    group.user_set.add(instance.user)
    group.save()