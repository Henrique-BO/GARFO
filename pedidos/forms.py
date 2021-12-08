from django import forms
from .models import Item


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