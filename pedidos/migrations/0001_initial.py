# Generated by Django 3.2.7 on 2021-11-23 01:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Conta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pago', models.BooleanField(verbose_name='Pago')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=20, verbose_name='Nome')),
                ('preco', models.FloatField(verbose_name='Preço')),
                ('descricao', models.CharField(max_length=255, verbose_name='Descrição')),
                ('foto_url', models.URLField(max_length=255, verbose_name='URL da foto')),
                ('disponivel', models.BooleanField(verbose_name='Disponível')),
            ],
        ),
        migrations.CreateModel(
            name='Mesa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('capacidade', models.IntegerField(verbose_name='Capacidade')),
                ('localizacao', models.CharField(max_length=255, verbose_name='Localização')),
                ('disponivel', models.BooleanField(verbose_name='Disponível')),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pronto', models.BooleanField(verbose_name='Pronto')),
                ('chefcozinha', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.chefcozinha', verbose_name='Chef de Cozinha')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.cliente', verbose_name='Cliente')),
                ('conta', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pedidos.conta', verbose_name='Conta')),
                ('garcom', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.garcom', verbose_name='Garçom')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pedidos.item', verbose_name='Item')),
            ],
        ),
    ]
