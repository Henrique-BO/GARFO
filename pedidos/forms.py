from django import forms
from .models import Item, Mesa


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = [
            'nome',
            'preco',
            'descricao',
            'foto_url',
            'disponivel',
        ]
        labels = {
            'nome': 'Nome',
            'preco': 'Preço',
            'descricao': 'Descrição',
            'foto_url': 'URL da foto',
            'disponivel': 'Disponível',
        }

class MesaForm(forms.ModelForm):
    class Meta:
        model = Mesa
        fields = [
            'capacidade',
            'localizacao',
            'disponivel',
        ]
        labels = {
            'capacidade': 'Capacidade',
            'localizacao': 'Localização',
            'disponivel': 'Disponível',
        }