from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.forms import fields
from accounts.models import Cliente, Gerente, Garcom, ChefCozinha

class TeamUserLoginForm(AuthenticationForm):
   def __init__(self, * args, ** kwargs): super(TeamUserLoginForm, self).__init__( * args, ** kwargs)

   username = forms.CharField(widget = forms.TextInput(
      attrs = {
         'class': 'form-control',
         'placeholder': 'Nome',
      }))
   password = forms.CharField(widget = forms.PasswordInput(
      attrs = {
         'class': 'form-control',
         'placeholder': 'Senha',
      }))

class ClientCreationForm(forms.ModelForm):
   class Meta:
      model = Cliente
      fields = [
            'cpf',
            'mesa',
        ]
      labels = {
         'cpf': 'CPF',
         'mesa': 'Mesa',
      }
      widgets = {
            'cpf': forms.TextInput(attrs={
               'class': 'form-control', 
               'placeholder': 'CPF'
      })}